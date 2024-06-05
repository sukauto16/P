from abc import ABC,  abstractmethod

class poligon(ABC):
   @abstractmethod
   def jumlah_sisi(self):
       pass

class segitiga(poligon):
    def jumlah_sisi(self):
        print("segitiga memiliki 3 sisi")

class segiempat(poligon):
    def jumlah_sisi(self):
        print("segiempat memiliki 4 sisi")


segitiga = segitiga()
segitiga.jumlah_sisi()
segiempat = segiempat()
segiempat.jumlah_sisi()