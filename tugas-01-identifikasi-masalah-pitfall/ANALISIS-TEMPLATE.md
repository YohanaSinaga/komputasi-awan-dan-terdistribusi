# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama               | NIM          | Kontribusi                             |
| ------------------ | ------------ | -------------------------------------- |
| Yohanna Purnomo    | 103072400127 | The network is reliable                |
| Yohana Sinaga      | 103072400009 | Latency is zero                        |
| Laura Chyndearni S | 103072400049 | Single Point of Failure / skalabilitas |

## Pitfall 1: The network is reliable — ditulis oleh YOHANNA PURNOMO

**Bukti di skenario:**

network is always reliable, no need fo retry

**Kenapa ini keliru:** Dalam sistem terdistribusi, komunikasi antarservice  bergantung pd jaringan shg permintaan tidak selalu berhasil. Komunikasi dapat mengalami kegagalan atau gangguan sementara. Karena itu, sistem perlu mengantisipasi kemungkinan permintaaan tidak mendapatkan respons dan tidak boleh menganggap jaringan selalu dapat diandalkan.

**Dampak ke FoodGo:** Ketika terjadi gangguan komunikasi antara service, permintaan dari satu modul dapat gagal tanpa adanya percobaan ulang. Dalam kondisi trafik tinggi, kegagalan komunikasi dapat membuat proses pemesanan atau pembayaran terganggu. Hal ini dapat menyebabkan sebagian permintaan pengguna gagal, sementara aplikasi secara keseluruhan sudah berada dalam kondisi terbebani.

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

## Pitfall 3: *Single Point of Failure / Skalabilitas* — ditulis oleh **Laura Chyndearni Saragih**

**Bukti di Skenario:** Skenario menyebutkan:

 “Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama.”

Skenario juga menyebutkan:

 “Server backend kadang *crash* total dan perlu di-restart manual.”

Dari dua bagian tersebut, terlihat bahwa semua modul FoodGo masih bergantung pada satu server dan satu proses.

**Kenapa Ini Keliru?:** Menjalankan semua modul dalam satu proses dan satu server membuat modul pesanan, pembayaran, dan notifikasi kurir menggunakan resource yang sama, seperti CPU, memori, dan kapasitas pemrosesan.

Satu server memiliki kapasitas yang terbatas. Ketika jumlah permintaan meningkat, semua modul harus berbagi resource yang tersedia. Akibatnya, peningkatan beban pada satu bagian dapat memengaruhi kinerja bagian lainnya.

Selain itu, jika server tersebut mengalami gangguan atau *crash*, semua modul yang bergantung pada server tersebut dapat ikut berhenti. Kondisi ini dapat disebut sebagai Single Point of Failure, karena kegagalan pada satu komponen dapat menyebabkan layanan lain ikut terganggu.

Masalah ini juga berkaitan dengan skalabilitas. Jika hanya satu modul yang mengalami peningkatan beban, FoodGo tidak dapat dengan mudah menambah kapasitas modul tersebut tanpa mempertimbangkan seluruh aplikasi yang masih berjalan dalam proses yang sama.

**Dampak ke FoodGo:** Saat terjadi lonjakan pesanan pada jam makan siang atau ketika promo besar, jumlah permintaan yang masuk ke FoodGo meningkat.

Karena Order, Payment, dan Notification berjalan pada server yang sama, semua modul menggunakan resource yang sama. Ketika jumlah request semakin banyak, server menjadi semakin terbebani.

Alur masalahnya dapat digambarkan secara sederhana:

Trafik meningkat → request bertambah → semua modul menggunakan resource server yang sama → server kewalahan → aplikasi menjadi lambat → server dapat crash

Jika server sampai mengalami *crash*, modul pesanan, pembayaran, dan notifikasi kurir ikut terdampak karena semuanya berada dalam server dan proses yang sama.

Akibatnya, pengguna dapat mengalami masalah seperti:

1. **Tidak dapat membuat pesanan**
2. **Proses pembayaran terganggu**
3. **Notifikasi kurir tidak berjalan**
4. **Aplikasi menjadi lambat**
5. **Layanan harus menunggu sampai server di-restart**

Jadi, masalah pada satu server dapat berdampak ke seluruh fungsi utama FoodGo.

**Solusi Desain Awal:** FoodGo dapat mulai memisahkan modul utama menjadi beberapa service, misalnya:

- **Order Service** — menangani proses pemesanan.
- **Payment Service** — menangani proses pembayaran.
- **Notification Service** — menangani notifikasi kepada pengguna dan kurir.

Dengan pemisahan tersebut, setiap service dapat dikelola dan ditingkatkan kapasitasnya secara lebih mandiri.

Contohnya, ketika terjadi promo besar dan beban pada Order Service meningkat, FoodGo dapat menambah kapasitas Order Service tanpa harus menambah kapasitas seluruh modul lainnya.

Pemisahan service juga dapat mengurangi dampak kegagalan. Jika Notification Service mengalami masalah, Order Service dan Payment Service tidak harus langsung berhenti, selama ketergantungan antarservice dirancang dengan baik.

Untuk tim kecil seperti FoodGo, pemisahan ini dapat dilakukan secara bertahap, tidak harus langsung mengubah seluruh aplikasi menjadi banyak service sekaligus.

**Trade-off:** Pemisahan service dapat membantu meningkatkan skalabilitas, tetapi membuat sistem menjadi lebih kompleks dibandingkan monolitik.

Pada sistem monolitik, semua modul berada dalam satu proses sehingga komunikasi antarbagian relatif sederhana. Setelah dipisahkan menjadi beberapa service, komunikasi harus dilakukan melalui jaringan.

Akibatnya, FoodGo perlu menangani masalah tambahan seperti:

- **Timeout**
- **Kegagalan komunikasi antarservice**
- **Monitoring**
- **Deployment masing-masing service**
- **Pengelolaan koneksi antarservice**

Selain itu, pemisahan servicetidak otomatis menghilangkan semua Single Point of Failure. Jika beberapa service masih bergantung pada satu komponen yang sama, komponen tersebut tetap dapat menjadi titik kegagalan.

Karena itu, menurut analisis kami, pemisahan service sebaiknya dilakukansecara bertahap dan disertai pengelolaan komunikasi antarservice yang baik. Dengan cara tersebut, FoodGo dapat meningkatkan skalabilitas tanpa menambah kompleksitas sistem secara berlebihan.

## Kesimpulan Kelompok

Dari ketiga pitfall yang ditemukan, FoodGo membutuhkan sistem yang lebih decoupled agar gangguan jaringan, keterlambatan antarmodul, atau beban pada satu modul tidak langsung mengganggu seluruh sistem. Setiap layanan perlu dapat berkomunikasi dengan lebih terkontrol dan tidak saling bergantung secara berlebihan. Hal ini menjadi dasar untuk  Tugas **2 ,** yaitu merancang arsitektur menggunakan SOA atau kombinasi SOA dengan Publish-Subscribe agar modul Pesanan, Pembayaran, Kurir/Notifikasi, dan Katalog Resto dapat berjalan lebih terpisah dan fleksibel.
