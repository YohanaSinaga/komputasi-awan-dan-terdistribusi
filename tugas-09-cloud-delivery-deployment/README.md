# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:

- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.
2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).
3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).
4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

JAWAB :

### 1. Rekomendasi Deployment Model (YOHANNA PURNOMO)

#### 1.1 Perbandingan Deployment Model

| Model           | Karakteristik                                                                                                | Kesesuaian dengan Studi Kasus                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Public Cloud    | Infrastruktur disediakan oleh penyedia layanan eksternal dan digunakan bersama oleh berbagai organisasi.     | Kurang sesuai karena kontrol infrastruktur tidak sepenuhnya berada di tangan negara.                                           |
| Private Cloud   | Infrastruktur cloud digunakan secara eksklusif oleh satu organisasi dan dapat dikelola sesuai kebutuhannya.  | Sangat sesuai karena pemerintah dapat mengendalikan infrastruktur dan pengelolaan data.                                        |
| Community Cloud | Infrastruktur digunakan bersama oleh beberapa organisasi yang memiliki kepentingan atau kebutuhan yang sama. | Dapat digunakan untuk kolaborasi antarinstansi, tetapi pengaturan kepemilikan dan kontrol infrastrukturnya perlu diperhatikan. |
| Hybrid Cloud    | Menggabungkan dua atau lebih model cloud yang berbeda dan saling terhubung.                                  | Dapat memberikan fleksibilitas, tetapi meningkatkan kompleksitas integrasi dan pengamanan data.                                |

#### 1.2 Model yang Direkomendasikan: Private Cloud

Model deployment yang direkomendasikan adalah **Private Cloud**. Model ini dipilih karena sistem mengelola data kependudukan yang bersifat sangat rahasia dan harus berada pada infrastruktur yang sepenuhnya dikendalikan oleh negara.

Dengan Private Cloud, pemerintah dapat mengatur pengelolaan server, penyimpanan data, jaringan, keamanan, serta hak akses pengguna. Infrastruktur juga dapat dirancang sesuai kebutuhan sistem dan kebijakan keamanan pemerintah.

Kebutuhan skalabilitas dapat dipenuhi melalui penambahan sumber daya komputasi, seperti server dan kapasitas penyimpanan. Sistem juga dapat menggunakan horizontal scaling, yaitu menambahkan beberapa server dengan fungsi serupa untuk membagi beban permintaan.

Namun, skalabilitas Private Cloud tetap bergantung pada kapasitas infrastruktur yang disediakan pemerintah. Oleh karena itu, diperlukan perencanaan kapasitas, pemantauan penggunaan sumber daya, dan penyediaan kapasitas cadangan.

#### 1.3 Penerapan Lima Karakteristik Cloud Computing Menurut NIST

Berdasarkan NIST SP 800-145, cloud computing memiliki lima karakteristik utama yang dapat diterapkan pada Sistem Data Kependudukan.

**1. On-Demand Self-Service**

Administrator pemerintah dapat menyediakan atau menambah sumber daya komputasi sesuai kebutuhan tanpa harus selalu melakukan permintaan manual kepada penyedia layanan.

Contohnya, ketika terjadi peningkatan permintaan saat pemilu atau pendaftaran sekolah, administrator dapat menambah kapasitas server dan penyimpanan sesuai kebutuhan.

**2. Broad Network Access**

Layanan dapat diakses melalui jaringan oleh berbagai perangkat dan lokasi selama pengguna memiliki hak akses yang sesuai.

Contohnya, petugas Dukcapil, kepolisian, dan perbankan dapat mengakses layanan verifikasi NIK melalui API yang disediakan pemerintah. Setiap instansi memiliki hak akses sesuai kewenangannya.

**3. Resource Pooling**

Sumber daya komputasi dapat dikumpulkan dalam satu kumpulan sumber daya untuk melayani berbagai kebutuhan sistem.

Contohnya, sumber daya server dapat digunakan bersama untuk layanan verifikasi NIK, pengelolaan data biometrik, dan aplikasi administrasi kependudukan. Penggunaan sumber daya tetap diatur berdasarkan kebutuhan dan kebijakan keamanan.

**4. Rapid Elasticity**

Kapasitas sumber daya dapat ditambah atau dikurangi sesuai perubahan kebutuhan sistem.

Contohnya, ketika jumlah permintaan meningkat saat musim pemilu, pemerintah dapat menambahkan server untuk membagi beban akses. Setelah permintaan menurun, kapasitas tambahan dapat dikurangi.

Pada Private Cloud, elastisitas tetap dibatasi oleh kapasitas infrastruktur yang tersedia. Oleh karena itu, pemerintah perlu menyiapkan kapasitas cadangan dan melakukan perencanaan sejak awal.

**5. Measured Service**

Penggunaan sumber daya cloud dapat dipantau dan diukur secara otomatis.

Contohnya, pemerintah dapat memantau penggunaan CPU, memori, kapasitas penyimpanan, bandwidth, dan jumlah permintaan API. Data pengukuran tersebut digunakan untuk mengetahui kondisi sistem, merencanakan penambahan kapasitas, serta mendeteksi penggunaan yang tidak normal.

Pengukuran ini tidak harus selalu berkaitan dengan pembayaran berdasarkan penggunaan, tetapi juga dapat digunakan untuk kebutuhan monitoring dan evaluasi.


### 2. Rekomendasi Service Model (YOHANNA PURNOMO)

Untuk Sistem Data Kependudukan, service model yang direkomendasikan adalah kombinasi IaaS, PaaS, dan SaaS sesuai fungsi masing-masing komponen.

#### 2.1 Infrastructure as a Service (IaaS)

IaaS digunakan untuk menyediakan infrastruktur dasar seperti server virtual, jaringan, dan penyimpanan data.

Penerapannya:

- Database utama yang menyimpan data kependudukan.
- Penyimpanan data biometrik.
- Server untuk menjalankan layanan inti sistem.

IaaS dipilih karena pemerintah membutuhkan kontrol yang lebih besar terhadap sistem operasi, penyimpanan, konfigurasi server, dan pengamanan infrastruktur.

#### 2.2 Platform as a Service (PaaS)

PaaS digunakan untuk menyediakan platform pengembangan dan pengoperasian aplikasi tanpa harus mengelola seluruh infrastruktur dasar secara langsung.

Penerapannya:

- API untuk verifikasi NIK.
- Aplikasi administrasi kependudukan.
- Layanan autentikasi dan otorisasi.
- Layanan integrasi antarinstansi.

Dengan PaaS, tim pengembang dapat lebih berfokus pada pengembangan aplikasi, sedangkan pengelolaan platform dan infrastruktur dasarnya ditangani oleh layanan PaaS.

#### 2.3 Software as a Service (SaaS)

SaaS menyediakan aplikasi yang dapat langsung digunakan oleh pengguna tanpa harus mengelola infrastruktur dan platform aplikasi.

Penerapannya dapat dibatasi untuk kebutuhan pendukung yang tidak menyimpan data kependudukan sensitif, seperti:

- Email internal.
- Aplikasi kolaborasi.
- Pengelolaan dokumen nonrahasia.

Penggunaan SaaS dari penyedia eksternal harus mengikuti kebijakan keamanan pemerintah. Data NIK, alamat, dan biometrik tidak boleh ditempatkan pada SaaS eksternal yang tidak berada dalam kendali negara.

#### 2.4 Pemetaan Service Model

| Komponen Sistem                 | Service Model | Alasan                                                                |
| ------------------------------- | ------------- | --------------------------------------------------------------------- |
| Database utama kependudukan     | IaaS          | Membutuhkan kontrol terhadap server, sistem operasi, dan penyimpanan. |
| Penyimpanan data biometrik      | IaaS          | Membutuhkan kontrol dan perlindungan data yang ketat.                 |
| API verifikasi NIK              | PaaS          | Mempermudah pengembangan dan pengelolaan layanan API.                 |
| Aplikasi administrasi           | PaaS          | Mempermudah pengembangan dan pemeliharaan aplikasi.                   |
| Autentikasi dan otorisasi       | PaaS          | Mendukung pengelolaan akses pengguna dan integrasi layanan.           |
| Email dan kolaborasi nonrahasia | SaaS          | Dapat langsung digunakan untuk kebutuhan pendukung.                   |

Seluruh komponen inti yang mengolah data kependudukan ditempatkan pada lingkungan Private Cloud yang dikendalikan pemerintah.

### 3. Risiko dan Mitigasi (YOHANA SINAGA)



### 4. Perbandingan dengan Alternatif yang Ditolak (LAURA CHYNDEARNI)





## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen                                    | Bobot | Kriteria                                                                                   |
| ------------------------------------------- | ----- | ------------------------------------------------------------------------------------------ |
| Ketepatan rekomendasi deployment model      | 30%   | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model         | 25%   | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal                                      |
| Analisis risiko & mitigasi                  | 25%   | Risiko spesifik ke konteks data kependudukan (bukan risiko generik)                        |
| Perbandingan dengan alternatif yang ditolak | 20%   | Argumen penolakan jelas dan berdasar                                                       |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.
