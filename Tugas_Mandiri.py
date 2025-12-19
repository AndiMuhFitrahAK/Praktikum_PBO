import logging

# Konfigurasi dasar: Mencatat Waktu - Level - Nama Logger - Pesan [cite: 38]
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

# Membuat logger khusus untuk sistem produksi musik kita [cite: 38]
LOGGER = logging.getLogger('MusicStudio')

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Song:
    """Wadah untuk menyimpan data lagu yang mau kita proses.
    
    Args:
        title (str): Judul lagunya.
        artist (str): Nama penyanyi atau band.
        raw_data (str): Simulasi data audionya ini.
        is_processed (bool): Penanda apa lagu ini sudah di proses.
    """
    title: str
    artist: str
    raw_data: str
    is_processed: bool = False

# --- REFACTORING: ABSTRAKSI (Kontrak DIP/OCP) ---
class IAudioEffect(ABC):
    """Kontrak: Semua efek audio harus punya method 'apply' yaa."""
    @abstractmethod
    def apply(self, song: Song):
        """Menerapkan efek pada lagu.
        
        Args:
            song (Song): Objek lagu yang akan di kasih efek.
        """
        pass

class IMusicPublisher(ABC):
    """Kontrak: Semua layanan publikasi harus punya method 'upload' yaak."""
    @abstractmethod
    def upload(self, song: Song):
        """Proses unggah lagu ke platform publikasi."""
        pass

# --- IMPLEMENTASI KONKRIT (SRP) ---
class BassBoostEffect(IAudioEffect):
    def apply(self, song: Song):
        """Memberikan efek penguatan bass pada lagu."""
        LOGGER.info(f"Audio Effect: Meningkatkan frekuensi Bass pada lagu '{song.title}'.") [cite: 39]

class SpotifyPublisher(IMusicPublisher):
    def upload(self, song: Song):
        """Mengunggah lagu yang sudah diproses ke Spotify."""
        LOGGER.info(f"Publisher: Lagu '{song.title}' berhasil rilis di Spotify.") [cite: 39]

# --- KELAS KOORDINATOR (SRP & DIP) ---
class MusicProductionSystem:
    """Kelas tingkat tinggi untuk mengoordinasi proses produksi musik.
    
    Kelas ini memisahkan logika pemberian efek dan publikasi (memenuhi SRP).
    """
    def __init__(self, effect: IAudioEffect, publisher: IMusicPublisher):
        """Menginisialisasi sistem produksi dengan dependensi yang diperlukan. [cite: 35]
        
        Args:
            effect (IAudioEffect): Implementasi interface efek audio.
            publisher (IMusicPublisher): Implementasi interface layanan publikasi.
        """
        self.effect = effect
        self.publisher = publisher

    def produce(self, song: Song):
        """Jalanin proses: kasih efek, tandai selesai terus di upload.
        
        Args:
            song (Song): Lagu mana yang mau kita produksi sekarang.
        """
        LOGGER.info(f"Memulai produksi lagu: {song.title} oleh {song.artist}") [cite: 39]
        
        try:
            self.effect.apply(song)
            song.is_processed = True
            self.publisher.upload(song)
            LOGGER.info(f"Produksi selesai. '{song.title}' siap dipublikasikan.") [cite: 39]
        except Exception as e:
            LOGGER.error(f"Gagal memproses lagu {song.title}: {str(e)}") [cite: 39]

# --- PROGRAM UTAMA --- 
if __name__ == "__main__":
    # 1. Setup Awal
    my_song = Song("Cranberries", "Indie Band", "audio_binary_data")
    
    # 2. Inject implementasi Bass Boost dan Spotify
    bass_effect = BassBoostEffect()
    spotify_pub = SpotifyPublisher()
    
    studio = MusicProductionSystem(effect=bass_effect, publisher=spotify_pub)
    
    print("\n--- Skenario 1: Produksi Musik Standar ---")
    studio.produce(my_song)

    # 3. Pembuktian OCP: Menambah Efek REVERB tanpa mengubah MusicProductionSystem
    class ReverbEffect(IAudioEffect):
        def apply(self, song: Song):
            # Menggunakan LOGGER sesuai syarat modul
            LOGGER.info(f"Audio Effect: Menambahkan Reverb (Ruang) pada '{song.title}'.")

    new_song = Song("WaterBoys", "Pop Band", "audio_binary_data")
    reverb = ReverbEffect()
    
    # Inject efek baru (OCP Terbukti)
    studio_pro = MusicProductionSystem(effect=reverb, publisher=spotify_pub)
    print("\n--- Skenario 2: Pembuktian OCP (Efek Reverb Baru) ---")
    studio_pro.produce(new_song)