def hitung_kelulusan(nama, nilai_list):
    rata_rata = sum(nilai_list) / len(nilai_list)
    status = "Lulus" if rata_rata >= 75 else "Perlu Remedial"
    
    print(f"Nama      : {nama}")
    print(f"Rata-rata : {rata_rata:.2f}")
    print(f"Status    : {status}")

# Contoh penggunaan
nilai_budi = [80, 75, 85, 70]
hitung_kelulusan("Budi", nilai_budi)