## LINK HEROKUAPP : 
1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Internal CSS biasanya dituliskan dalam bentuk tag. Internal CSS hanya bisa digunakan untuk satu halaman web saja dan tidak bisa digunakan untuk halaman lainnya. 
Kelebihannya sebagai berikut :
- perubahan hanya pada satu halaman
- HTML dan CSS dalam satu file sehingga tidak perlu mengupload beberapa file
- Class dan ID bisa digunakan oleh internal stylesheet
Kekurangannya sebagai berikut :
- Karena hanya bisa satu file, jadi tidak efisien apabila kita ingin tampilannya sama
- Performa menjadi lama
Eksternal CSS biasanya dituliskan terpisah dengan kode HTML, sehingga ada file khusus ekstensi .css yang biasanya diletakkan pada <head>
Kelebihannya sebagai berikut :
- Ukuran file menjadi lebih kecil
- Performa lebih cepat
- File CSS bisa digunakan di berbagai file
Kekurangannya sebagai berikut :
- Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.
Inline CSS adalah kode yang langsung ditulis dalam atribut elemen HTML, dimana setiap elemen memiliki atribut style
Kelebihannya sebagai berikut :
- Sangat menguji untuk melihat suatu perubahan
- Bisa memperbaiki kode dengan simpel
- Performa lebih cepat
Kekurangannya sebagai berikut :
- Hanya bisa diterapkan pada satu elemen

2. Jelaskan tag HTML5 yang kamu ketahui.
- <html> --> untuk menentukan dokumen HTML
- <h1> to <h6> --> untuk membuat heading
- <title> --> membuat judul dari sebuah halaman
- <body> --> membuat tubuh dari suatu halaman
- <button> --> untuk membuat tombol yang bisa ditekan

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- <p>
``` 
    p {
    color: blue;
}
```
itu berarti semua elemen <p> akan berubah warna menjadi biru
- <.> 
```
.pink {
  color: white;
  background: pink;
  padding: 5px;
}
```
memilih elemen berdasarkan nama class
- <#>
```
#header {
    background: teal;
    color: white;
    height: 100px;
    padding: 50px;
}
```
mirip dengan class, namun selector ID hanya saja bersifat unik
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Melakukan pemanggilan framework Bootstrap untuk semua file html
- Mengedit login.html
```
<style>
    table{
        margin: auto;
        font-size: 25px;
        font-family: Arial, Helvetica, sans-serif;
        font-weight: bold;
        color: rgb(90, 219, 242);
    }
</style>
...
 <p style="text-align:center">Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a></p>
```
- Pada todolist kita buat card dan mengedit kode menjadi demikian
```
<div class="container-fluid p-3">
<div class="row row-cols-1 row-cols-md-4 g-4">
  {% for task in list %}
  <tr>
      <div class="col">
      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h4 class="card-title">{{task.title}}</h4>
          <h5 class="card-subtitle mb-2 text-muted">{{task.date}}</h5>
          <p class="card-text">{{task.description}}</p>
          {% if task.is_finished  %}
          <a href="update/{{task.pk}}" class="card-link">Selesai</a>
          {% else %}
          <a href="update/{{task.pk}}" class="card-link">Belum Selesai</a>
          {% endif %}
          <a href="hapus/{{task.pk}}" class="card-link">Hapus</a>
        </div>
      </div>
    </div>
  </tr>
{% endfor %}
</div>
</div>
```
- Tambahkan head html pada seluruh halaman