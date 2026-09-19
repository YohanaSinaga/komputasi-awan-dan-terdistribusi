
# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## 19 september 2026

- Peserta: Yohanna Purnomo, Yohana Sinaga, Laura Chyndearni
- Poin diskusi: Membahas tiga pitfall pada skenario FoodGo, yaitu The network is reliable, Latency is zero, dan Single Point of Failure/skalabilitas.
- Perbedaan pendapat (jika ada): Tidak ada perbedaan pendapat yang signifikan. Kelompok kami berdiskusi untuk memastikan pembagian pitfall dan pembahasannya tidak tumpang tindih.

## [Tanggal diskusi 2]

- ...

## Review Silang

- Yohanna Purnomo mengomentari analisis Yohana Sinaga: bahwa bagian Latency is zero perlu dibedakan dari masalah The network is reliable. Fokusnya harus pada waktu respons dan kondisi modul Order yang menunggu Payment tanpa batas waktu, bukan pada kegagalan jaringan.
- Yohana Sinaga mengomentari analisis Yohanna Purnomo bahwa bukti dari skenario harus tetap menggunakan bagian network is always reliable, no need for retry supaya hubungan antara pitfall dan skenario terlihat jelas.
- Laura mengomentari analisis Yohanna dan Yohana kalau dampak dari kedua masalah tersebut juga dapat semakin parah karena semua modul masih bisa berjalan pada satu server. Jadi, masalah komunikasi antarservice dan masalah beban server bisa saling memperburuk kondisi FoodGo-nya.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal           | Tool AI | Prompt yang diberikan                                                                                                                                                                                                                          | Ringkasan saran/ide AI                                                                                                                                                                                                                                                                              | Bagaimana diolah jadi tulisan/kode sendiri                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 19 september 2026 | GPT     | Kami sedang mengerjakan Tugas sistem terdistribusi tentang studi kasus FoodGo. Bantu kami memahami dan menyusun ide untuk mengidentifikasi pitfall yang sesuai. Setelah itu, bantu untuk menyusun gambaran untuk bisa kami kembangkan sendiri. | AI membantu mengarahkan tiga masalah utama FoodGo menjadi The network is reliable, Latency is zero, dan Single Point of Failure/skalabilitas. AI juga memberikan struktur pembahasan berupa bukti dari skenario, alasan asumsi tersebut keliru, dampak terhadap sistem, solusi awal, dan trade-off. | Kelompok menyesuaikan kembali ide dari AI dengan isi skenario FoodGo dan membagi pembahasan sesuai kontribusi masing-masing anggota. Setiap pitfall diperiksa agar memiliki bukti yang benar-benar berasal dari skenario dan tidak saling tumpang tindih. Solusi dan trade-off kemudian didiskusikan kembali oleh anggota kelompok, lalu ditulis ulang menggunakan bahasa kelompok sendiri. |
