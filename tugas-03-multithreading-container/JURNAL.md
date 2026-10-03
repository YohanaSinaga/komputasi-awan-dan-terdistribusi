# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock

- Pada percobaan pertama, program dijalankan tanpa menggunakan `<span>threading.Lock()</span>`untuk membuat race condition lebih mudah terlihat, proses pembacaan dan perubahan`<span>processed_count</span>` dibuat terpisah:

```
current = processed_count
time.sleep(0.001)
processed_count = current + 1
```

### Hasil Percobaan

Program dijalankan sebanyak lima kali dan menghasilkan:

* Percobaan 1: 33 dari 100
* Percobaan 2: 37 dari 100
* Percobaan 3: 38 dari 100
* Percobaan 4: 34 dari 100
* Percobaan 5: 37 dari 100

Hasil tersebut tidak sesuai dengan jumlah pesanan yang seharusnya, yaitu 100.

### Analisis Race Condition

Race condition terjadi karena beberapa thread mengakses dan mengubah `<span>processed_count</span>` secara bersamaan.

Ketika satu thread membaca nilai `<span>processed_count</span>`, thread lain dapat membaca nilai yang sama sebelum perubahan pertama selesai. Akibatnya, beberapa proses penambahan dapat saling menimpa sehingga jumlah akhir menjadi lebih kecil dari 100.

Hasil yang berbeda-beda pada setiap percobaan terjadi karena urutan eksekusi thread tidak selalu sama.

Bukti percobaan disimpan pada:

```
bukti/race-condition-tanpa-lock.png
```


## Percobaan dengan Lock

- Hasil `processed_count` setelah perbaikan: ...

## Kendala Docker

- Kendala yang ditemui selama pengerjaan adalah Docker Desktop pada awalnya tidak dapat berjalan karena konfigurasi Windows Subsystem for Linux (WSL) belum aktif dengan benar. Setelah konfigurasi WSL diperbaiki dan Docker Desktop dapat berjalan, proses build image berhasil dilakukan. Selain itu, pada percobaan awal penggunaan Lock terdapat kesalahan indentasi sehingga bagian kode yang menggunakan Lock tidak berada di dalam fungsi process_order(). Setelah posisi kode diperbaiki, program dapat berjalan dengan benar dan menghasilkan nilai 100.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
