from abc import ABC, abstractmethod

class mobil(ABC):
    def kecepatan(self):
        pass
    def harga(self):
        pass
    def kekuatan(self):
        pass
    def fasilitas(self):
        pass

class BMW(mobil):
    def kecepatan(self):
        return "130km/jam"
    def harga(self):
        return "RP.750JT"
    def kekuatan(self):
        return "kalibrasi yang stabil"
    def fasilitas(self):
        return "nos"
class avanza(mobil):
    def kecepatan(self):
        return "130km/jam"
    def harga(self):
        return "RP.250JT"
    def kekuatan(self):
        return "tahan untuk perjalanan jauh"
    def fasilitas(self):
        return "ac,kursi 8 orang"
    
class ferari(mobil):
    def kecepatan(self):
        return "130km/jam"
    def harga(self):
        return "3M "
    def kekuatan(self):
        return "body aerodinamis"
    def fasilitas(self):
        return "pintu buka keatas,sporty body"
    
def mobil_behavior(Mobil: mobil):
    print(f"kecepatanya adalah: {Mobil.kecepatan()}")
    print(f"harganya adalah: {Mobil.harga()}+ ")
    print(f"kekuatannya adalah: {Mobil.kekuatan()}")
    print(f"fasilitasnya adalah: {Mobil.fasilitas()}")

bmw = BMW();
Avanza = avanza();
Ferari = ferari();

mobil_behavior(bmw);
mobil_behavior(Avanza);
mobil_behavior(Ferari);