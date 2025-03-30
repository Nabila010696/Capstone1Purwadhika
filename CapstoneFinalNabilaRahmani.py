daftar_siswa = [
    {'Kelas':1,'Nama' :'nabila', 'NIS' : '25010114120052','Jenis Kelamin': 'Perempuan','Matematika' : 80, 'Bahasa Indonesia' : 90, 'IPA' : 80, 'Agama' : 90},
    {'Kelas':1,'Nama' :'yasmin', 'NIS' : '25010114120053','Jenis Kelamin': 'Perempuan','Matematika' : 70, 'Bahasa Indonesia' : 80, 'IPA' : 80, 'Agama' : 90},
    {'Kelas':1,'Nama' :'rahma', 'NIS' : '25010114120054','Jenis Kelamin': 'Perempuan','Matematika' : 75, 'Bahasa Indonesia' : 80, 'IPA' : 100, 'Agama' : 85},
    {'Kelas':1,'Nama' :'ibrahim', 'NIS' : '25010114120055','Jenis Kelamin': 'Laki-laki','Matematika' : 100, 'Bahasa Indonesia' : 75, 'IPA' : 80, 'Agama' : 85},
    {'Kelas':2,'Nama' :'aghni', 'NIS' : '25020114120052','Jenis Kelamin': 'Perempuan','Matematika' : 80, 'Bahasa Indonesia' : 90, 'IPA' : 80, 'Agama' : 90},
    {'Kelas':2,'Nama' :'lidia', 'NIS' : '25020114120053','Jenis Kelamin': 'Perempuan','Matematika' : 70, 'Bahasa Indonesia' : 80, 'IPA' : 80, 'Agama' : 90},
    {'Kelas':2,'Nama' :'lita', 'NIS' : '25020114120054','Jenis Kelamin': 'Perempuan','Matematika' : 75, 'Bahasa Indonesia' : 80, 'IPA' : 100, 'Agama' : 85},
    {'Kelas':2,'Nama' :'richard', 'NIS' : '25020114120055','Jenis Kelamin': 'Laki-laki','Matematika' : 100, 'Bahasa Indonesia' : 75, 'IPA' : 80, 'Agama' : 85},
    {'Kelas':3,'Nama' :'alexander', 'NIS' : '25030114120052','Jenis Kelamin': 'Laki-laki','Matematika' : 80, 'Bahasa Indonesia' : 90, 'IPA' : 80, 'Agama' : 90},
    {'Kelas':3,'Nama' :'hendra', 'NIS' : '25030114120053','Jenis Kelamin': 'Laki-laki','Matematika' : 70, 'Bahasa Indonesia' : 80, 'IPA' : 80, 'Agama' : 90},
    {'Kelas':3,'Nama' :'nikko', 'NIS' : '25030114120054','Jenis Kelamin': 'Laki-laki','Matematika' : 75, 'Bahasa Indonesia' : 80, 'IPA' : 100, 'Agama' : 85},
    {'Kelas':3,'Nama' :'dilham', 'NIS' : '25030114120055','Jenis Kelamin': 'Laki-laki','Matematika' : 100, 'Bahasa Indonesia' : 75, 'IPA' : 80, 'Agama' : 85},
    {'Kelas':4,'Nama' :'eric', 'NIS' : '25040114120052','Jenis Kelamin': 'Laki-laki','Matematika' : 80, 'Bahasa Indonesia' : 90, 'IPA' : 80, 'Agama' : 90},
    {'Kelas':4,'Nama' :'okta', 'NIS' : '25040114120053','Jenis Kelamin': 'Laki-laki','Matematika' : 70, 'Bahasa Indonesia' : 80, 'IPA' : 80, 'Agama' : 90},
    {'Kelas':4,'Nama' :'aziz', 'NIS' : '25040114120054','Jenis Kelamin': 'Laki-laki','Matematika' : 75, 'Bahasa Indonesia' : 80, 'IPA' : 100, 'Agama' : 85},
    {'Kelas':4,'Nama' :'aria', 'NIS' : '25040114120055','Jenis Kelamin': 'Laki-laki','Matematika' : 100, 'Bahasa Indonesia' : 75, 'IPA' : 80, 'Agama' : 85}
    ]

database_daftar_siswa = daftar_siswa.copy()

def menu_tampilan_data_siswa_semua(daftar_siswa) :
    print('                                                         DAFTAR NILAI SEMUA SISWA KELAS     ')
    print('''
     --------------------------------------------------------------------------------------------------------------------------------------------------------
    |      Kelas        |      Nama      |          NIS               |   Jenis Kelamin  |    Matematika   | Bahasa Indonesia |     IPA       |     Agama    |
     --------------------------------------------------------------------------------------------------------------------------------------------------------'''
    )

    for siswa in daftar_siswa:
        print(f'    | {siswa['Kelas']:^14}    | {siswa['Nama'].capitalize() :<14} | {siswa['NIS']:^26} |  {siswa['Jenis Kelamin']:^15} |    {siswa['Matematika']:>12} | {siswa['Bahasa Indonesia']:>16} | {siswa['IPA']:>13} |{siswa['Agama']:>13} |')
    print('     --------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n\n')


def menu_tampilan_data_siswa_kelas(daftar_siswa) :
    print('Masukkan kelas yang ingin Anda lihat!')
    kelas_dicetak = int(input('Kelas 1/2/3/4'))
    print(f'                                                         DAFTAR NILAI SISWA KELAS {kelas_dicetak} ')
    print('''
    ------------------------------------------------------------------------------------------------------------------------------------
    |      Nama      |          NIS               |   Jenis Kelamin  |    Matematika   | Bahasa Indonesia |     IPA       |     Agama  |
    ------------------------------------------------------------------------------------------------------------------------------------'''
    )

    for siswa in daftar_siswa:
        if siswa['Kelas'] == kelas_dicetak :
            print(f'    | {siswa['Nama'].capitalize():<14} | {siswa['NIS']:^26} |  {siswa['Jenis Kelamin']:^15} |    {siswa['Matematika']:>12} | {siswa['Bahasa Indonesia']:>16} | {siswa['IPA']:>13} |{siswa['Agama']:>12}|')
    print('    ------------------------------------------------------------------------------------------------------------------------------------')

#-------------------------------------------------------------------- Menu Utama Data Siswa

def menu_data_siswa():
    print('''
+---------+---------+---------+---------+---------+---------+---------+---------+
|         Selamat Datang di Data Nilai Sekolah Dasar Aisyiah Tembalang          |
|                                                                               |
| Pilih menu data siswa :                                                       |
|                                                                               |
| 1. Menampilkan Daftar Nilai Siswa                                             |
| 2. Menambah Daftar Nilai Siswa                                                |
| 3. Mengubah Daftar Nilai Siswa                                                |
| 4. Menghapus Daftar Nilai Siswa                                               |
| 5. Keluar dari Program Daftar Nilai Siswa                                     |
+---------+---------+---------+---------+---------+---------+---------+---------+
''')
    print('\n')
    pilih_menu_data_siswa = int(input('Ketik Menu yang akan Anda pilih! (1/2/3/4/5) ___'))
    if pilih_menu_data_siswa == 1:
        menu_tampilan_data_siswa()
    elif pilih_menu_data_siswa == 2:
        menu_tambah_data_siswa()
    elif pilih_menu_data_siswa == 3:
        menu_update_data_siswa()
    elif pilih_menu_data_siswa == 4:
        menu_hapus_data_siswa()
    elif pilih_menu_data_siswa == 5:
        menu_keluar_data_siswa()

    print('\n')

#-------------------------------------------------------------------- Menu Tampilkan Daftar Nilai Siswa

def menu_tampilan_data_siswa ():
    print('''
     --------------------------------------------------------------------
    | Menu Tampilan Data Siswa :                                         |
    | 1 = Tampilkan data SELURUH siswa                                   |
    | 2 = Tampilkan data siswa berdasarkan KELAS                         |                      
    | 3 = Tampilan data siswa berdasarkan Nomor Induk Siswa (NIS)        |
    | 4 = Kembali ke Menu Utama                                          |
     --------------------------------------------------------------------'''
    )
    print('\n')

    tampilan_data_siswa = int(input('Ketik 1/2/3/4 : '))
    if tampilan_data_siswa == 1 : #Tampilkan data SELURUH siswa
        menu_tampilan_data_siswa_semua(daftar_siswa)

        print('''
              Ketik Y untuk kembali ke Menu Tampilan Data Siswa''')
        print('\n\n')

        kembali_menu_tampilan_data_siswa = input('Ketik Y untuk kembali ke Menu Tampilan Data Siswa : ').upper()
        if kembali_menu_tampilan_data_siswa == 'Y':
            menu_tampilan_data_siswa()

    elif tampilan_data_siswa == 2 : #Tampilkan data siswa berdasarkan KELAS
        while True :
            menu_tampilan_data_siswa_kelas(daftar_siswa)
            
            print('''
            Apakah Anda ingin melihat data nilai siswa lainnya berdasarkan kelas?
            Y = Melihat data siswa berdasarkan kelas kembali
            N = Kembali ke Menu Menampilkan Daftar Siswa''')

            melihat_kembali = input('Apakah Anda ingin melihat nilai kelas lainnya? Y/N ').upper()
            if melihat_kembali != 'Y' :
                menu_tampilan_data_siswa()
                break

    elif tampilan_data_siswa == 3: #Tampilan data siswa berdasarkan Nomor Induk Siswa (NIS)
        while True:
            print('Masukkan NIS yang ingin Anda lihat dengan format angka: contoh : 25010114120052!')
            nis_cetak = input('Masukkan NIS yang ingin Anda lihat : __ ')
            for siswa in daftar_siswa:
                if siswa['NIS'] == nis_cetak:
                    print('                                                         NILAI SISWA ')
                    print('''
                ------------------------------------------------------------------------------------------------------------------------------------
                |      Nama      |          NIS               |   Jenis Kelamin  |    Matematika   | Bahasa Indonesia |     IPA       |     Agama  |
                ------------------------------------------------------------------------------------------------------------------------------------''')
                    print(f'                |  {siswa["Nama"].capitalize():<12}  | {siswa["NIS"]:^26} |  {siswa["Jenis Kelamin"]:^15} |    {siswa["Matematika"]:>12} | {siswa["Bahasa Indonesia"]:>16} | {siswa["IPA"]:>13} |{siswa["Agama"]:>12}|')
                    print('                ------------------------------------------------------------------------------------------------------------------------------------')
                    print('\n')
                    break 
            else:
                print('Data tidak ditemukan! Inputkan NIS dengan benar!')
                continue

            print('''
            Apakah Anda ingin melihat data nilai siswa lainnya berdasarkan NIS?
            Y = Melihat data siswa berdasarkan NIS kembali
            N = Kembali ke Menu Menampilkan Daftar Siswa''')

            melihat_kembali_1 = input('Y (Kembali melihat data siswa berdasarkan NIS), N (Kembali ke Menu Utama): ').upper()
            if melihat_kembali_1 != 'Y':
                menu_tampilan_data_siswa()
                break
            
    elif tampilan_data_siswa == 4: #Kembali ke Menu Utama
        print('Kembali ke Menu Utama')
        menu_data_siswa()

#-------------------------------------------------------------------- Menu Menambah Daftar Nilai Siswa
def menu_tambah_data_siswa():
    print('''
     --------------------------------------------------------
    | Menu Tambah Data Siswa :                               |
    | 1. Melanjutkan Tambah Data Siswa                       |
    | 2. Kembali ke Menu Utama                               |
     --------------------------------------------------------     
        ''')
    
    input_menu_tambah_data = int(input('Ketik 1/2 ___'))
    if input_menu_tambah_data == 2:
        menu_data_siswa()
    elif input_menu_tambah_data == 1:
        print('''
               -------------------------------------------------------
              | Masukkan data siswa sebagai berikut :                 |
              | - Nomor Induk Siswa (14 digit)                        |
              | - Kelas siswa                                         |
              | - Nama siswa                                          |
              | - Jenis kelamin siswa                                 |
              | - Nilai Matematika, Bahasa Indonesia, IPA, Agama      |
               -------------------------------------------------------
              ''')
        print('\n')
    #input dan verifikasi NIS
        while True:
            masukkan_NIS = input('Masukkan NIS siswa anda sejumlah 14 digit, dan harus berupa angka semua!__')
            list_nis = []
            for siswa in daftar_siswa:
                list_nis.append(siswa['NIS'])
            if masukkan_NIS not in list_nis and len(masukkan_NIS) == 14:
                break
            elif masukkan_NIS in list_nis and len(masukkan_NIS) == 14:
                print('NIS yang Anda cantumkan sudah terdapat di database! Silahkan input kembali NIS yang baru!')
                continue

#input kelas
        while True:
            masukkan_kelas = int(input('Masukkan kelas siswa yang ingin ditambahkan : 1/2/3/4!__'))
            if masukkan_kelas in [1,2,3,4]:
                break
            else :
                print('Masukkan angka kelas dengan benar! 1/2/3/4')

#input nama
        masukkan_nama = input('Masukkan nama siswa dengan huruf kecil semua!').lower()

#input jenis kelamin kelas
        while True:
            masukkan_jeniskelamin = input('Masukkan jenis kelamin siswa update (L/P)! L : Laki-laki/ P : Perempuan!__')
            if masukkan_jeniskelamin == 'L' or masukkan_jeniskelamin == 'l':
                masukkan_jeniskelamin = 'Laki-laki'
                break
            elif masukkan_jeniskelamin == 'P' or masukkan_jeniskelamin == 'p':
                masukkan_jeniskelamin = 'Perempuan'
                break
            else :
                print('Masukkan L atau P')

#input nilai siswa
        masukkan_matematika = int(input('Masukkan nilai Matematika siswa baru!__'))
        masukkan_bahasa_Indonesia = int(input('Masukkan nilai Bahasa Indonesia siswa baru!__'))
        masukkan_IPA = int(input('Masukkan nilai IPA siswa baru!__'))
        masukkan_agama = int(input('Masukkan nilai Agama siswa baru!__'))

#menambah hasil input
        daftar_siswa.append({
            'Kelas':masukkan_kelas,
            'Nama' :masukkan_nama, 
            'NIS' : masukkan_NIS,
            'Jenis Kelamin': masukkan_jeniskelamin,
            'Matematika' : masukkan_matematika, 
            'Bahasa Indonesia' : masukkan_bahasa_Indonesia, 
            'IPA' : masukkan_IPA, 
            'Agama' : masukkan_agama
        })

        print('''
        Lihat daftar siswa terbaru!
        1 = Lihat semua daftar siswa 
        2 = Lihat daftar siswa per kelas''')

        opsi_lihat_data_tambahan = int(input('Ketik 1/2 __'))
        if opsi_lihat_data_tambahan == 1:
            menu_tampilan_data_siswa_semua(daftar_siswa)

            print('\n')
            print('Data berhasil ditambahkan!')

        elif opsi_lihat_data_tambahan == 2 :
            while True :
                menu_tampilan_data_siswa_kelas(daftar_siswa)
                print('\n')
                print('''
                Apakah Anda ingin melihat nilai kelas lainnya?
                    Y = Melihat data siswa kelas lainnya!
                    N = Kembali ke Menu Utama
                      '''
                )
                melihat_kembali_1 = input('Ketik Y/N').upper
                if melihat_kembali_1 == 'Y' :
                    continue
                elif melihat_kembali_1 == 'N' :
                    menu_tambah_data_siswa()
                    break

        print('Apakah ingin menambahkan data baru kembali?')
        isi_data_baru_lagi = input('Apakah Anda ingin memasuki data baru kembali? Y/N__').upper()
        if isi_data_baru_lagi == 'Y':
            menu_tambah_data_siswa()
        else :
            print('Anda kembali ke Menu Utama!')
            menu_data_siswa()


#-------------------------------------------------------------------- Menu Update Daftar Nilai Siswa
def menu_update_data_siswa():
    print('''
         ---------------------------------------------------
        | Menu data update/edit siswa :                     |
        | 1. Update - edit NIS siswa                        |
        | 2. Update - edit data jenis kelamin siswa         |
        | 3. Update - edit data nama siswa                  |
        | 4. Update - edit nilai siswa                      |
        | 5. Kembali ke Menu Utama                          |
        |                                                   |
        | nb : Edit data siswa membutuhkan data NIS siswa   |
         ---------------------------------------------------
        ''')
    pilihan_menu_update = int(input('Ketik 1/2/3/4/5__'))

    if pilihan_menu_update == 1:
        while True:
            nis_cetak = input('Masukkan NIS siswa yang akan diubah datanya!__')
            for siswa in daftar_siswa:
                if siswa['NIS'] == nis_cetak:
                    siswa['NIS'] = input('Masukkan NIS siswa terupdate!__')
                    print('Daftar siswa telah berhasil dirubah! Cek data berikut :')
                    print('\n')
                    print(siswa)
                    break
            else:
                print('NIS tidak ditemukan, pastikan NIS diinputkan dengan benar!')
                continue  

            print('\n')
            print('Apakah Anda ingin mengupdate data NIS kembali? Y/N')
            print('\n')
            input_update_kembali = input('Y/N__').upper()
            if input_update_kembali == 'Y':
                continue
            elif input_update_kembali =='N':
                print('Kembali ke Menu Update/Edit siswa__')
                menu_update_data_siswa()
    
    elif pilihan_menu_update == 2:
        while True :
            nis_cetak = input('Masukkan NIS siswa yang akan diubah datanya!__')
            for siswa in daftar_siswa:
                if siswa['NIS'] == nis_cetak:
                    jenis_kelamin_update = input('Masukkan jenis kelamin L/P!__').upper()
                    if jenis_kelamin_update == 'L':
                        siswa['Jenis Kelamin'] = 'Laki-laki'
                    elif jenis_kelamin_update == 'P':
                        siswa['Jenis Kelamin'] = 'Perempuan'
                    print(siswa)
                    break
            else :
                siswa['NIS'] != nis_cetak
                print('Data NIS tidak tersedia! Inputkan NIS kembali!')
                continue
            print('\n')
            print('Apakah Anda ingin mengupdate data Jenis Kelamin kembali? Y/N')
            print('\n')
            input_update_kembali = input('Y/N__').upper()
            if input_update_kembali == 'Y':
                continue
            elif input_update_kembali =='N':
                print('Kembali ke Menu Update/Edit siswa')
                menu_update_data_siswa()
                break
                
    elif pilihan_menu_update == 3:
        while True:
            nis_cetak = input('Masukkan NIS siswa yang akan diubah datanya!__')
            for siswa in daftar_siswa:
                if siswa['NIS'] == nis_cetak:
                    nama_update = input('Masukkan nama edit!__')
                    siswa['Nama'] = nama_update
                    print(siswa)
                    break
            else :
                siswa['NIS'] != nis_cetak
                print('Data NIS tidak tersedia! Inputkan NIS kembali!')
                continue
            print('\n')
            print('Apakah Anda ingin mengupdate data Nama kembali? Y/N')
            print('\n')
            input_update_kembali = input('Y/N__').upper()
            if input_update_kembali == 'Y':
                continue
            elif input_update_kembali =='N':
                print('Kembali ke Menu Update/Edit siswa')
                menu_update_data_siswa()
                break
        
    elif pilihan_menu_update == 4:
        while True :
            nis_cetak = input('Masukkan NIS siswa yang akan diubah datanya!__')
            for siswa in daftar_siswa:
                if siswa['NIS'] == nis_cetak:
                    siswa['Matematika'] = int(input('Masukkan nilai Matematika update!__'))
                    siswa['Bahasa Indonesia'] = int(input('Masukkan nilai Bahasa Indonesia update!__'))
                    siswa['IPA'] = int(input('Masukkan nilai IPA update!__'))
                    siswa['Agama'] = int(input('Masukkan nilai Agama update!__'))
                    print(siswa)
                    break
            else :
                siswa['NIS'] != nis_cetak
                print('Data NIS tidak tersedia! Inputkan NIS kembali!')
                continue
            
            print('\n')
            print('Apakah Anda ingin mengupdate data Nilai kembali? Y/N')
            print('\n')
            input_update_kembali = input('Y/N__').upper()
            if input_update_kembali == 'Y':
                continue
            elif input_update_kembali =='N':
                print('Kembali ke Menu Update/Edit siswa')
                menu_update_data_siswa()
                break
    
    elif pilihan_menu_update == 5:
        menu_data_siswa()

#-------------------------------------------------------------------- Menu Hapus Daftar Nilai Siswa
def menu_hapus_data_siswa():

    print('''
    ---------------------------------------------------------
    | Menu Pilihan Hapus :                                  |
    | 1. Hapus data siswa berdasarkan Nomor Induk Siswa     |
    | 2. Kembali ke Menu Utama                              |
    ---------------------------------------------------------      
    ''')
    pilihan_menu_hapus = int(input('Ketik 1/2__ '))
    if pilihan_menu_hapus == 1:
        while True:
            print('Masukkan NIS siswa yang ingin Anda hapus! Pastikan NIS terdiri dari 14 digit angka')
            NIS_siswa_hapus = input('Masukkan NIS siswa yang ingin dihapus:__ ')
            for siswa in daftar_siswa:
                if siswa['NIS'] == NIS_siswa_hapus:
                    daftar_siswa.remove(siswa)
                    print(f'Penghapusan data siswa dengan NIS {NIS_siswa_hapus} berhasil!')
                    print('\n\n')
                    menu_tampilan_data_siswa_semua(daftar_siswa) #menampilkan semua data siswa untuk cek apakah data sudah terhapus
                    break
            else :
                print('NIS yang Anda hapus tidak tersedia!')
                continue

            hapus_lagi = (input('Apakah Anda ingin menghapus data siswa by NIS kembali? Y/N__')).upper()
            if hapus_lagi != 'Y':
                menu_hapus_data_siswa()
                break

    elif pilihan_menu_hapus == 2:
        menu_data_siswa() #menuju menu tampilkan menu utama

#-------------------------------------------------------------------- Menu Keluar dari Menu Daftar Nilai Siswa
def menu_keluar_data_siswa():
    print('Anda telah keluar dari sistem Data Nilai Siswa SD Aisyiah Tembalang!')
    

#-------------------------------------------------------------------- Menjalankan Menu Daftar Nilai Siswa
menu_data_siswa()