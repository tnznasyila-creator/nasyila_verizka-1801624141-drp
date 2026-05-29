# SOAL 1 - Layout Catur

print("\n=== PAPAN CATUR ===\n")

print("♜  ♞  ♝  ♛  ♚  ♝  ♞  ♜")

for baris in range(8):
    for kolom in range(8):

        if (baris + kolom) % 2 == 0:
            print("⬜", end=" ")
        else:
            print("⬛", end=" ")

    print()

print("♜  ♞  ♝  ♛  ♚  ♝  ♞  ♜")

# SOAL 2 - Program Aktivitas

daftar_aktivitas = []

jumlah = int(input("\nBerapa aktivitas yang ingin dilakukan? "))

if jumlah == 0:
    print("\nTidak ada aktivitas yang dimasukkan")

else:

    for i in range(jumlah):

        print("\nAktivitas ke-", i + 1)

        aktivitas = input("Masukkan aktivitas: ")
        waktu = input("Masukkan waktu aktivitas: ")
        tempat = input("Masukkan tempat aktivitas: ")

        selesai = input("Apakah aktivitas sudah selesai? (Iya/Tidak): ")

        if selesai == "Iya":
            status = "✅ Selesai"
        else:
            status = "⏳ Belum selesai"

        prioritas = input("Prioritas aktivitas (Penting/Biasa): ")

        if prioritas == "Penting":
            prioritas = "⭐ Prioritas Tinggi"
        else:
            prioritas = "• Prioritas Biasa"

        data = {
            "aktivitas": aktivitas,
            "waktu": waktu,
            "tempat": tempat,
            "status": status,
            "prioritas": prioritas
        }

        daftar_aktivitas.append(data)

    print("\n==============================")
    print("     DAFTAR AKTIVITAS")
    print("==============================")

    for i, data in enumerate(daftar_aktivitas, start=1):

        print("\nAktivitas", i)
        print("Nama Aktivitas :", data["aktivitas"])
        print("Waktu          :", data["waktu"])
        print("Tempat         :", data["tempat"])
        print("Status         :", data["status"])
        print("Prioritas      :", data["prioritas"])

print("\n✨ Terus semangat menghadapi hari-harimu! ✨")