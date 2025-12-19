from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    raw_data: str
    is_processed: bool = False

# --- ABSTRAKSI: Kontrak untuk OCP & DIP [cite: 111] ---
class IAudioEffect(ABC):
    @abstractmethod
    def apply(self, song: Song):
        pass

class IMusicPublisher(ABC):
    @abstractmethod
    def upload(self, song: Song):
        pass

# --- IMPLEMENTASI KONKRIT: SRP (Satu kelas, satu tanggung jawab) [cite: 120] ---
class BassBoostEffect(IAudioEffect):
    def apply(self, song: Song):
        print(f"Audio Effect: Meningkatkan Bass pada lagu '{song.title}'.")

class SpotifyPublisher(IMusicPublisher):
    def upload(self, song: Song):
        print(f"Publisher: Lagu '{song.title}' berhasil rilis di Spotify.")

# --- KELAS KOORDINATOR: Menerapkan DIP & Dependency Injection [cite: 126, 127] ---
class MusicProductionSystem:
    def __init__(self, effect: IAudioEffect, publisher: IMusicPublisher):
        # Bergantung pada Abstraksi, bukan detail konkrit [cite: 39, 128]
        self.effect = effect
        self.publisher = publisher

    def produce(self, song: Song):
        self.effect.apply(song) # Delegasi tugas efek [cite: 139]
        song.is_processed = True
        self.publisher.upload(song) # Delegasi tugas publikasi [cite: 141]
        print("Produksi Musik Selesai.")

# --- PROGRAM UTAMA & PEMBUKTIAN OCP [cite: 145, 151] ---
if __name__ == "__main__":
    my_song = Song("Cranberries", "Indie Band", "data_audio")
    
    # Inject implementasi yang dibutuhkan [cite: 153, 154]
    studio = MusicProductionSystem(effect=BassBoostEffect(), publisher=SpotifyPublisher())
    
    print("--- Skenario 1: Produksi Musik Standar ---")
    studio.produce(my_song)

    # BUKTI OCP: Menambah efek baru (Reverb) tanpa mengubah kelas koordinator [cite: 156]
    class ReverbEffect(IAudioEffect):
        def apply(self, song: Song):
            print(f"Audio Effect: Menambahkan Reverb pada '{song.title}'.")

    print("\n--- Skenario 2: Pembuktian OCP (Efek Baru) ---")
    new_studio = MusicProductionSystem(effect=ReverbEffect(), publisher=SpotifyPublisher())
    new_studio.produce(Song("WaterBoys", "Pop Band", "data_audio"))