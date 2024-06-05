class kendaraan():
    def __init__(self, nama, warna, harga):
        self.nama = nama    
        self.warna = warna
        self.harga = harga
        
    def tampilan(self):
        print('Details :', self.nama, self.warna, self.harga)

    def kecepatan_max(self):
        print('kecepatan kendaraan max = 150 km/jam')

    def change_gear(self):
        print('kendaraan ini bisa mengganti gaer sampai 6')

class mobil(kendaraan):
    def kecepatan_max(self):
        print('kecepatan kendaraan max =  km/jam')

    def change_gear(self):
        print('kendaraan ini bisa mengganti gaer sampai 7')


mobil = mobil('mobil x1', 'hijau', '20000')
mobil.tampilan()
mobil.kecepatan_max()
mobil.change_gear()

kendaraan = kendaraan('pajero', 'kuning', '75000')
kendaraan.tampilan()
kendaraan.kecepatan_max()
kendaraan.change_gear()