
# Jurnal Proses — Tugas 6

## Implementasi find_successor(Yohana Sinaga)

- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Kode dan output akhir yang tersedia tidak mencatat kesalahan pertama yang benar-benar dialami. Namun, kasus penting yang perlu diperhatikan dalam implementasi Chord adalah  *wrap-around* , yaitu ketika tidak ditemukan node dengan ID lebih besar atau sama dengan hash key, pencarian harus kembali ke node dengan ID terkecil.
- Cara memperbaikinya: Fungsi `<span>find_successor()</span>` mengurutkan ID node, kemudian mencari node pertama yang memenuhi kondisi `<span>node_id >= key_hash</span>`. Jika tidak ada node yang memenuhi kondisi tersebut, fungsi mengembalikan `<span>node_ids[0]</span>` sebagai successor melalui  *wrap-around* . Dengan demikian, pencarian tetap dapat dilakukan ketika hash key lebih besar daripada ID node terbesar.

## Skenario join/leave (yohanna p  dan laura)

- Hasil sebelum & sesudah node baru bergabung: sebelum node baru bergabung, ring memiliki node dengan ID 40, 102, 136, dan 177. Kurir `<span>kurir-uji-23</span>` memiliki hash 119 dan IP `<span>192.168.1.23</span>`, sehingga successor-nya adalah node 136. Setelah `<span>node-medan-1</span>` dengan ID 123 dan IP `<span>10.0.0.5</span>` bergabung, successor untuk hash 119 berubah menjadi node 123 karena node tersebut merupakan node pertama dengan ID yang lebih besar atau sama dengan 119. Output program menunjukkan bahwa mapping `<span>kurir-uji-23</span>` berpindah tanggung jawab dari node 136 ke node 123, sedangkan IP kurir tetap `<span>192.168.1.23</span>`.

--- Node baru bergabung ---
Node 'node-medan-1' (id=123) bergabung, alamat 10.0.0.5
  Mapping kurir-uji-23 (192.168.1.23) berpindah ke node 123
kurir-uji-23 -> 192.168.1.23 

- Hasil sebelum & sesudah node keluar: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
