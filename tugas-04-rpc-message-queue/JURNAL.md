# Jurnal Proses — Tugas 4

## Jalur yang dipilih

- [RPC / MQ / keduanya], alasan: Kami memilih  **keduanya (RPC dan MQ)** . RPC digunakan untuk komunikasi synchronous, yaitu ketika modul membutuhkan respons secara langsung seperti pengecekan saldo dan proses pembayaran. Sedangkan MQ digunakan untuk komunikasi asynchronous, yaitu untuk mengirim notifikasi pembayaran tanpa harus menunggu modul penerima.

Pada bagian RPC, kami menggunakan `xmlrpc` dari Python untuk menghubungkan modul Pesanan dengan modul Pembayaran. Server dijalankan pada port 8000, kemudian client memanggil fungsi `cek_saldo()` dan `proses_pembayaran()`.

Hasil percobaan menunjukkan bahwa `cek_saldo("user1")` mengembalikan saldo Rp50.000. Kemudian ketika dilakukan pembayaran sebesar Rp20.000, hasilnya sukses dan saldo akhir menjadi Rp30.000.

Kami juga mencoba memberikan delay pada server untuk melihat cara kerja komunikasi synchronous. Client harus menunggu sampai server memberikan respons. Dari percobaan tersebut terlihat bahwa RPC cocok digunakan untuk proses yang membutuhkan hasil secara langsung.



Consumer dijalankan pada laptop yang berbeda dengan RabbitMQ. Setelah koneksi berhasil, Consumer menggunakan queue `pembayaran_berhasil` untuk menerima pesan dari Publisher.

Kami melakukan uji dengan mematikan Consumer terlebih dahulu, kemudian menjalankan Publisher untuk mengirim 3 pesan. Pada RabbitMQ Dashboard terlihat `Ready = 3` dan `Unacked = 0`. Setelah Consumer dijalankan kembali, ketiga pesan berhasil diterima dan diproses.

Consumer menampilkan notifikasi pembayaran untuk user1, user2, dan user3. Setelah pesan diberikan `basic_ack`, jumlah pesan pada queue berubah menjadi `Ready = 0`.

## Kendala teknis

- Error saat setup (mis. koneksi RabbitMQ ditolak, port bentrok): ...

## Uji "pesan tidak hilang" (khusus Jalur B)

- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati:
- **Consumer:** Setelah Consumer dijalankan kembali, ketiga pesan yang sebelumnya tersimpan di RabbitMQ berhasil diterima dan diproses. Setelah `basic_ack`, queue menunjukkan `Ready = 0`.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
