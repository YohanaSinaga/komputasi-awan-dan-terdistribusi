
# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## 19 september 2026

- Peserta: Yohanna Purnomo, Yohana Sinaga, Laura Chyndearni
- Poin diskusi: Membahas tiga pitfall pada skenario FoodGo, yaitu The network is reliable, Latency is zero, dan Single Point of Failure/skalabilitas.
- Perbedaan pendapat (jika ada): Tidak ada perbedaan pendapat yang signifikan. Kelompok kami berdiskusi untuk memastikan pembagian pitfall dan pembahasannya tidak tumpang tindih.

## 20 September 2026
- **Peserta:** Yohana Sinaga, Yohanna Purnomo, Laura Chyndearni Saragih
  
- **Poin diskusi:**
  - Kami membahas solusi yang cocok untuk masing-masing masalah.
  - Untuk masalah jaringan, kami membahas penggunaan retry dengan backoff agar request yang gagal karena gangguan sementara dapat dicoba kembali.
  - Untuk masalah tidak adanya timeout, kami membahas penggunaan timeout agar Order Service nya tidak menunggu Payment Service tanpa batas.
  - Kami juga membahas circuit breaker sebagai tambahan untuk mencegah request terus dikirim ke service yang sedang bermasalah.
  - Untuk masalah satu server, kami membahas pemisahan modul menjadi service/proses yg berbeda agar semua fungsi tidak bergantung pada satu server.
  - Kami membahas trade off dari setiap solusi supaya analisis tidak hanya berisi kelebihan solusi.

- **Perbedaan pendapat (jika ada):**

  - Kami sempat membahas apakah retry saja sudah cukup untuk mengatasi masalah jaringan. Setelah didiskusikan, kami menyimpulkan bahwa retry tetap perlu dibatasi dan menggunakan jeda karena terlalu banyak retry dapat menambah beban ketika service sedang bermasalah.
    
## Review Silang

**Yohana Sinaga mengomentari analisis Yohanna Purnomo**

- Yohana memberikan masukan bahwa bagian dampak sebaiknya menjelaskan apa yang terjadi ketika komunikasi antar-service mengalami gangguan, bukan hanya menyebut request gagal.
- Kami kemudian membahas bahwa kegagalan komunikasi pada saat trafik tinggi dapat mengganggu proses pemesanan atau pembayaran.
- Yohanna memperjelas bagian dampak dengan menjelaskan bahwa request yang gagal dapat mengganggu proses Order atau Payment, terutama ketika server juga sedang terbebani.

**Yohanna Purnomo mengomentari analisis Laura Chyndearni Saragih**

- Yohanna memberikan masukan bahwa bagian tentang satu server perlu menjelaskan dua masalah, yaitu scalability dan Single Point of Failure.
- Kami membahas bahwa ketika satu server menangani Order, Payment, dan Notification sekaligus, peningkatan trafik membuat semua modul menggunakan resource yang sama.
- Laura kemudian menambahkan bahwa jika server tersebut mengalami crash, beberapa modul yang berjalan di dalamnya juga dapat ikut berhenti.

  
**Laura Chyndearni Saragih mengomentari analisis Yohana Sinaga**

- Laura memberikan masukan bahwa dampak dari tidak adanya timeout perlu dijelaskan lebih detail, terutama mengenai request yang tertahan ketika Payment Service lambat memberikan respons.
- Kami kemudian membahas bahwa semakin banyak request yang menunggu, semakin banyak resource server yang digunakan.
- Yohana memperjelas bagian dampak dengan menjelaskan hubungan antara Payment Service yang lambat, request yang tertahan, penggunaan resource, dan aplikasi yang menjadi semakin lambat.

## Hasil Akhir Diskusi 

Setelah melakukan pembahasan dan review silang, kami menyepakati tiga masalah utama yang akan digunakan dalam analisis, yaitu **The Network is Reliable**, tidak adanya **timeout pada komunikasi antar-service**, serta **Single Point of Failure dan masalah scalability** akibat penggunaan satu server atau proses untuk beberapa modul. Kami kemudian menyusun solusi berdasarkan masalah masing-masing. Solusi yang dipilih adalah timeout, retry dengan backoff, circuit breaker, dan pemisahan modul secara bertahap. Kami juga menambahkan trade-off dari setiap solusi agar analisis tidak hanya menjelaskan keuntungan tetapi juga risiko atau kekurangannya.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal           | Tool AI | Prompt yang diberikan                                                                                                                                                                                                                          | Ringkasan saran/ide AI                                                                                                                                                                                                                                                                              | Bagaimana diolah jadi tulisan/kode sendiri                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 19 september 2026 | GPT     | Kami sedang mengerjakan Tugas sistem terdistribusi tentang studi kasus FoodGo. Bantu kami memahami dan menyusun ide untuk mengidentifikasi pitfall yang sesuai. Setelah itu, bantu untuk menyusun gambaran untuk bisa kami kembangkan sendiri. | AI membantu mengarahkan tiga masalah utama FoodGo menjadi The network is reliable, Latency is zero, dan Single Point of Failure/skalabilitas. AI juga memberikan struktur pembahasan berupa bukti dari skenario, alasan asumsi tersebut keliru, dampak terhadap sistem, solusi awal, dan trade-off. | Kelompok menyesuaikan kembali ide dari AI dengan isi skenario FoodGo dan membagi pembahasan sesuai kontribusi masing-masing anggota. Setiap pitfall diperiksa agar memiliki bukti yang benar-benar berasal dari skenario dan tidak saling tumpang tindih. Solusi dan trade-off kemudian didiskusikan kembali oleh anggota kelompok, lalu ditulis ulang menggunakan bahasa kelompok sendiri. |
