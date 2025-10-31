Aplikasi Manajemen Buku Pribadi
Aplikasi ini adalah web sederhana yang dibangun untuk membantu pengguna melacak koleksi buku pribadi. Pengguna dapat mencatat buku yang dimilikinya, sedang dibaca atau ingin dibeli dengan menggunakan React.
Aplikasi ini menggunakan local storage yaitu peramban untuk menyimpan data, sehingga daftar buku akan tetap ada bahkan setelah pengguna menutup tab atau me-refresh halaman.

<img width="1906" height="932" alt="image" src="https://github.com/user-attachments/assets/ca9be1a6-2421-4c00-bc48-1c3566a2069b" />
Gambar di atas merupakan tampilan aplikasi

Untuk menjalankannya di komputer lokal pengguna dengan mengikuti langkah-langkah berikut:
1. Clone repositori ini atau unduh dile ini dengan format .zip
2. Kemudian masuk ke direktori proyek dengan mengetik cd _nama directory proyek_
3. instal semua dependensi dengan mengetik npm install di terminal
4. Jalankan aplikasi dengan mengetik npm start di terminal
5. Kemudian buka http://localhost:3000 di peramban anda

Fitur yang digunakan adalah sebagai berikut:
1. Functional Components, seluruh aplikasi dibangun dengan menggunakan functional components dengan hooks
2. State Management, dengan menggu useState yang digunakan untuk mengelola state lokal pada komponen input sorm dan state editing, kemudian pada context API digunakan untuk global state management. BookContext.js bertindak sebagai singlesource of truth untuk daftar buku, filter, dan search term, menghindari prop drilling
3. Side Effects, digunakan dalam custom hook 'yseLocalStorage' untuk menyimpan state buku ke 'localStorage' setiap kali ada perubahan
4. Komponen Reusable, yaitu pada BookForm yaitu komponen untuk menambah dan mengedit buku, BookList yaitu komponen untuk menampilkan daftar buku yang sudah difilter, dan BookFilter merupakan komponen untuk UI pencarian dan filter status.
5. Routing, menggunakan react-router-dom untuk membuat aplikasi multi-halaman
6. Custom Hooks, menggunakan useLocalStorage.js yaitu hook kustom untuk abstraksi logika penyimpanan data ke localStorage dan useBookStats.js yaitu hook kustom yang menggunakan useMemo untuk menghitung statistika buku secara efisien
7. Error Handling yaitu validasi input sederhana di BookForm untuk mencegah pengiriman data kosong
8. Modular Structure yaitu struktur folder dipisahkan berdasarkan fungsi components, pages, hooks, context untuk memudahkan navigasi dan pemeliharaan

Komentar penjelasan telah ditambahkan di seluruh basis kode, terutama di bagian custom hooks (useLocalStorage.js), context API(BookContext.js) dan logika filtering di BookList.js untuk mempermudah pemahaman alur kerja.

Pada proye ini dilengkapi dengan 5 unit test menggunakan react testing library

untuk menjalankan tes yaitu dengan mengetik npm test di terminal.
<img width="1372" height="356" alt="image" src="https://github.com/user-attachments/assets/f27d9b2a-c3d4-44ec-ac96-416c07c36c7c" />


Fitur yang ada pada aplikasi
1. Menambahkan buku yang ingin dibaca, dibeli atau dimiliki
   <img width="1073" height="568" alt="image" src="https://github.com/user-attachments/assets/83c52a1f-f0fb-4122-86b3-7591efda30b2" />
2. Fitur untuk melihat daftar buku
   <img width="1090" height="924" alt="image" src="https://github.com/user-attachments/assets/dc2cc26e-8559-4b03-8e3f-28b07be2458f" />
3. Fitur melihat daftar buku yang sudah dimiliki
   <img width="1090" height="924" alt="image" src="https://github.com/user-attachments/assets/f59f9bdf-401e-45ed-b3d9-2ce126fbaae7" />
5. Fitur untuk melihat daftar buku yang sudah dibaca
   <img width="1099" height="877" alt="image" src="https://github.com/user-attachments/assets/e5a08f74-6fd1-4f34-aa37-06c5d0b8619d" />
7. Fitur untuk melihat daftar buku yang ingin dibeli
   <img width="1084" height="707" alt="image" src="https://github.com/user-attachments/assets/0d266610-6da8-4f80-8a62-0360f19c4118" />
9. Fitur pencarian buku
    <img width="1086" height="226" alt="image" src="https://github.com/user-attachments/assets/9fb454b2-7d21-4242-a486-e519d2a62d12" />
11. Fitur untuk melihat statistik buku
    <img width="1202" height="471" alt="image" src="https://github.com/user-attachments/assets/d6627cb5-2fe1-4851-8fa3-a468288397a5" />


