# Jurnal Proses — Tugas 6

## Implementasi find_successor(Yohana Sinaga)

- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Kode dan output akhir yang tersedia tidak mencatat kesalahan pertama yang benar-benar dialami. Namun, kasus penting yang perlu diperhatikan dalam implementasi Chord adalah  *wrap-around* , yaitu ketika tidak ditemukan node dengan ID lebih besar atau sama dengan hash key, pencarian harus kembali ke node dengan ID terkecil.
- Cara memperbaikinya: Fungsi `<span>find_successor()</span>` mengurutkan ID node, kemudian mencari node pertama yang memenuhi kondisi `<span>node_id >= key_hash</span>`. Jika tidak ada node yang memenuhi kondisi tersebut, fungsi mengembalikan `<span>node_ids[0]</span>` sebagai successor melalui  *wrap-around* . Dengan demikian, pencarian tetap dapat dilakukan ketika hash key lebih besar daripada ID node terbesar.

## Skenario join/leave

- Hasil sebelum & sesudah node baru bergabung: ...
- Hasil sebelum & sesudah node keluar: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
