Fitur yang ada adalah
1. Menambah, mengedit, dan menghapus tugas
2. menandai tugas sebagai selesai atau belum selesai
3. menyimpan data secara lokal agar tidak hilang saat halaman ditutup
4. filter dan pencarian tugas berdasarkan status, mata kuliah, atau nama
5. menampilkan jumlah total tugas, tugas selesai, dan belum selesai
6. validasi form memastikan nama tugas, mata kuliah dan deadline diisi dengan benar
   
Screenshot fitur yang ada dalam aplikasi manajemen tugas mahasiswa
1. <img width="1343" height="918" alt="Screenshot 2025-10-18 022601" src="https://github.com/user-attachments/assets/b6a21130-f244-49e0-bb61-b6fe4cae9008" />
2. <img width="1257" height="902" alt="Screenshot 2025-10-18 022819" src="https://github.com/user-attachments/assets/833c806e-70e8-4c6c-b32f-e266bf3020b5" />
3. <img width="1198" height="858" alt="Screenshot 2025-10-18 022931" src="https://github.com/user-attachments/assets/4052b899-7489-44d7-9aaa-6ed804f9d8cd" />
4. <img width="1277" height="899" alt="Screenshot 2025-10-18 023006" src="https://github.com/user-attachments/assets/8c5c27ca-f8fe-4e12-801e-f4c09ad01f23" />






Cara menjalankan aplikasi
1. Buka folder proyek yang berisi file Index.html
2. Klik dua kali file tersebut atau dengan membuka browser dengan klik kanan pada file kemudian pilih open with kemudian pilih browser
3. Aplikasi akan langsung berjalan di browser
4. kemudian gunakan fitur tambah tugas, klik tombol selesai/belum, edit, atau hapus sesuai kebutuhan, kemudian gunakan filter dan kolom pencarian untuk menampilkan tugas tertentu
5. Semua data akan tersimpan

Daftar Fitur yang Diimplementasikan
1. Tambah Tugas
2. Edit Tugas
3. Hapus
4. Simpan
5. Tandai Selesai
6. Update Tugas
7. Pencarian Tugas
8. Statistik Tugas
9. Validasi Form
10. Penyimpanan lokal

Aplikasi manajemen tugas mahasiswa menggunakan localStorage untuk menyimpan seluruh data tugas secara permanen di browser. Setiap kali pengguna menambah, mengedit atau menghapus data, data tersebut disimpan dalam bentuk array dan dikonversi menjadi format JSON sebelum disimpan ke localStorage. Sat halaman dibuka kembali, aplikasi otomatis memuat ata dari localStorage agar pengguna tidak kehilangan data meskipun halaman direfresh untuk memastikan data yang dimasukkan sudah benar. Validasi ini memastikan bahwa nama tugas, mata kuliah, dan deadline tidak boleh kosong sebelum tugas disimpan. Jika ada input yang tidak valid, sistem akan menampilkan pesan kesalahan dan memberi tanda pada kolom yang bermasalah sehingga pengguna dapat memperbaikinya terlebih dahulu sebelum melanjutkannya.
