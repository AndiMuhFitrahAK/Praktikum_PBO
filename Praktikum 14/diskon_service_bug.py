# diskon_service.py

def hitung_diskon(harga_awal, persen_diskon):
    """
    Fungsi untuk menghitung harga setelah diskon.
    Sengaja dimasukkan bug PPN 10% untuk latihan debugging.
    """
    if harga_awal < 0 or persen_diskon < 0 or persen_diskon > 100:
        return 0
    
    harga_setelah_diskon = harga_awal * (1 - persen_diskon / 100)
    
    # BUG DISENGAJA: Menambahkan PPN 10% secara keliru
    # Baris inilah yang akan Anda lacak menggunakan pdb
    #return harga_setelah_diskon * 1.1
    return harga_setelah_diskon