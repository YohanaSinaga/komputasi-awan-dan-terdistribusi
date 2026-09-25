
# Tugas 2 - Perancangan Arsitektur FoodGo

## 1. Gaya Arsitektur yang dipilih

Kombinasi Service-Oriented Architecture (SOA) + Publish-Subscribe (Pub-Sub). 

Pelanggan perlu tahu seketika apakah pembayarannya berhasil sebelum pesanan dilanjutkan, sifat komunikasinya butuh jawaban pasti dan sinkron, sehingga gaya yang cocok adalah Service-Oriented Architecture(SOA).

Resto perlu diberi tahu ada pesanan baru, kurir perlu diberi tahu ada tugas baru, pelanggan perlu diberi tahu status kurir, sifat komunikasinya tidak perlu jawaban langsunh, banyak penerima, boleh sedikit tertunda, sehingga gaya yang cocok adalah Publish-Subscribe(Pub-Sub).

Bagian transaksi inti (Pesanan - Pembayaran) tetap menggunakan pola SOA berbasis *request-response* karena keputusan "bayar berhasil/gagal" harus pasti sebelum sistem melangkah ke tahap berikutnya, kalau ini dibuat asinkron, sistem bisa saja melanjutkan pesanan yang sebenarnya pembayarannya gagal. Sebaliknya, **koordinasi lintas tim** (resto, kurir, notifikasi ke pelanggan) memakai Pub-Sub lewat  *message broker* , sehingga Service Pesanan **tidak pernah tahu dan tidak peduli** siapa saja yang mendengarkan event-nya.
