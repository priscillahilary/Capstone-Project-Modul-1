#Capstone Project Module 1 
#Tema: Rental Mobil
#Priscilla Hilary Kusumaningrum #JCDS03

from tabulate import tabulate

Data_Car= [
   {
        'Idx' : 0,
        'Tipe Mobil' : 'Fortuner',
        'Transmisi' : 'MT',
        'Warna' : 'Hitam',
        'Stock' : 2,
        'Harga 12 jam' : 450000,
        'Harga 24 jam' : 900000
    },
    
    {
        'Idx' : 1,
        'Tipe Mobil' : 'Jeep',
        'Transmisi' : 'MT',
        'Warna' : 'Hitam',
        'Stock' : 1,
        'Harga 12 jam' : 500000, 
        'Harga 24 jam' : 1000000
    },

    {
        'Idx' : 2,
        'Tipe Mobil' : 'Avanza',
        'Transmisi' : 'AT',
        'Warna' : 'Silver',
        'Stock' : 3, 
        'Harga 12 jam' : 250000,
        'Harga 24 jam' : 500000
    },

    {
        'Idx' : 3,
        'Tipe Mobil' : 'Jazz', 
        'Transmisi' : 'AT',
        'Warna' : 'Merah',
        'Stock' : 1,
        'Harga 12 jam' : 350000,
        'Harga 24 jam' : 700000
    }
]

#Membuat fungsi untuk menampilkan data mobil rental
def show(data):
    #Menampilkan tabel data rental mobil dalam tabulate
    Column = ['Idx','Tipe Mobil','Transmisi','Warna','Stock','Harga 12 jam','Harga 24 jam']
    #Convert list dalam dictionary ke bentuk list dalam lists
    table = []
    for i in data:
        table.append (list(i.values()))
    print ('\nDaftar Mobil Rentalancar:\n')
    print (tabulate(table,headers=Column,tablefmt="fancy_grid"))

#Membuat fungsi untuk menampilkan data mobil rental dalam filter 'Transmisi'
def filter (data):
    show (Data_Car)  
    cek_trans = input ('Masukkan transmisi:')   
    out = []
    for item in Data_Car:
        if cek_trans.lower() == item['Transmisi'].lower():
            out.append(item)
    show(out)
    data

#Membuat fungsi untuk menambahkan data mobil baru
def add (data):
    #Menampilkan data mobil rental sebelum menambah data mobil
    show(data)
    while True:
        inp = str(input('''
--------------------------------------------+----------------------------------------------------
Apakah anda ingin menambahkan data mobil?(yes/no) : ''')).lower()
        if (inp == 'yes'):
            TipeMobil_new = input('\nMasukkan Tipe Mobil Baru: ')
            #Jika menginput tipe mobil yang sudah ada maka akan mengulang/looping ke pertanyaan pertama
            for i in Data_Car:
                if i['Tipe Mobil'].lower() == TipeMobil_new.lower():
                    break
            else:
                print('\nTipe mobil belum ada,silahkan input data baru') 
                #Jika menginput tipe mobil baru maka akan lanjut ke inputan data mobil baru
                Idx_new= int(input('\nMasukkan Index Baru: '))
                TipeMobil_new = str(input('\nMasukkan Tipe Mobil Baru: ')).capitalize()
                Transmisi_new = str(input('Masukkan Transmisi Mobil: ')).upper()
                Warna_new= str(input('Masukkan Warna Mobil: ')).capitalize()
                Stock_new = int(input('Masukkan Stock Mobil Saat Ini: '))
                Harga12jam_new= int(input('Masukkan Harga Sewa 12 jam: '))
                Harga24jam_new = int(input('Masukkan Harga Sewa 24 jam: '))
                simpan = str(input('\nApakah anda ingin menambah dan menyimpan data? (yes/no) : ')).lower()
                if(simpan == 'yes'):
                    Data_Car.append({'Idx': Idx_new,'Tipe Mobil': TipeMobil_new,'Transmisi': Transmisi_new,'Warna': Warna_new,'Stock': Stock_new,'Harga 12 jam':Harga12jam_new,'Harga 24 jam':Harga24jam_new})
                    show(data)
                    print('\nData Berhasil Ditambahkan')
                else:
                    print('\nData Belum Ditambahkan')
        elif(inp == 'no'):
            break
        else:
            break
    show (data)

#Membuat fungsi untuk memperbaharui/mengupdate data stock mobil
def update (data):
    #Menampilkan data mobil rental sebelum mengupdate stock mobil
    show (data)
    while True:
        inp = str (input('''
--------------------------------------------+----------------------------------------------------
Apakah anda ingin mengupdate data stock mobil?(yes/no) : ''')).lower()
        if (inp == 'yes'):
            #Menginput indeks mobil yang ingin diupdate 
            cek_idx = int(input('\nMasukkan Index Mobil(secara indexing, row 1=0): '))
            if cek_idx <0 or cek_idx >= len(Data_Car):
                #jika indeks mobil yang diinput kurang dari 0 atau lebih dari panjang iterasi di Data_Car maka akan mengulang/looping ke pertanyaan pertama
                print ('Indeks mobil tidak sesuai')
                continue
            else:
                #jika indeks mobil yang diinput sesuai maka lanjut input stock mobil yang ingin diupdate
                stock_update = int(input ('Masukkan stock mobil terupdate:'))
                updt = str(input('\nApakah anda ingin mengupdate dan menyimpan data? (yes/no) : ')).lower()
                if(updt == 'yes'):
                    Data_Car[cek_idx]['Stock']=stock_update
                    show (data)
                    print('\nData Berhasil Diupdate')
                else:
                    print('\nData Belum Diupdate')
                    break
        elif (inp == 'no'):
            break
        else:
            break
    show (data)

#Membuat fungsi untuk menghapus 
def delete(data):
    show (data)
    while True:
        inp = str (input('''
--------------------------------------------+----------------------------------------------------
Apakah anda ingin menghapus data mobil?(yes/no) : ''')).lower()
        if (inp == 'yes'):
            cek_idx= int(input('\nMasukkan Index Mobil(secara indexing, row 1=0): '))
            if cek_idx <0 or cek_idx >= len(Data_Car):
                #jika indeks mobil yang diinput kurang dari 0 atau lebih dari panjang iterasi di Data_Car maka akan mengulang/looping ke pertanyaan pertama
                continue
            else:
                delete = str(input('Apakah anda ingin menghapus mobil ini? (yes/no) : ')).lower()
                if(delete == 'yes'):
                    del Data_Car[cek_idx]
                    #data dicopy agar dictionary tidak berubah saat dihapus, data tetap sama saat melakukan penyewaan berdasarkan index
                    show (data)
                    print('\nData Berhasil Dihapus')
                    break
                else:
                    print('\nData Belum Dihapus')
                    break
        elif(inp == 'no'):
            break
        else:
            break

#Membuat Keranjang Penyewaan Mobil,dibuat global agar dapat diakses di fungsi lain dan juga valuenya dapat di reset setelah melakukan pembayaran
cart =[]
total_harga= 0
#Membuat fungsi untuk menyewa mobil
def rental (data):
    global cart
    reorder = 'yes'
    while reorder!= 'no':
        show(data) 
        while True:
            cek_idx= int(input('\nMasukkan Index Mobil (secara indexing, row 1=0): '))
            if cek_idx < 0 or cek_idx >= len(Data_Car):
                #jika indeks mobil yang diinput kurang dari 0 atau lebih dari panjang iterasi di Data_Car maka akan mengulang/looping ke pertanyaan pertama
                print('Index mobil tidak sesuai')
            else:
                break

        #Validasi inputan lama sewa dengan tarif 12 jam atau tarif 24 jam, jika tidak maka akan looping
        while True:
            lama_sewa = input("Masukkan lama sewa [Harga 12 jam /Harga 24 jam] : ")
            if lama_sewa in ['Harga 12 jam', 'Harga 24 jam']:
                break
            else:
                print('Lama sewa tidak tersedia')

        #Stock mobil akan berkurang sesuai dengan jumlah mobil yang disewa
        while True:
            qty = int(input('Masukkan jumlah mobil yang disewa : '))
            if qty > Data_Car[cek_idx]['Stock']:
                print('Stock mobil tidak mencukupi')
                return
            elif qty <= 0:
                print('Jumlah mobil yang disewa tidak bisa kurang dari 1')
                return
            else:
                #Menambahkan data mobil yang disewa ke cart 
                Data_Car[cek_idx]['Stock'] -= qty
                cart.append({
                    'Tipe Mobil': Data_Car[cek_idx]['Tipe Mobil'],
                    'Transmisi': Data_Car[cek_idx]['Transmisi'],
                    'Warna': Data_Car[cek_idx]['Warna'],
                    'Stock': qty,
                    'Lama Sewa': lama_sewa,
                    'Tarif': Data_Car[cek_idx][lama_sewa],
                    'Total': Data_Car[cek_idx][lama_sewa] * qty,
                })
            break

        print ('\t\t\t\t    Update Daftar Mobil')
        show (data)

        #cek user ingin menambah mobil yang disewa atau tidak, jika 'no' maka akan keluar dari looping
        confirm = input('Apakah akan menyewa lagi?(yes/no): ').lower()
        if confirm == 'no':
            reorder = 'no'

#Membuat fungsi pembayaran sewa mobil
def payrental (data):
    global cart
    global total_harga
    show (data)
    
    if len(cart) == 0:
        print('Anda belum menyewa mobil')
        return
    else:
        for i in cart:
            total_harga += i['Total']
        while True:
            print(f'Total Yang Harus Dibayar = {total_harga}')
            qty_uang = int(input('Masukkan jumlah uang : '))
            if(qty_uang > total_harga) :
                kembali = qty_uang - total_harga
                print(f'Terima kasih \n\nUang kembalian anda : {kembali}')
                break
            elif(qty_uang == total_harga) :
                print('Terima kasih')
                break
            elif qty_uang < total_harga:
                kekurangan = total_harga - qty_uang
                print(f'Uang anda kurang sebesar {kekurangan}')
            break

#Membuat fungsi untuk keluar dari aplikasi 
def exit(data):
    print('\n<<< Terimakasih telah menggunakan aplikasi RENTALANCAR! >>>')
    print('\n')
    data
'==============================================================================================================='

#CallMenu

def read_menu(data):
    while True:
        menu1 = int(input('''
-----------------------+----------------------------------+
Pilihan menu:
    1. Menampilkan semua data menu
    2. Menampilkan data mobil berdasarkan transmisi
    3. Kembali ke Menu Utama
-----------------------+----------------------------------+
Masukkan pilihan menu: '''))
        if menu1 == 1:
            show(data)
        elif menu1 == 2:
            filter(data)
        elif menu1 == 3:
            main_menu()
            break
        else:
            print('Pilihan menu tidak tersedia')

def add_menu (data):
    while True:
        menu2 = int(input('''
-----------------------+----------------------------------+
Pilihan menu:
    1. Menambahkan data mobil 
    2. Kembali ke Menu Utama
-----------------------+----------------------------------+
Masukkan pilihan menu: '''))
        if menu2 == 1:
            add (data)
        elif menu2 == 2:
            main_menu()
            break
        else:
            print('Pilihan menu tidak tersedia')

def update_menu (data):
    while True:
        menu3 = int(input('''
-----------------------+----------------------------------+
Pilihan menu:
    1. Mengupdate stock mobil 
    2. Kembali ke Menu Utama
-----------------------+----------------------------------+
Masukkan pilihan menu: '''))
        if menu3 == 1:
            update (data)
        elif menu3 == 2:
            main_menu()
            break
        else:
            print('Pilihan menu tidak tersedia')       

def delete_menu (data):
    while True:
        menu4 = int(input('''
-----------------------+----------------------------------+
Pilihan menu:
    1. Menghapus data mobil
    2. Kembali ke Menu Utama
-----------------------+----------------------------------+
Masukkan pilihan menu: '''))
        if menu4 == 1:
            delete (data)
        elif menu4 == 2:
            main_menu()
            break
        else:
            print('Pilihan menu tidak tersedia')       

def sewa_menu(data):
    while True:
        menu5 = int(input ('''
-----------------------+----------------------------------+
Pilihan menu:
    1. Menyewa Mobil        
    2. Pembayaran & Finalisasi Sewa              
    3. Pembatalan Sewa & kembali ke menu utama 
-----------------------+----------------------------------+
Masukkan pilihan menu : '''))
        
        if menu5 == 1:
            rental (data)
        elif menu5 == 2:
            payrental (data)
        elif menu5 == 3:
            print('Penyewaan mobil selesai')
            break
        else:
            print('Pilihan menu tidak tersedia')

def main_menu():
    while True:
        user_input = int(input('''
------WELCOME TO RENTALANCAR-----
                           
MENU: 
    1. Menampilkan Data Mobil Rentalancar
    2. Menambah Data Mobil Rentalancar
    3. Memperbaharui Stock Data Mobil Rentalancar
    4. Menghapus Data Mobil Rentalancar
    5. Menyewa Mobil Rentalancar
    6. Keluar
                           
Masukkan pilihan menu: '''))
        if(user_input == 1):
            read_menu (Data_Car)
        elif (user_input == 2):
            add_menu (Data_Car)
        elif (user_input == 3):
            update_menu (Data_Car)
        elif (user_input == 4):
            delete_menu (Data_Car)
        elif (user_input == 5):
            sewa_menu (Data_Car)
        elif (user_input == 6):
            exit (Data_Car)
        else:
            print('\n<<< Silahkan masukkan indeks menu yang tersedia >>>')
main_menu()



             

    

