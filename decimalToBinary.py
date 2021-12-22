from math import pow
# Değişkenler
sonuc = 0
üs = 0
basamak = 0

# Kullanıcıdan sayının alınması
sayi = int(input())


while(sayi > 0):
    # Çevirme işlemlerinin yapılması
    basamak = int((sayi % 2) * pow(10, üs))
    üs += 1
    sayi = sayi // 2
    sonuc += basamak

# Çevrilen sayının ekrana bastırılması
print(sonuc)
