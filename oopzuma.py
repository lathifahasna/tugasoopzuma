class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True
        
    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        
    def tembak(self):
        self.skor += 50
        
    def info_status(self):
        print("=== STATUS KATAK ZUMA ===")
        print(f"Warna Peluru : {self.warna_peluru}")
        print(f"Skor Saat Ini: {self.skor}")
        print(f"Status Aktif : {self.is_active}")
        print("--------------------------")

katak_player = KatakZuma("Kuning")

katak_player.info_status()

katak_player.tembak()

katak_player.ganti_warna("Merah")

katak_player.tembak()

katak_player.info_status()