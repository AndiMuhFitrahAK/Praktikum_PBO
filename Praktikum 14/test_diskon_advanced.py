import unittest
# Import dari file yang sudah diperbaiki nantinya
from diskon_service_bug import hitung_diskon 

class TestDiskonLanjut(unittest.TestCase):
    def test_float_discount(self):
        # Tes 5: Uji nilai float (diskon 33% pada 999)
        self.assertAlmostEqual(hitung_diskon(999, 33), 669.33, places=2)

    def test_zero_price(self):
        # Tes 6: Uji harga awal 0
        self.assertEqual(hitung_diskon(0, 50), 0)

if __name__ == '__main__':
    unittest.main()