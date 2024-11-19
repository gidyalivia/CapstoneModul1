#Case Study: Data Stok (Gudang)

data_stok = [{
        'code' : 'B001',
        'produk': 'Beras',
        'kategori':'Bahan Pokok',
        'qty': 25,
        'harga': 37000, 
        'tgl_masuk': '2024-10-11'
    }, 
    {
        'code' : 'B002',
        'produk': 'Kecap',
        'kategori':'Bahan Masak',
        'qty': 15,
        'harga': 15000, 
        'tgl_masuk': '2024-10-07'
    },
    {
        'code' : 'B001',
        'produk': 'Beras',
        'kategori':'Bahan Pokok',
        'qty': 30,
        'harga': 40000, 
        'tgl_masuk': '2024-11-13'
    }]

cart = []

# Main Menu
def menu_utama():
    print('=='*44)
    print('===='*10, 'DATA STOK ','=='*18)
    print('===='*10, 'WARUNG XYZ','=='*18)
    print('=='*44)
    global menu
    menu = int(input(''' 
        List Menu:
        1. Menampilkan Daftar Stok
        2. Menambah Stok
        3. Update Stok
        4. Menghapus Stok
        5. Exit Program
        
        Masukkan angka Menu yang ingin dijalankan : '''))
    return menu

# Daftar Function
def daftar_stok(data): 
    print('---'*29)
    print('Index  \t|Code  \t| Produk\t| Kategori\t| Qty\t| Harga Satuan \t| Tanggal Masuk')
    print('---'*29)
    for i in range(len(data)):
        print('{} \t| {} \t| {}  \t| {} \t| {}  \t| {} \t| {}'.format(i, data[i]['code'],data[i]['produk'],data[i]['kategori'],data[i]['qty'],data[i]['harga'],data[i]['tgl_masuk']))

# Read Menu
def read_stok():
    while True:
        opsi_read = int(input('''
        Pilih Data yang Ditampilkan:
            1. Tampilkan semua stok
            2. Tampilkan berdasarkan kode produk
            3. Kembali ke menu utama
        Masukkan angka Menu yang ingin dijalankan : '''))
        # 1. Tampilkan semua stok
        if opsi_read == 1: 
            if len(data_stok) > 0:
                print('DAFTAR STOK'.center(87,' '))
                daftar_stok(data_stok)
            else:
                print("Tidak ada produk yang tersimpan")
        # 2. Tampilkan berdasarkan kode produk
        elif opsi_read == 2:
            if len(data_stok) > 0:
                print('DAFTAR STOK'.center(87,' '))
                daftar_stok(data_stok)
                primery_key = input('Masukkan code barang : ').upper()
                
                # Code barang yang diinput tersedia di gudang
                matching_stok = [item for item in data_stok if item['code'] == primery_key]
                if matching_stok:
                    print('DAFTAR STOK'.center(87,' '))
                    daftar_stok(matching_stok)
                        
                # Code barang yang diinput tidak tersedia di gudang
                else:
                    print('Produk tidak tersedia di gudang')
            else:
                print("Tidak ada produk yang tersimpan")
        # 3. Kembali ke menu utama
        elif opsi_read == 3:
            break
        else:
            pass


# Create Menu
def create_stok():
    while True:
        opsi_create = int(input('''
        Pilih Opsi:
            1. Menambah produk baru
            2. Kembali ke menu utama
        Masukkan angka Menu yang ingin dijalankan : '''))
        # 1. Menambah produk baru
        if opsi_create == 1:
            code_produk = input('Masukkan Code Produk : ').title()
            produk_ada = False 
            tota_qty = 0
            # Jika produk tersedia di gudang
            matching_stok = [item for item in data_stok if item['code'] == code_produk]
            if matching_stok:
                print('DAFTAR STOK'.center(87, ' '))
                daftar_stok(matching_stok)
                total_qty = sum(item['qty'] for item in matching_stok)
                print(f'Produk dengan kode {code_produk} sudah tersedia.')
                print(f"Total stok saat ini untuk kode {code_produk}: {total_qty}")
                check_tambah = input(f'Apakah Anda ingin menambahkan stock {matching_stok[0]['produk']}? (y/n) :').lower()
                if check_tambah == 'n':
                    produk_ada = True
                    return
                elif check_tambah =='y':
                    nama_produk = matching_stok[0]['produk']
                    kategori_produk = matching_stok[0]['kategori']
                    produk_ada = True
            # Jika produk tidak tersedia di gudang
            if produk_ada == False:
                nama_produk = input('Masukkan Nama Produk Baru : ').title()
                kategori_produk = input('Masukkan Kategori Produk : ').title()
            stok_produk = int(input('Masukkan Stok Produk : '))
            harga_produk = int(input('Masukkan Harga Satuan Produk : '))
            tanggal_masuk = input('Masukkan Tanggal Produk Masuk (YYYY-MM-DD): ')
            cart.append({
                    'code' : code_produk,
                    'produk': nama_produk,
                    'kategori':kategori_produk,
                    'qty': stok_produk,
                    'harga': harga_produk, 
                    'tgl_masuk': tanggal_masuk
                })
            # Menampilkan data yang baru diinput
            print('ISI CART'.center(87,' '))
            daftar_stok(cart)    
            # Memastikan disimpan atau tidaknya data baru
            simpan = input('Apakah Anda ingin menyimpan data? (y/n) : ').lower()
            if simpan == 'y':
                print('Data berhasil disimpan')
                data_stok.extend(cart)
                print('DAFTAR STOK'.center(87,' '))
                daftar_stok(data_stok)
                cart.clear()
            elif simpan =='n':
                cart.clear()
                break
        # 2. Kembali ke menu utama
        elif opsi_create == 2:
            break      
        else:
            pass      


# Update Menu
def update_stok():
    while True: 
        opsi_update = int(input('''
        Pilih Opsi:
            1. Update data
            2. Kembali ke menu utama
        Masukkan angka Menu yang ingin dijalankan : '''))
        # 1. Update data
        if opsi_update == 1:
            data_stok.sort(key=lambda produk: produk['tgl_masuk'])
            print('DAFTAR STOK'.center(87,' '))
            daftar_stok(data_stok)
            code_produk = input('Masukkan code produk yang ingin diupdate : ').title()
            
            # Jika produk tersedia di gudang
            produk_list = [item for item in data_stok if item['code'] == code_produk]
            if produk_list:
                    print('DAFTAR STOK'.center(87,' '))
                    daftar_stok(produk_list)
                    # Konfirmasi lanjut/tidaknya update
                    confirm_update = input('Lanjutkan update? (y/n) : ').lower()
                    # Lanjut update
                    if confirm_update == 'y':
                        input_kolom = int(input('''
        Menu Update
        1. Qty
        2. Harga Satuan
        Masukkan angka menu berdasarkan kolom yang ingin di update : '''))
                        # Update data kolom Qty (mengambil stok di gudang berdasarkan barang yang masuk terlebih dahulu)
                        if input_kolom == 1:
                            qty_produk_diambil = int(input('Masukkan jumlah produk yang diambil : '))
                            total_qty = sum(item['qty'] for item in produk_list)
                            # for i in range(len(produk_list)):
                            # Jika jumlah yang diinput lebih besar dari jumlah stok
                            if qty_produk_diambil > total_qty:
                                print(f"Stok tidak cukup, total {produk_list[0]['produk']} hanya tersedia {total_qty}")
                            else:
                                # Proses pengambilan berdasarkan First In First Out
                                for item in produk_list:
                                    if qty_produk_diambil > item['qty']:
                                        qty_produk_diambil -= item['qty']
                                        cart.append(item.copy())  # Tambahkan ke cart
                                        item['qty'] = 0  # Stok habis
                                    else:
                                        cart.append({
                                            'code': item['code'],
                                            'produk': item['produk'],
                                            'kategori': item['kategori'],
                                            'qty': qty_produk_diambil,
                                            'harga': item['harga'],
                                            'tgl_masuk': item['tgl_masuk']
                                        })
                                        item['qty'] -= qty_produk_diambil
                                        qty_produk_diambil = 0
                                        break
                                # Menampilkan data yang diambil dari stok
                                print('ISI CART'.center(87,' '))
                                daftar_stok(cart)
                                # Konfirmasi update/tidak
                                check_update = input('Apakah Anda ingin menyimpan data update? (y/n) : ')
                                if check_update == 'y':
                                    print('Data berhasil di update')
                                    print('DAFTAR STOK'.center(87,' '))
                                    daftar_stok(data_stok)
                                    cart.clear()
                                else:
                                    cart.clear()
                                    break
                        # Update data kolom Harga Satuan (mengubah harga satuan produk)
                        elif input_kolom == 2:
                            harga_baru = int(input(f'Masukkan harga satuan produk {produk_list[0]['produk']} terbaru : '))
                            # Konfirmasi update/tidak
                            check_update = input('Apakah Anda ingin menyimpan data update? (y/n) : ')
                            if check_update == 'y':
                                for item in produk_list:
                                    item['harga'] = harga_baru
                                print('Data berhasil di update')
                                print('DAFTAR STOK'.center(87,' '))
                                daftar_stok(data_stok)
                            elif check_update =='n':
                                break
                    # Tidak lanjut update
                    elif confirm_update == 'n':
                        print('Update dibatalkan.')
            # Jika produk tidak tersedia di gudang
            else:
                print(f"Tidak ada produk dengan code {code_produk} yang tersimpan")
        # 2. Kembali ke menu utama
        elif opsi_update == 2 :
            break
        else:
            pass
        

# delete stok
def delete_stok():
    while True:
        opsi_delete = int(input('''
        Pilih Opsi:
            1. Delete data
            2. Kembali ke menu utama
        Masukkan angka Menu yang ingin dijalankan : '''))
        data_stok.sort(key=lambda produk: produk['tgl_masuk'])
        print('DAFTAR STOK'.center(87,' '))
        daftar_stok(data_stok)
        # 1. Delete data (Menghapus data yang terlebih dahulu masuk. Contoh kondisi: produk yang expired)
        if opsi_delete == 1:
            code_produk = input('Masukkan code produk yang ingin dihapus : ').title()
            produk_ada = False 
            # Jika produk tersedia di gudang
            for i in range(len(data_stok)):
                if code_produk == data_stok[i]['code']:
                    # Konfirmasi delete/tidak
                    check_del = input(f'Apakah Anda ingin menghapus data {data_stok[i]['produk']} pada tanggal {data_stok[i]['tgl_masuk']}? (y/n) : ')
                    if check_del == 'y':
                        produk_ada = True
                        del data_stok[i]
                        print('Data berhasil dihapus')
                        print('DAFTAR STOK'.center(87,' '))
                        daftar_stok(data_stok)
                        break
                    else:
                        produk_ada = True
                        break
            # Jika produk tidak tersedia di gudang
            if produk_ada ==False:
                print(f"Tidak ada produk dengan code {code_produk} yang tersimpan")
        # 2. Kembali ke menu utama
        elif opsi_delete == 2:
            break
        else:
            pass


while True:
    menu= menu_utama()
    if menu == 1:
        read_stok()
    elif menu == 2:
        create_stok()
    elif menu == 3:
        update_stok()
    elif menu == 4:
        delete_stok()
    elif menu == 5:
        print('Keluar dari Program.')
        break
    else:
        print('Pilihan yang Anda masukkan tidak valid. Coba Lagi!')