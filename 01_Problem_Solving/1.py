# Buat Nums kosong dan isi dari inputan dengan menggunakan for dan split
nums = []
nums = [int(item) for item in input("nums = ").split()]

# Buat masukkan untuk target
target = int(input("target = "))

# Buat 3 variabel berikut agar scope global
tambah = 0
number1 = 0
number2 = 0

# batasi sesuai pengaturan
if (len(nums) < 2 or len(nums) > 104) or (min(nums) < -109 or max(nums) > 109) or (target < -109 or target > 109):
    pass
else:
    # Buat perulangan untuk hasil yang pertama
    for i in range(0, len(nums)):
        # Buat perulangan untuk hasil yang kedua
        for j in range(i + 1, len(nums)):
            
            # apabila target samadengan tambah maka berhenti
            if target == tambah:
                break
            # jika tidak maka ulang sampai tambah sama dengan target lalu simpan dari masing masing kedalam variabel
            else:
                tambah = (nums[i] + nums[j])
                number1 = nums[i]
                number2 = nums[j]
    # Buat list Kosong
    hasil = []
    # Buat variabel hasil1 dan cari dalam nums angka dari number1 merupakan index ke berapa
    hasil1 = nums.index(number1)
    # manipulasi index dari hasil sebelumnya agar tidak duplikat
    nums[hasil1] = 0
    hasil2 = nums.index(number2)
    # kembalikan ke variabel awal
    nums[hasil1] = number1

    # append kedua hasil kedalam list
    hasil.append(hasil1)
    hasil.append(hasil2)

    # print hasil
    print(hasil)