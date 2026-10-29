
"""
Tugas 6 - Simulasi Chord DHT
Pemetaan ID kurir ke alamat IP menggunakan consistent hashing.
"""

import hashlib

M_BITS = 8
RING_SIZE = 2 ** M_BITS


def hash_id(key: str) -> int:
    """Mengubah string menjadi hash dalam rentang 0-255."""
    digest = hashlib.sha1(key.encode()).digest()
    return int.from_bytes(digest, "big") % RING_SIZE


class ChordRing:
    def __init__(self):
        self.nodes: dict[int, str] = {}
        self.data: dict[int, tuple[str, str]] = {}

    def find_successor(self, key_hash: int) -> int:
        """Mencari node pertama dengan ID >= hash key."""
        if not self.nodes:
            raise ValueError("Ring belum memiliki node.")

        node_ids = sorted(self.nodes.keys())

        for node_id in node_ids:
            if node_id >= key_hash:
                return node_id

        return node_ids[0]

    def join(self, node_name: str, node_ip: str):
        node_id = hash_id(node_name)

        if node_id in self.nodes:
            print(f"Node '{node_name}' sudah ada.")
            return

        old_owners = {}
        for key_hash in self.data:
            if self.nodes:
                old_owners[key_hash] = self.find_successor(key_hash)

        self.nodes[node_id] = node_ip
        print(
            f"Node '{node_name}' (id={node_id}) "
            f"bergabung, alamat {node_ip}"
        )

        for key_hash, (kurir_id, ip_kurir) in self.data.items():
            new_owner = self.find_successor(key_hash)
            if old_owners.get(key_hash) != new_owner:
                print(
                    f"  Mapping {kurir_id} ({ip_kurir}) "
                    f"berpindah ke node {new_owner}"
                )

    def leave(self, node_name: str):
        node_id = hash_id(node_name)

        if node_id not in self.nodes:
            print(f"Node '{node_name}' tidak ditemukan.")
            return

        affected = []
        for key_hash, (kurir_id, ip_kurir) in self.data.items():
            if self.find_successor(key_hash) == node_id:
                affected.append((kurir_id, ip_kurir, key_hash))

        del self.nodes[node_id]
        print(f"Node '{node_name}' (id={node_id}) keluar dari ring")

        if not self.nodes:
            print("Ring kosong; tidak ada node untuk mengambil alih.")
            return

        for kurir_id, ip_kurir, key_hash in affected:
            new_owner = self.find_successor(key_hash)
            print(
                f"  Mapping {kurir_id} ({ip_kurir}) "
                f"berpindah ke node {new_owner}"
            )

    def register_kurir(self, kurir_id: str, ip_kurir: str):
        key_hash = hash_id(kurir_id)
        owner = self.find_successor(key_hash)
        self.data[key_hash] = (kurir_id, ip_kurir)

        print(
            f"Kurir '{kurir_id}' terdaftar: IP {ip_kurir}, "
            f"hash {key_hash}, penanggung jawab node {owner}"
        )

    def lookup(self, kurir_id: str) -> str | None:
        key_hash = hash_id(kurir_id)
        self.find_successor(key_hash)

        data = self.data.get(key_hash)
        if data is None or data[0] != kurir_id:
            return None

        return data[1]


def main():
    ring = ChordRing()

    print("--- Node bergabung ---")
    ring.join("node-jakarta-1", "10.0.0.1")
    ring.join("node-jakarta-2", "10.0.0.2")
    ring.join("node-bandung-1", "10.0.0.3")
    ring.join("node-surabaya-1", "10.0.0.4")

    print("\n--- Registrasi kurir ---")
    ring.register_kurir("kurir-001", "192.168.1.10")
    ring.register_kurir("kurir-002", "192.168.1.11")
    ring.register_kurir("kurir-003", "192.168.1.12")
    ring.register_kurir("kurir-uji-23", "192.168.1.23")
    ring.register_kurir("kurir-leave-14", "192.168.1.14")

    print("\n--- Lookup sebelum perubahan topologi ---")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))

    print("\n--- Node baru bergabung ---")
    ring.join("node-medan-1", "10.0.0.5")
    print("kurir-uji-23 ->", ring.lookup("kurir-uji-23"))

    print("\n--- Sebuah node keluar ---")
    ring.leave("node-jakarta-1")
    print("kurir-leave-14 ->", ring.lookup("kurir-leave-14"))
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))


if __name__ == "__main__":
    main()