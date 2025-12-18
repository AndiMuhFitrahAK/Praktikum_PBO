Identifikasi Masalah: Sebelum Dilakukan Refacoring, Kode nya ada di dalam kelas MusicManager. Kelas ini kategorinya sebagai God Class karena punya banyak tanggung jawab. 
SRP: Kelas MusicManager menangani 2 tugas pemrosesan efek suara dan pengungghana ke platform publikasi. Harusnya 1 kelas hanya memiliki 1 alasan buat berubah. 
OCP: Penambahan efek baru (Reverb) atau Platform baru memaksa kita memodifikasi kode internal menggunakan blok if/else. Kode ini "tertutup" untuk ekstensi karena setiap perubahan membutuhkan modifikasi pada kode yang sudah stabil.
DIP: Modul tingkat tinggi bergantung pada teknis efek suara tertentu secara langsung, bukan lewat kontrak abstraksi.
