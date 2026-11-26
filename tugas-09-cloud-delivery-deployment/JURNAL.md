# Jurnal Proses — Tugas 9

## Diskusi deployment model (YOHANA SINAGA)

- Opsi yang dipertimbangkan dan kenapa akhirnya memilih salah satu: ...
- Opsi yang dipertimbangkan:

  - **Public Cloud:** Memiliki skalabilitas tinggi dan sumber daya dapat disediakan dengan cepat. Namun, infrastrukturnya dikelola oleh penyedia eksternal sehingga kurang sesuai dengan kebutuhan sistem yang mengharuskan data berada pada infrastruktur yang sepenuhnya dikendalikan negara.
  - **Private Cloud:** Infrastruktur digunakan secara eksklusif dan dapat dikendalikan oleh pemerintah. Model ini memberikan kontrol lebih besar terhadap server, jaringan, penyimpanan, serta keamanan data.
  - **Community Cloud:** Dapat digunakan bersama oleh beberapa instansi yang memiliki kepentingan yang sama. Namun, pengaturan tanggung jawab dan kontrol infrastruktur antarinstansi perlu diperhatikan.
  - **Hybrid Cloud:** Menggabungkan dua atau lebih model cloud sehingga lebih fleksibel. Namun, integrasi dan pertukaran data antarlingkungan cloud dapat menambah kompleksitas keamanan.
- **Keputusan:** Kelompok memilih **Private Cloud** sebagai deployment model utama.
- **Alasan pemilihan:** Sistem menyimpan data pribadi yang sangat sensitif, seperti NIK, alamat, dan data biometrik. Karena data harus berada pada infrastruktur yang sepenuhnya dikendalikan negara, Private Cloud menjadi pilihan yang paling sesuai.
- **Pertimbangan skalabilitas:** Private Cloud memiliki keterbatasan kapasitas dibandingkan Public Cloud. Untuk mengantisipasi lonjakan permintaan saat pemilu atau pendaftaran sekolah, pemerintah perlu menyiapkan kapasitas cadangan, menerapkan horizontal scaling, menggunakan load balancer, serta melakukan monitoring dan load testing.
- **Counter-scenario:** Jika jumlah permintaan meningkat hingga 10 kali lipat, Hybrid Cloud dapat dipertimbangkan untuk menangani beban kerja non-sensitif pada Public Cloud, sementara database utama dan data biometrik tetap berada di Private Cloud. Namun, opsi ini belum dipilih sebagai model utama karena menambah risiko pertukaran data, sinkronisasi, dan kompleksitas pengelolaan.

## Diskusi service model per komponen (Kholifa)

- Opsi yang dipertimbangkan:
  - **Public Cloud:** Memiliki skalabilitas tinggi dan sumber daya dapat disediakan dengan cepat. Namun, infrastrukturnya dikelola oleh penyedia eksternal sehingga kurang sesuai dengan kebutuhan sistem yang mengharuskan data berada pada infrastruktur yang sepenuhnya dikendalikan negara.
  - **Private Cloud:** Infrastruktur digunakan secara eksklusif dan dapat dikendalikan oleh pemerintah. Model ini memberikan kontrol lebih besar terhadap server, jaringan, penyimpanan, serta keamanan data.
  - **Community Cloud:** Dapat digunakan bersama oleh beberapa instansi yang memiliki kepentingan yang sama. Namun, pengaturan tanggung jawab dan kontrol infrastruktur antarinstansi perlu diperhatikan.
  - **Hybrid Cloud:** Menggabungkan dua atau lebih model cloud sehingga lebih fleksibel. Namun, integrasi dan pertukaran data antarlingkungan cloud dapat menambah kompleksitas keamanan.
- **Keputusan:** Kelompok memilih **Private Cloud** sebagai deployment model utama.
- **Alasan pemilihan:** Sistem menyimpan data pribadi yang sangat sensitif, seperti NIK, alamat, dan data biometrik. Karena data harus berada pada infrastruktur yang sepenuhnya dikendalikan negara, Private Cloud menjadi pilihan yang paling sesuai.
- **Pertimbangan skalabilitas:** Private Cloud memiliki keterbatasan kapasitas dibandingkan Public Cloud. Untuk mengantisipasi lonjakan permintaan saat pemilu atau pendaftaran sekolah, pemerintah perlu menyiapkan kapasitas cadangan, menerapkan horizontal scaling, menggunakan load balancer, serta melakukan monitoring dan load testing.
- **Counter-scenario:** Jika jumlah permintaan meningkat hingga 10 kali lipat, Hybrid Cloud dapat dipertimbangkan untuk menangani beban kerja non-sensitif pada Public Cloud, sementara database utama dan data biometrik tetap berada di Private Cloud. Namun, opsi ini belum dipilih sebagai model utama karena menambah risiko pertukaran data, sinkronisasi, dan kompleksitas pengelolaan.

## Diskusi service model per komponen

- **IaaS — Database utama kependudukan:** Dipilih karena pemerintah membutuhkan kontrol terhadap server, sistem operasi, jaringan, dan penyimpanan yang digunakan untuk menyimpan data kependudukan.
- **IaaS — Penyimpanan data biometrik:** Dipilih karena data biometrik membutuhkan pengamanan ketat dan kontrol penyimpanan yang lebih besar.
- **PaaS — API verifikasi NIK:** Dipilih agar pengembangan dan pengelolaan layanan API dapat lebih berfokus pada aplikasi tanpa harus mengelola seluruh infrastruktur dasar.
- **PaaS — Aplikasi administrasi kependudukan:** Digunakan untuk mendukung pengembangan dan pemeliharaan aplikasi yang digunakan oleh petugas sesuai kewenangannya.
- **PaaS — Layanan autentikasi dan otorisasi:** Digunakan untuk mendukung pengelolaan identitas pengguna, proses login, dan pembatasan hak akses antarinstansi.
- **SaaS — Email dan aplikasi kolaborasi:** Dapat digunakan untuk kebutuhan pendukung yang tidak menyimpan atau memproses data kependudukan sensitif. Penggunaan SaaS eksternal harus mengikuti kebijakan keamanan pemerintah.
- **Keputusan akhir:** Komponen inti yang mengolah data kependudukan menggunakan IaaS dan PaaS di lingkungan Private Cloud. SaaS hanya digunakan secara terbatas untuk kebutuhan nonrahasia. Data NIK, alamat, dan biometrik tidak ditempatkan pada SaaS eksternal yang infrastrukturnya tidak berada dalam kendali negara.

## Catatan hasil diskusi

- Risiko yang dibahas meliputi kebocoran data atau akses tidak sah, keterbatasan kapasitas saat terjadi lonjakan permintaan, dan gangguan pada pusat data.
- Mitigasi yang disepakati meliputi RBAC, MFA, enkripsi data, audit log, monitoring, horizontal scaling, load balancer, kapasitas cadangan, backup, replikasi, serta Disaster Recovery Plan.
- Alternatif Public Cloud ditolak sebagai deployment model utama karena tidak memenuhi kebutuhan kontrol infrastruktur negara pada studi kasus.
- Keputusan akhir kelompok adalah menggunakan Private Cloud dengan kombinasi IaaS dan PaaS untuk komponen inti serta SaaS secara terbatas untuk kebutuhan pendukung nonrahasia.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
