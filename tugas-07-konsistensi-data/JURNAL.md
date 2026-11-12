# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi(Yohana Sinaga)

- ### Argumen yang dipertimbangkan: ...

  * Eventual Consistency memperbolehkan replika berbeda untuk sementara waktu sampai seluruh pembaruan selesai direplikasi. Model ini dapat membantu menghindari sinkronisasi global yang mahal dan sesuai untuk data yang toleran terhadap keterlambatan, seperti jumlah  *like* .
  * Saldo e-wallet merupakan data keuangan. Perbedaan saldo dapat menyebabkan transaksi yang sah ditolak atau, jika saldo lama yang lebih tinggi digunakan untuk debit, berisiko menyebabkan pengeluaran melebihi saldo sebenarnya.
  * Sequential Consistency menjamin operasi seluruh proses dapat dipandang berlangsung dalam satu urutan sekuensial yang sama, dengan tetap mempertahankan urutan operasi setiap proses. Namun, koordinasi yang lebih kuat dapat menambah biaya komunikasi dan memengaruhi skalabilitas.
  * Read-Your-Writes merupakan jaminan Client-Centric Consistency: setelah pelanggan melakukan top-up, pembacaan berikutnya oleh pelanggan yang sama harus melihat efek top-up tersebut. Versi operasi dapat digunakan untuk memeriksa apakah replika tujuan sudah cukup baru.
  * Read-Your-Writes tidak sendirian menyelesaikan konflik debit yang terjadi bersamaan. Validasi dan pengurangan saldo untuk transaksi harus tetap dilakukan secara atomik pada sumber data yang berwenang.
- ### Kesimpulan akhir & alasan: ...

  * Eventual Consistency saja tidak cukup untuk pembacaan saldo setelah top-up karena replika Bandung dapat mengembalikan saldo lama.
  * Solusi yang dipilih adalah Eventual Consistency untuk replikasi umum dengan tambahan Read-Your-Writes pada sesi pelanggan. Setiap top-up diberi versi; jika versi replika tujuan lebih rendah daripada versi minimum milik client, pembacaan dialihkan ke server Jakarta yang sudah memiliki pembaruan.
  * Pendekatan ini menyelesaikan masalah stale read pada skenario tugas tanpa mengharuskan semua pembacaan selalu menunggu seluruh replika selesai sinkronisasi.

## Simulasi (jika dikerjakan)

- ### Hasil skenario naif vs Read-Your-Writes: ...

  * Skenario naif: saldo awal `user1` adalah Rp0. Setelah top-up Rp50.000 di Jakarta, pembacaan segera dari Bandung (sebelum delay replikasi selesai) masih menghasilkan Rp0. Ini menunjukkan  *inconsistent read* .
  * Setelah proses replikasi selesai, Bandung menerima saldo Rp50.000 versi 1.
  * Skenario Read-Your-Writes: pelanggan melakukan top-up Rp20.000 berikutnya sehingga saldo di Jakarta menjadi Rp70.000 versi 2. Ketika client membaca melalui Bandung dengan `versi_minimal = 2`, Bandung mendeteksi versi lokalnya belum mencukupi dan mengalihkan pembacaan ke Jakarta. Hasil yang diterima adalah Rp70.000 versi 2, bukan saldo lama.
  * Dengan demikian, simulasi menunjukkan bahwa Read-Your-Writes mencegah pelanggan membaca saldo yang lebih lama daripada hasil top-up terakhirnya.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
