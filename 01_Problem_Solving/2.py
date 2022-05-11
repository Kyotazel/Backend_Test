# Buat inputan number dan jadikan ke strinf
number = str(input("x = "))


# buat list kosong dan ukuran number
reversed_string = []
index = len(number)

# buat perulangan untuk membalikkan number
while index > 0:
    reversed_string += number[index-1]
    index -= 1

# dari data list jadikan ke string
reversed_string = ''.join(reversed_string)

# cek apabila sama maka True apabila tidak sama maka False
if number == reversed_string and len(reversed_string) != 1:
    print(True)
else:
    print(False)