import unittest
from diskon_service_bug import hitung_diskon

class TestDebugBug(unittest.TestCase):
    def test_perhitungan_salah(self):
        # Harga 1000 diskon 10% harusnya 900.0
        # Karena bug PPN 10% (* 1.1), hasilnya jadi 990.0 dan test ini akan GAGAL
        self.assertEqual(hitung_diskon(1000, 10), 900.0)

if __name__ == "__main__":
    unittest.main()