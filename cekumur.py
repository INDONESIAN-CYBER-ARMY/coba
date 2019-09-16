    #program pertama belajar python
    #Cek identitas
print ("         ================ CEK UMUR ================")
    #identitsa
nama = raw_input ("Nama Depan: ")
nama_belakang = raw_input ("Nama Belakang: ")
tgl_lahir = input ("Tanggal Lahir [05]: ")
bln_lahir = raw_input ("Bulan Lahir [Maret]: ")
tahun_lahir = input ("Tahun Lahir [1988]: ")
tempat_lahir = raw_input ("Tempat Lahir [Bogor]: ")
jenis_kelamin = raw_input ("Jenis Kelamin [L/P]: ")
    #tahun sekarang
tahun = 2019
print ("        ---------------- KETERANGAN ----------------")
    #hitung Usia
tahun = tahun - tahun_lahir
tambah = tahun + 1
print ("# Jika Bulan lahir belum sampai ditahun 2019 Umur kamu: %s" % tahun)
print ("# Jika Bulan lahir sudah sampai ditahun 2019 Umur kamu: %s" % tambah)
print ("         >>>>>>>>>> created by: Cyber_Hansome <<<<<<<<<< ")



