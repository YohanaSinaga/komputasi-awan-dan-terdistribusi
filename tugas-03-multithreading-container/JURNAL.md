# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock

- Hasil `processed_count` yang didapat: ...
- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): ...

## Percobaan dengan Lock

- Hasil `processed_count` setelah perbaikan: ...

## Kendala Docker

- Kendala yang ditemui selama pengerjaan adalah Docker Desktop pada awalnya tidak dapat berjalan karena konfigurasi Windows Subsystem for Linux (WSL) belum aktif dengan benar. Setelah konfigurasi WSL diperbaiki dan Docker Desktop dapat berjalan, proses build image berhasil dilakukan. Selain itu, pada percobaan awal penggunaan Lock terdapat kesalahan indentasi sehingga bagian kode yang menggunakan Lock tidak berada di dalam fungsi process_order(). Setelah posisi kode diperbaiki, program dapat berjalan dengan benar dan menghasilkan nilai 100.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| ------- | ------- | --------------------- | ---------------------- | ------------------------------------------ |
| ...     | ...     | ...                   | ...                    | ...                                        |
