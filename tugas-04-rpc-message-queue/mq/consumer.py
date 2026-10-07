"""
Tugas 4 - Jalur B: Consumer (simulasi modul Kurir/Notifikasi)
Jalankan file ini SEBELUM publisher.py untuk uji normal, atau SESUDAHNYA
untuk membuktikan pesan tetap tersimpan di antrean (asynchronous decoupling).
"""

import pika
import json

QUEUE_NAME = "pembayaran_berhasil"


def callback(ch, method, properties, body):

    # Mengubah pesan JSON menjadi dictionary
    pesan = json.loads(body)

    # Memproses pesan
    print(
        f"Kurir menerima notifikasi pembayaran "
        f"untuk {pesan['user_id']} "
        f"sejumlah Rp{pesan['jumlah']}"
    )

    # Memberikan acknowledgement
    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )


def main():

    # Koneksi ke RabbitMQ di laptop teman
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="10.219.3.196"
        )
    )

    # Membuat channel
    channel = connection.channel()

    # Menggunakan queue yang sama dengan publisher
    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True
    )

    # Mendaftarkan callback
    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=callback
    )

    print(
        "Menunggu event dari antrean "
        "'pembayaran_berhasil'... (Ctrl+C untuk berhenti)"
    )

    # Menunggu pesan
    channel.start_consuming()


if __name__ == "__main__":
    main()