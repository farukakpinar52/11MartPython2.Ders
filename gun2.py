#f-string ve kullanıcıdan veri alarak alınan verinin uygun formata dönüştürülmesi
# vade = int(input("Vade sayısını giriniz : "))
# krediTutar = int(input("Kredi tutarınızı giriniz : "))
# sonucMesaj = f"Aylık kredi geri ödemeniz {int(krediTutar/vade)} TL'dir."
# print(sonucMesaj)

dizi =["a","b","c"]
print(dizi)
dizi.append("d") #dizinin sonuna eleman ekler
print(dizi)

dizi.clear()
print(dizi)

dizi2=["asd",2,True]
dizi2.pop()  #dizinin son elemannı siler ve geri dönderir
dizi2.pop(0)  #dizinin 0.index elemannı siler ve geri dönderir
print(dizi2)

dizi3=[231,11,5,111,"aaaa"]
dizi3.remove(11) # pop fonk. index ile çalışırken remove fonksiyonu value yani değer ile çalışır

dizi3.extend(["abim","ben","sen"]) #diziyi buradaki elemanları dizimizin sonuna ekleyerek genişlettik
print(dizi3)




