print ('\n--------------------------------------------------')
print('DAFTAR BARANG DI LAB MANAJEMEN INFORMATIKA')
print ('--------------------------------------------------')

class Barang: 
    def __init__(self, nama="", kode="", jumlah=0, kondisi=""):
        self.barang = nama
        self.kode = kode
        self.jumlah = jumlah
        self.kondisi = kondisi

    def tampilData(self):
        print('Nama Barang: ', self.barang)
        print('Kode Barang: ', self.kode)
        print('Jumlah Barang: ', self.jumlah)
        print('Kondisi Barang: ', self.kondisi)

Barang1 = Barang('Komputer', 'KB001', 40, 'Baik\n')
Barang2 = Barang('Proyektor', 'PJ002', 1, 'Rusak\n')
Barang3 = Barang('Meja', 'MJ003', 55, 'Baik\n')

Barang1.tampilData()
Barang2.tampilData()
Barang3.tampilData()