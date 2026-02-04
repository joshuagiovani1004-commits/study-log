catatan = []
favorit = set()

def tambah_catatan():
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()
    while True:
        dur = input("Durasi belajar (menit): ").strip()
        try:
            durasi = int(dur)
            if durasi <= 0:
                print("Masukkan angka lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Masukkan durasi dalam angka (menit). Contoh: 30")

    entry = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi,
    }
    catatan.append(entry)
    print("Catatan tersimpan.")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan.")
        return

    print("\nDaftar catatan belajar:")
    no_w = 4
    fav_label = " (Favorit)"
    mapel_displays = [
        c['mapel'] + (fav_label if c['mapel'].lower() in favorit else "")
        for c in catatan
    ]
    mapel_w = max(len("Mapel"), max((len(s) for s in mapel_displays), default=0))
    topik_w = max(len("Topik"), max((len(c['topik']) for c in catatan), default=0))
    dur_header = "Durasi (menit)"
    dur_w = max(len(dur_header), max((len(f"{c['durasi']} menit") for c in catatan), default=0))

    header = f"{'No':<{no_w}} | {'Mapel':<{mapel_w}} | {'Topik':<{topik_w}} | {dur_header:>{dur_w}}"
    separator = "-" * len(header)
    print(header)
    print(separator)

    for i, c in enumerate(catatan, start=1):
        dur_str = f"{c['durasi']} menit"
        mapel_display = mapel_displays[i-1]
        print(f"{i:<{no_w}} | {mapel_display:<{mapel_w}} | {c['topik']:<{topik_w}} | {dur_str:>{dur_w}}")

def kelola_favorit():
    while True:
        print("\n-- Kelola Mapel Favorit --")
        print("1. Tambah mapel favorit")
        print("2. Hapus mapel favorit")
        print("3. Lihat mapel favorit")
        print("4. Kembali")
        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            m = input("Masukkan nama mapel yang ingin dijadikan favorit: ").strip()
            if not m:
                print("Nama mapel tidak boleh kosong.")
            elif m.lower() in favorit:
                print(f"{m} sudah ada di favorit.")
            else:
                favorit.add(m.lower())
                print(f"{m} ditambahkan ke favorit.")
        elif pilihan == "2":
            m = input("Masukkan nama mapel yang ingin dihapus dari favorit: ").strip()
            if m.lower() in favorit:
                favorit.remove(m.lower())
                print(f"{m} dihapus dari favorit.")
            else:
                print(f"{m} tidak ditemukan di favorit.")
        elif pilihan == "3":
            if not favorit:
                print("Belum ada mapel favorit.")
            else:
                print("Daftar mapel favorit:")
                for i, f in enumerate(sorted(favorit), start=1):
                    print(f"{i}. {f}")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

def total_waktu():
    total = sum(c.get('durasi', 0) for c in catatan)
    print(f"Total waktu belajar: {total} menit")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Kelola mapel favorit")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "5":
        kelola_favorit()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")