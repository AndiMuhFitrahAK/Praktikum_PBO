from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    raw_data: str 
    is_processed: bool = False

# KODE BURUK: Melanggar SRP, OCP, dan DIP [cite: 81]
class MusicManager: 
    def process_and_upload(self, song: Song, effect: str):
        print(f"Mengolah lagu: {song.title} oleh {song.artist}")
        
        # LOGIKA EFEK (Melanggar OCP & DIP karena hardcoded if/else) [cite: 83]
        if effect == "distorsi":
            print("Menerapkan efek Distorsi Gitar...")
        elif effect == "bass_boost":
            print("Meningkatkan frekuensi Bass...")
        else:
            print("Efek tidak didukung.")
            return False
            
        # LOGIKA PUBLIKASI (Melanggar SRP karena gabung dengan logika efek) [cite: 89]
        print(f"Mengunggah '{song.title}' ke Spotify...")
        song.is_processed = True
        return True