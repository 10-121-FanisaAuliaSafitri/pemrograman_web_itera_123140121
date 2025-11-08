data_mahasiswa = [{"nama": "Fanisa Aulia Safitri", "NIM": "123140121", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 90},
                  {"nama": "Indah", "NIM": "123140220", "nilai_uts": 80, "nilai_uas" : 85, "nilai_tugas": 90},
                  {"nama": "Budi", "NIM": "123456789", "nilai_uts": 60, "nilai_uas": 68, "nilai_tugas": 75},
                  {"nama": "Dinda", "NIM": "123987654", "nilai_uts": 95, "nilai_uas": 90, "nilai_tugas": 92},
                  {"nama": "Andi", "NIM": "129876543", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 60}]

def hitung_nilai_akhir(uts, uas, tugas):
    nilai_akhir = (0.30 * uts) + (0.40 * uas) + (0.30 * tugas)
    return round(nilai_akhir, 2)

def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 80:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

def tampilkan_data_tabel(data):
    if not data:
        print("\n--- Data kosong. Tidak ada data untuk ditampilkan. ---")
        return

    col_width = {
        "NIM": 10, "Nama": 20, "UTS": 5, "UAS": 5, "Tugas": 7, 
        "Nilai Akhir": 12, "Grade": 5
    }

    header = (
        f"{'NIM':<{col_width['NIM']}} | {'Nama':<{col_width['Nama']}} | "
        f"{'UTS':<{col_width['UTS']}} | {'UAS':<{col_width['UAS']}} | "
        f"{'Tugas':<{col_width['Tugas']}} | {'Nilai Akhir':<{col_width['Nilai Akhir']}} | "
        f"{'Grade':<{col_width['Grade']}}"
    )
    separator = "-" * len(header)

    print(f"\n{separator}")
    print(f"{header}")
    print(f"{separator}")

    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        
        row = (
            f"{mhs['NIM']:<{col_width['NIM']}} | {mhs['nama']:<{col_width['Nama']}} | "
            f"{mhs['nilai_uts']:<{col_width['UTS']}} | {mhs['nilai_uas']:<{col_width['UAS']}} | "
            f"{mhs['nilai_tugas']:<{col_width['Tugas']}} | {nilai_akhir:<{col_width['Nilai Akhir']}.2f} | "
            f"{grade:<{col_width['Grade']}}"
        )
        print(row)
    
    print(f"{separator}\n")

def cari_nilai_ekstrem(data, tipe='tertinggi'):
    if not data:
        return None

    data_dengan_nilai_akhir = []
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        mhs_baru = mhs.copy()
        mhs_baru['nilai_akhir'] = nilai_akhir
        data_dengan_nilai_akhir.append(mhs_baru)

    if tipe == 'tertinggi':
        hasil = max(data_dengan_nilai_akhir, key=lambda x: x['nilai_akhir'])
        print("\n*** Mahasiswa dengan Nilai Tertinggi ***")
    elif tipe == 'terendah':
        hasil = min(data_dengan_nilai_akhir, key=lambda x: x['nilai_akhir'])
        print("\n*** Mahasiswa dengan Nilai Terendah ***")
    else:
        return None
    
    print(f"Nama: {hasil['nama']} (NIM: {hasil['NIM']})")
    print(f"Nilai Akhir: {hasil['nilai_akhir']:.2f}")
    print(f"Grade: {tentukan_grade(hasil['nilai_akhir'])}\n")
    return hasil

def input_data_baru(data_list):
    print("\n--- Input Data Mahasiswa Baru ---")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")

    while True:
        try:
            uts = int(input("Masukkan Nilai UTS: "))
            uas = int(input("Masukkan Nilai UAS: "))
            tugas = int(input("Masukkan Nilai Tugas: "))
            if 0 <= uts <= 100 and 0 <= uas <= 100 and 0 <= tugas <= 100:
                break
            else:
                print("Nilai harus dalam rentang 0-100. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    mahasiswa_baru = {
        "nama": nama,
        "NIM": nim,
        "nilai_uts": uts,
        "nilai_uas": uas,
        "nilai_tugas": tugas
    }
    data_list.append(mahasiswa_baru)
    print("\n[SUCCESS] Data mahasiswa baru berhasil ditambahkan!")
    tampilkan_data_tabel([mahasiswa_baru])

def filter_mahasiswa_by_grade(data_list):
    grade_pilihan = input("\nMasukkan Grade yang ingin difilter (A/B/C/D/E): ").upper()
    if grade_pilihan not in ('A', 'B', 'C', 'D', 'E'):
        print("\nGrade tidak valid. Harap masukkan A, B, C, D, atau E.")
        return

    hasil_filter = []
    for mhs in data_list:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        if grade == grade_pilihan:
            hasil_filter.append(mhs)

    print(f"\n--- Hasil Filter Mahasiswa Grade '{grade_pilihan}' ---")
    tampilkan_data_tabel(hasil_filter)

def hitung_rata_rata_kelas(data_list):
    if not data_list:
        print("\nData kosong. Tidak dapat menghitung rata-rata.")
        return

    total_nilai_akhir = 0
    for mhs in data_list:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        total_nilai_akhir += nilai_akhir

    rata_rata = total_nilai_akhir / len(data_list)
    
    print("\n*** Rata-Rata Nilai Akhir Kelas ***")
    print(f"Total Mahasiswa: {len(data_list)}")
    print(f"Rata-Rata Nilai Akhir: {rata_rata:.2f}\n")
    return rata_rata
  
def tampilkan_menu():
    print("=" * 40)
    print("   PROGRAM PENGELOLAAN NILAI MAHASISWA")
    print("=" * 40)
    print("1. Tampilkan Semua Data Mahasiswa")
    print("2. Input Data Mahasiswa Baru")
    print("3. Cari Mahasiswa Nilai Tertinggi")
    print("4. Cari Mahasiswa Nilai Terendah")
    print("5. Filter Mahasiswa Berdasarkan Grade")
    print("6. Hitung Rata-Rata Nilai Kelas")
    print("7. Keluar")
    print("-" * 40)

def main():
    global data_mahasiswa
    
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-7): ")

        if pilihan == '1':
            tampilkan_data_tabel(data_mahasiswa)
        elif pilihan == '2':
            input_data_baru(data_mahasiswa)
        elif pilihan == '3':
            cari_nilai_ekstrem(data_mahasiswa, tipe='tertinggi')
        elif pilihan == '4':
            cari_nilai_ekstrem(data_mahasiswa, tipe='terendah')
        elif pilihan == '5':
            filter_mahasiswa_by_grade(data_mahasiswa)
        elif pilihan == '6':
            hitung_rata_rata_kelas(data_mahasiswa)
        elif pilihan == '7':
            print("\nTerima kasih telah menggunakan Program Pengelolaan Data Nilai Mahasiswa.")
            break
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka antara 1 sampai 7.")
            
        input("Tekan ENTER untuk kembali ke menu...")

if __name__ == "__main__":

    main()
