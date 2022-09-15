Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
-> ![Gambar Bagan](/GambarBagan/messageImage_1663210215540.jpg)

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
-> Virtual environment adalah alat yang berguna untuk mengelola ruang terpisah sebuah proyek dengan pustaka dan dependensi. Lingkungan ini dirancang khusus untuk proyek tertentu, dan tidak berinterfer dengan dependensi lain. Proyek ini masih menggunakan virtual environment karena masing-masing proyek mempunyai kebutuhan yang berbeda-beda. Kita masih bisa membuat aplikasi web django tanpa virtual environment. Namun, karena ada requirements.txt, akan lebih mudah menggunakan virtual environment.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
-> 1. jika kita belum memiliki katalog app, maka kita buat terlebih dahulu
   2. tambahkan "katalog" ke INSTALLED_APPS ke settings.py
   3. kita diminta untuk membuat kelas CatalogItem model di models.py
   4. buat fungsi show_catalog di views.py yang di dalamnya ada nama, npm, dan ada data_katalog yang berisi barang-barangnya.
   5. buat from django.urls import path dan from katalog.views import show_katalog ke urlpatterns pada urls.py
   6. buat loop yang mengaco pada catalogitem pada katalog.html yang berisi name, price, stock, rating, description, item_url.
   7. Kita run untuk mengecek apakah proye yang kita buat berjalan atau tidak.
   8. Apabila sudah berjalan, deploy ke Heroku