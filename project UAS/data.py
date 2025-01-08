class DataMahasiswa:
    """Kelas untuk merepresentasikan data mahasiswa."""
    
    def _init_(self):
        self.daftar_mahasiswa = []

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa."""
        self.daftar_mahasiswa.append({'nama': nama, 'nilai': nilai})

    def get_data(self):
        """Mengembalikan daftar mahasiswa."""
        return self.daftar_mahasiswa