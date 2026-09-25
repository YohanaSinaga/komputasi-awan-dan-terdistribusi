
# Tugas 2 - Perancangan Arsitektur FoodGo

## Kelompok

| Nama                     | NIM          | Bagian yang dikerjakan               |
| ------------------------ | ------------ | ------------------------------------ |
| Yohana Sinaga            | 103072400009 | SOA dan Service                      |
| Yohanna Purnomo          | 103072400127 | Publish-Subscribe dan Message Broker |
| Laura Chyndearni Saragih | 103072400049 | Alur komunikasi dan trade-off        |

## 1. Gaya Arsitektur yang Dipilih

Kami memilih kombinasi **Service-Oriented Architecture (SOA)** dan **Publish-Subscribe (Pub-Sub)**.

Pelanggan perlu tahu seketika apakah pembayarannya berhasil sebelum pesanan dilanjutkan. Sifat komunikasinya membutuhkan jawaban yang pasti dan sinkron, sehingga bagian ini menggunakan **Service-Oriented Architecture (SOA)** dengan pola komunikasi *request-response*.

Resto perlu diberi tahu ketika ada pesanan baru, kurir perlu diberi tahu ketika ada tugas baru, dan pelanggan perlu mendapatkan informasi mengenai status kurir. Sifat komunikasi tersebut tidak selalu membutuhkan jawaban langsung, dapat memiliki beberapa penerima, dan boleh diproses sedikit tertunda. Oleh karena itu, bagian tersebut menggunakan **Publish-Subscribe (Pub-Sub)**.

Bagian transaksi inti, yaitu **Pesanan - Pembayaran**, tetap menggunakan pola SOA berbasis *request-response* karena keputusan "pembayaran berhasil atau gagal" harus diketahui sebelum sistem melanjutkan proses berikutnya. Jika proses tersebut dibuat sepenuhnya asinkron, sistem dapat melanjutkan proses pesanan sebelum mengetahui hasil pembayaran.

Sebaliknya, **koordinasi lintas layanan** seperti resto, kurir, dan notifikasi pelanggan menggunakan Pub-Sub melalui *message broker*. Dengan cara ini, Order Service tidak perlu mengetahui secara langsung siapa saja yang menerima event yang dikirimkannya Catalog Resto Service, Courier Service, dan Notification Service masing-masing berlangganan event yang relevan bagi mereka.


## 8. Kesimpulan

FoodGo membutuhkan arsitektur yang lebih terpisah dibandingkan arsitektur monolitik sebelumnya. Kombinasi SOA dan Publish-Subscribe digunakan karena kedua pendekatan tersebut memiliki fungsi yang berbeda.

SOA digunakan untuk bagian yang membutuhkan kepastian langsung, yaitu pesanan dan pembayaran. Publish-Subscribe digunakan untuk menyebarkan event kepada service yang membutuhkan Catalog Resto Service, Courier Service, dan Notification Service tanpa membuat Order Service bergantung langsung kepada semua penerima, dan dengan urutan event yang menjamin resto menerima notifikasi terlebih dahulu sebelum kurir ditugaskan.

Dengan rancangan tersebut, perubahan atau deployment pada satu service (misalnya Courier Service atau Notification Service) tidak lagi menyebabkan seluruh aplikasi FoodGo ikut berhenti. Namun, pemisahan service dan penggunaan message broker juga menambah kompleksitas: kegagalan, keterlambatan, dan duplikasi event perlu ditangani secara eksplisit, dan proses debugging membutuhkan bantuan *correlation ID* karena alurnya tidak lagi berjalan dalam satu proses tunggal seperti sebelumnya.
