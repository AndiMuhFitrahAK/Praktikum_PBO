Unit test pada fungsi hitung_diskon di file diskon_service_bug.py mengalami kegagalan (Failure). Berdasarkan skenario pengetesan (1000, 10), hasil yang diharapkan adalah 900.0, namun sistem mengembalikan nilai 990.0.

**Langkah langkah debugging (pdb)**  
Saya menggunakan modul pdb (Python Debugger) untuk menghentikan eksekusi program dan memeriksa nilai variabel saat runtime:
- Menambahkan import pdb; pdb.set_trace() sebelum baris return pada fungsi hitung_diskon.

- Menjalankan file tes dan masuk ke mode interaktif (Pdb).

- Menggunakan perintah p harga_setelah_diskon untuk melihat nilai variabel sebelum dikembalikan.

- Hasil di terminal menunjukkan angka 900.0, yang berarti perhitungan diskon sebenarnya sudah benar.

**Temuan Akar Masalah (Root Cause)** 
Akar masalah ditemukan pada baris terakhir fungsi hitung_diskon. Melalui perintah p harga_setelah_diskon * 1.1 di debugger, terbukti bahwa ada penambahan PPN 10% secara tidak sengaja melalui perkalian * 1.1 pada baris return. Inilah yang menyebabkan hasil akhir menjadi 990.0 dan memicu kegagalan unit test.

Solusi Perbaikan Menghapus kode * 1.1 pada baris return sehingga fungsi hanya mengembalikan variabel harga_setelah_diskon secara murni.