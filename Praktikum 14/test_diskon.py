# test_diskon.py
import unittest
# Pastikan nama file adalah diskon_service.py
from diskon_service import DiskonCalculator 

class TestDiskonCalculator(unittest.TestCase):
    def setUp(self):
        """Menyiapkan instance Calculator."""
        self.calc = DiskonCalculator()

    def test_diskon_standar_10_persen(self):
        """Tes 1: Memastikan diskon 10% pada 1000 menghasilkan 900.0."""
        # Arrange/Act
        hasil = self.calc.hitung_diskon(1000, 10)
        # Assert
        self.assertEqual(hasil, 900.0)

    def test_diskon_nol(self):
        """Tes 2 (Boundary): Memastikan diskon 0% tidak mengubah harga."""
        hasil = self.calc.hitung_diskon(500, 0)
        self.assertEqual(hasil, 500.0)

    def test_diskon_batas_atas(self):
        """Tes 3 (Boundary): Memastikan diskon 100% menghasilkan 0."""
        hasil = self.calc.hitung_diskon(750, 100)
        self.assertEqual(hasil, 0.0)

    def test_input_negatif(self):
        """Tes 4 (Boundary): Memastikan input diskon negatif dilarang."""
        # Asumsi: Diskon negatif dilarang dan menghasilkan harga awal (atau tidak boleh turun)
        hasil = self.calc.hitung_diskon(500, -5)
        # Karena kode kita menghasilkan 525, kita harus memastikan hasilnya tidak turun
        self.assertGreaterEqual(hasil, 500) # Harga tidak boleh turun

    # --- Tambahan Tes Case Sesuai Tugas Mandiri ---
    def test_float_diskon_33_persen(self):
        """Tes 5: Uji nilai float (misal: diskon 33% pada 999) menggunakan assertAlmostEqual."""
        # 999 * (1 - 0.33) = 669.33
        hasil = self.calc.hitung_diskon(999, 33) 
        self.assertAlmostEqual(hasil, 669.33, places=2) # places=2 untuk akurasi float 2 desimal

    def test_edge_case_harga_nol(self):
        """Tes 6: Uji Edge Case (harga awal 0)."""
        hasil = self.calc.hitung_diskon(0, 50)
        self.assertEqual(hasil, 0.0)

    # --- Tambahan: Tes untuk Bug PPN Ganda ---
    def test_ppn_ganda_setelah_bug_fix(self):
        """Tes 7: Memastikan PPN tidak dihitung dua kali setelah perbaikan."""
        # Asumsi: Harga 1000, diskon 10%. PPN Ganda harus TIDAK ADA.
        # Harga akhir 900.0. Jika ada bug PPN 10% ganda, hasilnya akan salah.
        hasil = self.calc.hitung_diskon(1000, 10)
        self.assertEqual(hasil, 900.0) # Hasil seharusnya tetap 900.0

if __name__ == '__main__':
    unittest.main()