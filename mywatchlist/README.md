# Link aplikasi Heroku : https://tugas2-pbp-apin.herokuapp.com/mywatchlist/
1. Jelaskan perbedaan antara JSON, XML, dan HTML!
 -> JSON (JavaScript Object Notation) merupakan turunan dari Object JavaScript dan didesain menjadi self-describing, sehingga JSON sangat mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data.
 -> XML (eXtensible Markup Language) didesain menjadi self-descriptive, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data.
 -> HTML (Hypertext Markup Language) adalah pemrograman dengan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser agar halaman tersebut dapat ditampilkan secara benar.

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
  -> untuk mengirimkan data dari satu stack ke stack lainnya dan bentuknya bisa bermacam-macam
  
3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  - buat aplikasi bernama mywatchlist
  - Buka settings.py di folder project_django dan tambahkan aplikasi wishlist ke dalam variabel INSTALLED_APPS tambahkan 'mywatchlist'
  - pada models.py buat 
    ```
    class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()
    ```
  - kita migrate
  - buat folder fixtures dan di dalamnya ada file initial_watchlist_data.json 
    ```
    [
    {
        "model":"mywatchlist.MyWatchList",
        "pk":1,
        "fields":{
            "watched":"Yes",
            "title":"Pengabdi Setan 2 : Communion",
            "rating": "4.5",
            "release_date": "4 Agustus 2022",
            "review":"Filmnya serem."
        }
    }
    ... lanjut sampai 10
    ```
  - masukkan database Django gunakan dengan "python manage.py loaddata initial_watchlist_data.json"
  - buka views.py lalu buat fungsi dengan parameter request. Mereturn "return render(request, "watchlist.html", context)"
  - buat folder templates dan di dalamnya ada file mywatchlist.html 
    ```
    {% extends 'base.html' %}

    {% block content %}

    <h5>Name: </h5>
    <p>{{nama}}</p>

    <h5>Student ID: </h5>
    <p>{{npm}}</p>

    <h2>Pesan: </h2>
    <p>{{pesan}}</p>

    <table>
        <tr>
            <th>Watched</th>
            <th>Title</th>
            <th>Rating</th>
            <th>Release Date</th>
            <th>Review</th>
        </tr>
        {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
        {% for movie in list_mywatchlist %}
            <tr>
                <th>{{movie.watched}}</th>
                <th>{{movie.title}}</th>
                <th>{{movie.rating}}</th>
                <th>{{movie.release_date}}</th>
                <th>{{movie.review}}</th>
            </tr>
        {% endfor %}
    </table>
    {% endblock content %}
    '''
  - menghubungkan models dengan views dan template
  - delivery data dengan tipe xml dan json
  - buat fungsi dengan paramter request yang mengembalikan data dalam bentuk xml dan json
  - kita deploy ke Heroku dan push ke repository github tugas 2

# Screenshot JSON
<img width="960" alt="image" src="https://user-images.githubusercontent.com/112617994/191603887-b0d31b87-ab84-4419-ac1b-67fba57680fd.png">

# Screenshot XML
<img width="960" alt="image" src="https://user-images.githubusercontent.com/112617994/191603835-f3cf6515-5ed3-48fe-b8c7-f1a4b1ad452b.png">

