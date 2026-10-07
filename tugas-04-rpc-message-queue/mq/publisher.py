"""
Tugas 4 - Jalur B: Publisher (simulasi modul Pembayaran)
"""

import pika
import json
import time

QUEUE_NAME = "pembayaran_berhasil"


def main():
    # TODO 1: koneksi ke RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="10.219.3.196")
    )
    channel = connection.channel()

    # TODO 2: deklarasikan queue
    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True
    )

    # Mengirim 3 event pembayaran
    for i in range(1, 4):
        pesan = {
            "user_id": f"user{i}",
            "jumlah": 20000 * i,
            "timestamp": time.time(),
        }

        # TODO 3: publish pesan ke RabbitMQ
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=json.dumps(pesan)
        )

        print(f"Event terkirim: {pesan}")
        time.sleep(1)

    # TODO 4: tutup koneksi
    connection.close()

    print("Publisher selesai mengirim event.")


if __name__ == "__main__":
    main()