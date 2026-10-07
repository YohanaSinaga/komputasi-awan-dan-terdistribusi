"""
Tugas 4 - Jalur A: RPC Client (simulasi modul Pesanan)
Jalankan server.py di terminal lain terlebih dahulu.
"""

import xmlrpc.client
import time


def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

    print("Memanggil cek_saldo('user1') ... menunggu respons sinkron")

    start = time.time()

    saldo = proxy.cek_saldo("user1")

    waktu_tempuh = time.time() - start

    print(f"Saldo user1: Rp{saldo}")
    print(f"Waktu respons: {waktu_tempuh:.4f} detik")

    print("Memanggil proses_pembayaran('user1', 20000) ...")

    hasil = proxy.proses_pembayaran("user1", 20000)

    print(f"Hasil pembayaran: {hasil}")


if __name__ == "__main__":
    main()