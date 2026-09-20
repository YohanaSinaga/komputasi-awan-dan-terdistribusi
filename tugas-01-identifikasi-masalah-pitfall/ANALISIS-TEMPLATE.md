# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama               | NIM          | Kontribusi                             |
| ------------------ | ------------ | -------------------------------------- |
| Yohanna Purnomo    | 103072400127 | The network is reliable                |
| Yohana Sinaga      | 103072400009 | Latency is zero                        |
| Laura Chyndearni S | 103072400049 | Single Point of Failure dan Scalability|

## Pitfall 1: The network is reliable — ditulis oleh YOHANNA PURNOMO

**Bukti di skenario:**

network is always reliable, no need fo retry

**Kenapa ini keliru:** Dalam sistem terdistribusi, komunikasi antarservice  bergantung pd jaringan shg permintaan tidak selalu berhasil. Komunikasi dapat mengalami kegagalan atau gangguan sementara. Krn itu, sistem perlu mengantisipasi kemungkinan permintaaan tidak mendapatkan respons dan tidak boleh menganggap jaringan selalu dapat diandalkan.

**Dampak ke FoodGo:** Ketikaa terjadi gangguan komunikasi antara service, permintaan dari satu modul dapat gagal tanpa adanya percobaan ulang. Dalam kondisi trafik tinggi, kegagalan komunikasi dapat membuat proses pemesanan atau pembayaran terganggu. Hal ini dapat menyebabkan sebagian permintaan pengguna gagal, sementara aplikasi secara keseluruhan sudah berada dalam kondisi terbebani.

**Solusi desain awal:** FoodGo dapat menambahkan timeout dan mekanisme retry dengan jumlah percobaan yang terbatas. Jeda antarpercobaan juga dapat dibuat bertahap ( backoff ) agar sistem tidak langsung mengirim permintaan berulang ketika service sedang mengalami masalah. Circuit breaker juga dapat digunakan untuk menghentikan sementara permintaan ke service yang terus mengalami kegagalan.

**Trade-off:** Retry dapat menambah jumlah request ketika sistem sedang bermasalah sehingga justru dapat meningkatkan beban. Karena itu, jumlah percobaan perlu dibatasi. Penggunaan circuit breaker juga membuat sistem menjadi lebih kompleks karena harus menentukan kapan permintaan dihentikan dan kapan dicoba kembali.

---

## Pitfall 2: Latency Is Zero — ditulis oleh Yohana Sinaga

**Bukti di skenario:** tidak ada *timeout* sama sekali pada pemanggilan antarservice dan secara khusus modul pesanan memanggil modul pembayaran dan menungu tanpa batas waktu.

**Kenapa ini keliru:** Dalam sistem terdistribusi, komunikasi antarservice membutuhkan waktu. Respons dari service lain tidak selalu datang dalam waktu yang sama karena dapat dipengaruhi oleh kondisi service dan tingginya jumlah permintaan. Oleh karena itu, sistem tidak boleh menganggap respons antarservice selalu tersedia dengan cepat.

**Dampak ke FoodGo:** Ketika modul Payment membutuhkan waktu lama untuk memberikan respons, modul Order akan tetap menunggu karena tidak memiliki  timeout. Jika banyak permintaan Order mengalami kondisi yang sama saat trafik sedang tinggi, semakin banyak proses yang tertahan menunggu Payment. Resource server kemudian ikut terbebani, sehinga aplikasi menjadi semakin lambat dan beberapa permintaan pengguna akhirnya mengalami  timeout. Kondisi ini dapat ikut berkontribusi terhadap server yang mengalami  crash

**Solusi desain awal:** FoodGo dapat memberikan batas waktu ( *timeout* ) pada pemanggilan dari modul Order ke modul Payment. Dengan demikian, Order tidak akan menunggu Payment tanpa batas. Untuk proses tertentu yang tidak harus langsung mendapatkan respons, FoodGo juga dapat menggunakan komunikasi asynchronous sehingga Order tidak harus terus menunggu proses dari Payment selesai

**Trade-off:** Timeout yang terlalu singkat dapat membuat permintaan dianggap gagal padahal Payment sebenarnya masih memprosesnya. Sementara itu, penggunaan komunikasi asynchronous membuat alur sistem menjadi lebih kompleks karena hasil proses tidak selalu langsung diterima oleh modul yang meminta.

---

## Pitfall 3: Single Point of Failure dan Scalability — ditulis oleh Laura Chyndearni Saragih

**Bukti di skenario:**  

Saat trafik naik, satu server menangani semua modul FoodGo, yaitu pesanan, pembayaran, dan notifikasi kurir. Semua modul tersebut berjalan dalam satu proses monolitik yang sama. Akibatnya, server menjadi kewalahan ketika jumlah trafik meningkat.

**Kenapa ini keliru:**  

Satu server yg menangani banyak modul membuat semua modul menggunakan resource yg sama. Ketika jumlah pengguna dan pesanannya meningkat, beban yg diterima server jg ikut meningkat. Hal ini menunjukkan adanya masalah scalability karena sistem belum mampu menangani peningkatan beban dengan baik.

Selain itu, penggunaan satu server untuk banyak fungsi juga membuat server tersebut menjadi Single point of failure yg artinya jika server tersebut mengalami masalah/crash, beberapa fungsi FoodGo yg berjalan di dalamnya dapat ikut terganggu.

**Dampak ke FoodGo:**  

Ketika jam makan sian/promo besar, jumlah pesanan meningkat. Order, Payment, dan Notification semuanya menggunakan resource dari server yang sama. Server akhirnya kewalahan sehingga aplikasi menjadi lambat dan beberapa request mengalami timeout.

Jika bebannya semakin tinggi sampai server crash bukan hanya satu fungsi yang tergangg tetapi modul pesanan, pembayaran, dan notifikasi yang berada dalam proses yang sama jg dapat ikut berhenti. Akibatnya, satu masalah pada server dapat mempengaruhi sebagian besar sistem FoodGo.

**Solusi desain awal:**  

FoodGo dapat mulai memisahkan modul berdasarkan fungsi menjadi service/proses yang terpisah. Misalnya Order Service, Payment Service, dan Notification Service tidak semuanya dijalankan dalam satu proses yang sama.

Dengan pemisahan tersebut, service yang memiliki beban paling tinggi dapat ditingkatkan kapasitasnya secara terpisah sesuai kebutuhan. FoodGo jg tidak terlalu bergantung pada satu proses untuk menjalankan seluruh fungsi utama aplikasi.

**Trade-off:**  

Pemisahan service dapat membantu mengurangi ketergantungan pada satu server dan membuat sistem lebih mudah dikembangkan sesuai kebutuhan. Namun, sistem menjadi lebih kompleks karena service harus berkomunikasi melalui jaringan. Tim juga perlu menangani monitoring, deployment, dan kemungkinan terjadinya kegagalan komunikasi antar servicnya.

## Kesimpulan Kelompok

Berdasarkan hasil diskusi, kami menemukan bahwa masalah FoodGo bukan hanya karena jumlah pengguna nya saja yg meningkat, tetapi juga karena ada beberapa kesalahan di perancangan sistemnya. Masalah yang kami temukan yaitu menganggap jaringan selalu reliable, tidak adanya timeout saat service saling berkomunikasi, dan satu server yang menangani banyak fungsi sekaligus.

Dari masalah tersebut, kami mengusulkan beberapa perbaikan seperti menggunakan retry dengan batas percobaan dan backoff, memberikan timeout pada komunikasi antarservice, serta memisahkan service Order, Payment, dan Notification. Dengan begitu, sistem tidak terlalu bergantung pada satu bagian saja dan lebih siap ketika jumlah request meningkat.

Namun, setiap solusi juga memiliki kekurangannya. Misalnya, retry yang terlalu banyak bisa menambah beban, sedangkan pemisahan service membuat sistem lebih kompleks karena service harus saling berkomunikasi melalui jaringan. Jadi, perbaikannya tetap perlu disesuaikan dengan kondisi sistem FoodGo.

Secara garis besar, FoodGo perlu memiliki sistem yang lebih siap menghadapi gangguan dan peningkatan trafik. Hasil analisis ini nantinya dapat menjadi dasar untuk merancang arsitektur FoodGo yang lebih baik pada Tugas 2.
