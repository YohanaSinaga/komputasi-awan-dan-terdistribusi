# Jurnal Proses — Tugas 4

## Jalur yang dipilih

- [RPC / MQ / keduanya], alasan: Kami memilih  **keduanya (RPC dan MQ)** . RPC digunakan untuk komunikasi synchronous, yaitu ketika modul membutuhkan respons secara langsung seperti pengecekan saldo dan proses pembayaran. Sedangkan MQ digunakan untuk komunikasi asynchronous, yaitu untuk mengirim notifikasi pembayaran tanpa harus menunggu modul penerima.

Pada bagian RPC, kami menggunakan `xmlrpc` dari Python untuk menghubungkan modul Pesanan dengan modul Pembayaran. Server dijalankan pada port 8000, kemudian client memanggil fungsi `cek_saldo()` dan `proses_pembayaran()`.

Hasil percobaan menunjukkan bahwa `cek_saldo("user1")` mengembalikan saldo Rp50.000. Kemudian ketika dilakukan pembayaran sebesar Rp20.000, hasilnya sukses dan saldo akhir menjadi Rp30.000.

Kami juga mencoba memberikan delay pada server untuk melihat cara kerja komunikasi synchronous. Client harus menunggu sampai server memberikan respons. Dari percobaan tersebut terlihat bahwa RPC cocok digunakan untuk proses yang membutuhkan hasil secara langsung.

Untuk bagian MQ, RabbitMQ dijalankan menggunakan Docker pada laptop salah satu anggota kelompok. Queue yang digunakan adalah `pembayaran_berhasil`.

Pada saat setup Publisher, terdapat error `No module named 'pika'` karena library `pika` belum terpasang. Setelah membuat virtual environment dan meng-install `pika` melalui `requirements.txt`, Publisher dapat dijalankan.

Publisher kemudian mengirimkan 3 pesan pembayaran, yaitu user1 sebesar Rp20.000, user2 sebesar Rp40.000, dan user3 sebesar Rp60.000.

Karena RabbitMQ berada di laptop teman, awalnya kami menggunakan `localhost` tetapi koneksi tidak berhasil. Setelah menggunakan IP laptop teman dan melakukan pengecekan port 5672, koneksi berhasil. Pesan yang dikirim Publisher kemudian terlihat pada RabbitMQ Management Dashboard.

Consumer dijalankan pada laptop yang berbeda dengan RabbitMQ. Setelah koneksi berhasil, Consumer menggunakan queue `pembayaran_berhasil` untuk menerima pesan dari Publisher.

Kami melakukan uji dengan mematikan Consumer terlebih dahulu, kemudian menjalankan Publisher untuk mengirim 3 pesan. Pada RabbitMQ Dashboard terlihat `Ready = 3` dan `Unacked = 0`. Setelah Consumer dijalankan kembali, ketiga pesan berhasil diterima dan diproses.

Consumer menampilkan notifikasi pembayaran untuk user1, user2, dan user3. Setelah pesan diberikan `basic_ack`, jumlah pesan pada queue berubah menjadi `Ready = 0`.

## Kendala teknis

* **Bagian RPC:** Tidak ada kendala besar karena `xmlrpc` sudah tersedia di Python. Kami melakukan percobaan dengan memberikan delay pada server untuk membuktikan bahwa client menunggu respons.
* **Bagian Docker/RabbitMQ dan Publisher:** Awalnya library `pika` belum terpasang sehingga muncul error `No module named 'pika'`. Setelah library di-install, Publisher dapat dijalankan. Selain itu, koneksi menggunakan `localhost` tidak bisa digunakan karena RabbitMQ berada di laptop teman.
* **Bagian Consumer:** Saat pertama kali mencoba koneksi ke RabbitMQ, `TcpTestSucceeded` menunjukkan `False`. Setelah menggunakan IP yang benar dari laptop teman dan memastikan port 5672 dapat diakses, koneksi berhasil.

## Uji "pesan tidak hilang" (khusus Jalur B)

- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati:
- **Bagian Docker/RabbitMQ:** RabbitMQ tetap menyimpan pesan yang dikirim ke queue walaupun Consumer sedang tidak berjalan. Saat Consumer dimatikan dan Publisher mengirim 3 pesan, dashboard menunjukkan `Ready = 3`.
- **Publisher:** Publisher berhasil mengirimkan 3 event pembayaran tanpa harus menunggu Consumer memproses pesan tersebut.
- **Consumer:** Setelah Consumer dijalankan kembali, ketiga pesan yang sebelumnya tersimpan di RabbitMQ berhasil diterima dan diproses. Setelah `basic_ack`, queue menunjukkan `Ready = 0`.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
