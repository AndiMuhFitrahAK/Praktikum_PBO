from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    raw_data: str  #Simulasi data audio
    is_processed: bool = False

# === KODE BURUK (SEBELUM REFACTOR) ===
class MusicManager: # Melanggar SRP, OCP, DIP
    def process_and_upload(self, song: Song, effect: str):
        print(f"Mengolah lagu: {song.title} oleh {song.artist}")
        
        # LOGIKA EFEK (Pelanggaran OCP/DIP)
        if effect == "distorsi":
            print("Menerapkan efek Distorsi Gitar...")
        elif effect == "bass_boost":
            print("Meningkatkan frekuensi Bass...")
        else:
            print("Efek tidak didukung.")
            return False
            
        # LOGIKA PUBLIKASI (Pelanggaran SRP)
        print(f"Mengunggah '{song.title}' ke Spotify...")
        song.is_processed = True
        return True

# --- REFACTORING: ABSTRAKSI (Kontrak DIP/OCP) ---
class IAudioEffect(ABC):
    """Kontrak: Semua efek audio harus punya method 'apply' yaa."""
    @abstractmethod
    def apply(self, song: Song):
        pass

class IMusicPublisher(ABC):
    """Kontrak: Semua layanan publikasi harus punya method 'upload' yaak."""
    @abstractmethod
    def upload(self, song: Song):
        pass

# --- IMPLEMENTASI KONKRIT (SRP) ---
class BassBoostEffect(IAudioEffect):
    def apply(self, song: Song):
        print(f"Audio Effect: Meningkatkan Bass pada lagu '{song.title}'.")

class SpotifyPublisher(IMusicPublisher):
    def upload(self, song: Song):
        print(f"Publisher: Lagu '{song.title}' berhasil rilis di Spotify.")

# --- KELAS KOORDINATOR (SRP & DIP)
class MusicProductionSystem:
    def __init__(self, effect: IAudioEffect, publisher: IMusicPublisher):
        # Dependency Injection: Bergantung pada Abstraksi
        self.effect = effect
        self.publisher = publisher

    def produce(self, song: Song):
        self.effect.apply(song)
        song.is_processed = True
        self.publisher.upload(song)
        print("Produksi Musik Selesai.")

# --- PROGRAM UTAMA --- 
if __name__ == "__main__":
    # 1. Setup Awal
    my_song = Song("Cranberries", "Indie Band", "audio_binary_data")
    
    # 2. Inject implementasi Bass Boost dan Spotify
    bass_effect = BassBoostEffect()
    spotify_pub = SpotifyPublisher()
    
    studio = MusicProductionSystem(effect=bass_effect, publisher=spotify_pub)
    
    print("--- Skenario 1: Produksi Musik Standar ---")
    studio.produce(my_song)

    # 3. Pembuktian OCP: Menambah Efek REVERB tanpa mengubah MusicProductionSystem
    class ReverbEffect(IAudioEffect):
        def apply(self, song: Song):
            print(f"Audio Effect: Menambahkan Reverb (Ruang) pada '{song.title}'.")

    new_song = Song("WaterBoys", "Pop Band", "audio_binary_data")
    reverb = ReverbEffect()
    
    # Inject efek baru (OCP Terbukti)
    studio_pro = MusicProductionSystem(effect=reverb, publisher=spotify_pub)
    print("\n--- Skenario 2: Pembuktian OCP (Efek Reverb Baru) ---")
    studio_pro.produce(new_song)