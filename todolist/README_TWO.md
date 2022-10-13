1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
--> asynchronus programming adalah kemampuan program kita dalam menjalankan tasknya secara bersamaan
--> synchronus programming adalah sebuah programming model dimana operasinya berjalan secara sekuensial
2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah sebuah paradigma dimana objects, services, dll. berhubungan secara tidak langsung dengan mengirimkan pesan satu sama lain melalui intermediary. Contohnya dalam tugas ini adalah ketika tambah tugas, maka akan muncul modal berupa pop up
3. Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan AJAX pada assynchronus programming berguna ketika kita menambah task, maka tidak perlu reload
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Tambahkan berikut pada views.py
```
    def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")

def add_todolist(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_barang = Task.objects.create(user=request.user, is_finished=False, title = title, description=description,date=datetime.datetime.now())
        new_barang.save()
        return HttpResponse(b"CREATED")

    return HttpResponseNotFound()
```
- kemudian pada urls.py tambahkan berikut 
```
    path("json/",show_json,name="show_json"),
    path("add/",add_todolist,name="add_todolist"),
```
- Teruntuk tombol pop up tambah task, kita akan membuat modal dengan implementasi kode berikut
```
    <div class="modal" tabindex="-1" id="exampleModal">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form id="form" onsubmit="return false;">
            {% csrf_token %}
            <div class="mb-3">
                <label for="recipient-name" class="col-form-label">Judul:</label>
                <input type="text" class="form-control" id="recipient-name" name="title">
            </div>
            <div class="mb-3">
                <label for="message-text" class="col-form-label">Deskripsi:</label>
                <textarea class="form-control" id="message-text" name="description"></textarea>
            </div>
            
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary"  id="button" data-bs-dismiss="modal">Tambah</button>
        </form>
        </div>
        </div>
    </div>
    </div>
```
- ketika button tambah di klik, akan mengirim request dengan implementasi kode sebagai berikut
```
    $("#button").click(function() {

    if ($("#recipient-name").val() && $("#message-text").val()) {
      fetch("{% url 'todolist:add_todolist' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(getTask)
    }
    return false;
  })
```
- ketika kita baru akses pertama kali, kemudian kita load. Todolist akan muncul
```
    $(document).ready(function(){
    $.get("/todolist/json", function(data) {
     for (i=0;i<data.length;i++){
        $("#container").append(`
      <div class="col">
      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h4 class="card-title">${data[i].fields.title}</h4>
          <h5 class="card-subtitle mb-2 text-muted">${data[i].fields.date}</h5>
          <p class="card-text">${data[i].fields.description}</p>
          {% if task.is_finished  %}
          <a href="update/${data[i].pk}}" class="card-link">Selesai</a>
          {% else %}
          <a href="update/${data[i].pk}" class="card-link">Belum Selesai</a>
          {% endif %}
          <a href="hapus/${data[i].pk}" class="card-link">Hapus</a>
        </div>
      </div>
    </div>`)
      }
    });
  } )
```
- Kalau kita menambah, cardnya akan reload dengan kode sebagai berikut :
```
      var getTask = function(data){
        $("#container").empty();
        $.get("/todolist/json", function(data) {
        for (i=0;i<data.length;i++){
            $("#container").append(`
        <div class="col">
        <div class="card" style="width: 18rem;">
            <div class="card-body">
            <h4 class="card-title">${data[i].fields.title}</h4>
            <h5 class="card-subtitle mb-2 text-muted">${data[i].fields.date}</h5>
            <p class="card-text">${data[i].fields.description}</p>
            {% if task.is_finished  %}
            <a href="update/${data[i].pk}}" class="card-link">Selesai</a>
            {% else %}
            <a href="update/${data[i].pk}" class="card-link">Belum Selesai</a>
            {% endif %}
            <a href="hapus/${data[i].pk}" class="card-link">Hapus</a>
            </div>
        </div>
        </div>`)
        }
        });
    } 
```