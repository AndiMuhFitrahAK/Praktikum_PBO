# diskon_service.py
import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""
    
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        
        # --- BUG LOGIKA DISINI (Persentase tidak dibagi 100) ---
        # BUG: Jika input diskon 10, maka dihitung sebagai 1000%
        jumlah_diskon = harga_awal * persentase_diskon / 100
        
        # --- KODE PERBAIKAN ---
        # jumlah_diskon = harga_awal * persentase_diskon / 100 
        
        harga_akhir = harga_awal - jumlah_diskon
        return harga_akhir

# --- UJI COBA (Ini adalah test case yang akan GAGAL) ---
if __name__ == '__main__':
    calc = DiskonCalculator()
    # Input: 1000 - 10%. Hasil yang diharapkan: 900.0
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil: {hasil}") 
    # Output: -9000.0 (salah)