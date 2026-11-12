# Tugas 7 (Pekan 7) — Konsistensi Data

**Materi terkait:** Data-Centric Consistency (Sequential, Eventual), Client-Centric Consistency.

## Studi Kasus

Data saldo *e-wallet* pelanggan FoodGo berbeda antara server wilayah **Jakarta** dan **Bandung** karena replikasi antar server berjalan lambat. Contoh kasus nyata: pelanggan top-up saldo lewat server Jakarta, lalu dalam hitungan detik memesan makanan lewat aplikasi yang tersambung ke server Bandung — saldo belum ter-update, transaksi ditolak padahal saldo sebenarnya cukup.

## Tugas Kelompok

### Bagian 1 — Analisis (wajib)

1. Tentukan: apakah kasus ini **membutuhkan Sequential Consistency** (semua replika melihat urutan operasi yang sama) atau **cukup Eventual Consistency** (replika akan konsisten "pada akhirnya", boleh sementara berbeda)? Berikan argumen berbasis dampak bisnis (mis. kasus saldo *e-wallet* jauh lebih sensitif dibanding kasus "jumlah like" di media sosial).
2. Jika kalian menyimpulkan Eventual Consistency saja **tidak cukup** untuk skenario ini, usulkan pendekatan **Client-Centric Consistency** yang relevan (mis. *Read-Your-Writes*: pelanggan yang baru top-up harus selalu melihat saldo terbarunya sendiri, walau replika lain belum sinkron).
3. Gambarkan **diagram alir urutan (sequence diagram)** yang menunjukkan operasi read/write antara pelanggan, server Jakarta, server Bandung, dan proses replikasi — untuk skenario **tanpa** jaminan konsistensi (bug terjadi) DAN skenario **dengan** solusi yang kalian usulkan (bug teratasi). Pakai Mermaid (`sequenceDiagram`) di `README.md` — lihat contoh cara pakai di Tugas 2.

JAWAB :

### 3. Sequence diagram (YOHANNA PURNOMO)

#### A. Tanpa jaminan Read-Your-Writes (bug terjadi)

```mermaid
sequenceDiagram
    autonumber
    actor P as Pelanggan
    participant J as Server Jakarta
    participant B as Server Bandung
    participant R as Proses Replikasi
    P->>J: Top-up Rp50.000
    J->>J: Perbarui saldo menjadi Rp50.000 (versi 1)
    J-->>P: Top-up berhasil
    Note over J,B: Replikasi belum selesai
    P->>B: Baca saldo untuk memesan makanan
    B-->>P: Saldo lama Rp0 (versi 0)
    Note over P,B: BUG: saldo terbaca 0, transaksi dapat ditolak
    R-->>B: Kirim pembaruan saldo Rp50.000 (versi 1)
    B->>B: Simpan saldo versi 1
```

## B. Dengan Read-Your-Writes (bug teratasi)



```mermaid
sequenceDiagram
    autonumber
    actor P as Pelanggan
    participant J as Server Jakarta
    participant B as Server Bandung
    participant R as Proses Replikasi
    P->>J: Top-up Rp50.000
    J->>J: Perbarui saldo menjadi Rp50.000 (versi 1)
    J-->>P: Berhasil, token versi 1
    Note over P: Client menyimpan versi_minimal = 1
    par Replikasi berjalan di latar belakang
        J->>R: Jadwalkan replikasi versi 1
        R-->>B: Kirim pembaruan setelah delay
        B->>B: Simpan saldo versi 1
    and Pelanggan langsung membaca saldo
        P->>B: Baca saldo (versi_minimal = 1)
        B->>B: Periksa versi lokal (versi 0)
        B-->>P: Redirect ke Jakarta karena versi lokal < 1
        P->>J: Baca saldo minimal versi 1
        J-->>P: Saldo Rp50.000 (versi 1)
    end
    Note over P,B: Pelanggan tidak menerima saldo lama
```

**Kesimpulan:** Replikasi tetap dapat berjalan secara eventual untuk menjaga kinerja, tetapi pembacaan saldo oleh pelanggan harus memenuhi Read-Your-Writes. Jika replika tujuan belum mencapai versi yang diminta, pembacaan diarahkan ke replika yang sudah memiliki versi tersebut.

### Bagian 2 — Simulasi (opsional, nilai tambah)

Skeleton `src/replica_simulation.py` mensimulasikan dua replika (Jakarta & Bandung) dengan delay replikasi buatan. Lengkapi TODO untuk:

1. Menunjukkan kondisi **inconsistent read** (replika Bandung masih menunjukkan saldo lama walau Jakarta sudah update).
2. Mengimplementasikan mekanisme **Read-Your-Writes** sederhana (mis. dengan version/timestamp per client) yang memperbaiki masalah tersebut.

```bash
python3 src/replica_simulation.py
```

## Struktur Submission

```
tugas-07-konsistensi-data/
├── README.md      # Analisis konsistensi + sequence diagram Mermaid
├── JURNAL.md
├── src/            # (opsional) simulasi replikasi
└── bukti/          # (jika mengerjakan simulasi) output program
```

## Rubrik Penilaian (Tugas 7)

| Komponen                              | Bobot | Kriteria                                                          |
| ------------------------------------- | ----- | ----------------------------------------------------------------- |
| Ketepatan pemilihan model konsistensi | 30%   | Argumen berbasis dampak bisnis nyata, bukan hafalan definisi      |
| Kualitas sequence diagram             | 30%   | Menunjukkan jelas titik kegagalan & titik perbaikan               |
| Usulan solusi client-centric          | 25%   | Solusi konkret dan dapat diimplementasikan (bukan wacana abstrak) |
| Proses & kontribusi kelompok          | 15%   | `JURNAL.md`, commit history (+ bonus jika simulasi dikerjakan)  |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya konsep umum consistency model ke AI untuk brainstorming; **tidak boleh** meminta AI menuliskan analisis akhir/sequence diagram atau isi `# TODO` di `src/replica_simulation.py` yang tinggal ditempel. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Sebagai bukti pemahaman konsep (bukan hafalan jawaban skenario FoodGo saja), `README.md` wajib menyertakan **satu skenario tambahan** yang kalian buat sendiri (mis. kasus lain di aplikasi ojek online) dan menentukan model konsistensi yang tepat untuk skenario tambahan tersebut.
