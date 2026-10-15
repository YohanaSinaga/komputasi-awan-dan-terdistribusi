# Jurnal Proses — Tugas 5

## Implementasi Bully

Pada tugas kelompok ini, kami melengkapi bagian `<span>TODO</span>` pada file `<span>src/node.py</span>` untuk menjalankan simulasi Bully Algorithm dengan lima node yang berjalan sebagai proses Python terpisah. Setiap node menggunakan port yang berbeda dan berkomunikasi melalui TCP socket pada `<span>localhost</span>`.

Bagian yang dilengkapi meliputi:

* `<strong><span>on_message()</span></strong>`: menangani pesan `<span>ELECTION</span>`, `<span>OK</span>`, `<span>COORDINATOR</span>`, dan `<span>PING</span>`.
* `<strong><span>start_election()</span></strong>`: mengirim pesan election ke node dengan ID lebih tinggi.
* `<strong><span>declare_leader()</span></strong>`: menetapkan leader dan mengirim pesan `<span>COORDINATOR</span>` ke semua node lain.
* `<strong><span>monitor_leader()</span></strong>`: memeriksa apakah leader masih merespons dan memulai election kembali jika leader tidak merespons.

**Kendala saat mengisi TODO 1-4:**

Pada pengujian awal, beberapa node sempat menyatakan dirinya sebagai leader karena node dengan ID lebih tinggi belum aktif atau belum merespons. Setelah Node 5 aktif, node-node lain menerima pesan `<span>COORDINATOR</span>` dan memperbarui informasi leader mereka.

Kami juga mengalami kendala ketika menjalankan program karena perintah terminal tidak sesuai dengan lokasi file `<span>node.py</span>`. Kendala tersebut diatasi dengan menyesuaikan perintah berdasarkan folder kerja terminal.

## Skenario 1: Start normal

- Leader yang terpilih: Node 5
- Log/observasi: Setelah kelima node dijalankan, beberapa node sempat menyatakan dirinya sebagai leader ketika node dengan ID lebih tinggi belum merespons. Setelah Node 5 aktif dan proses pemilihan berlangsung, node-node lain menerima pesan COORDINATOR dari Node 5 dan mencatat Node 5 sebagai leader. Hasil akhir sesuai dengan aturan Bully Algorithm karena Node 5 memiliki ID tertinggi.

## Skenario 2: Leader dimatikan

- Leader baru yang terpilih: Node 4.
- Berapa lama waktu sampai leader baru terdeteksi: Sekitar 3 detik.
- Log/observasi: Ketika Node 5 sebagai leader dimatikan, node lain mendeteksi kegagalan leader dan memulai proses pemilihan leader baru. Berdasarkan pengamatan melalui terminal, dibutuhkan waktu sekitar 3 detik hingga Node 4 terpilih sebagai leader baru dan node lain menerima pesan COORDINATOR dari Node 4. Hasil pengujian menunjukkan bahwa Bully Algorithm dapat memilih leader baru ketika leader sebelumnya tidak lagi aktif.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
