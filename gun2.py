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

#for döngüsü
for i in range(10): #  10 'a kadar olan sayılar alınır.
    print(i)
print("-------------------------------------")
for i in range(3,7): #  3'ten başlayıp 7'ye kadar olan sayıları yazdırır
    print(i)
print("-------------------------------------")
for i in range(3,15,5): #  3'ten 15'e kadar olan sayıları beşer beşer yazdırır
    print(i)

print("-------------------------------------")
for i in range(3,15,5): #  3'ten 15'e kadar olan sayıları beşer beşer yazdırır
    print(i)
print("-------------------------------------")

krediler = ["İhtiyaç","Taşıt","Düğün","Ev"]
for kredi in krediler:  #buradaki kullanım foreach yapısı gibi
    print(kredi)
print("-------------------------------------")
for i in range(len(krediler)): #range fonksiyonu direk integer bir değer almak zorunda
    print(krediler[i])
print("-------------------------------------")

# while True:  #bu tarz sonsuz döngüleri durdurmak için terminalde "CTRL + C"  kullanabilirsiniz.
#     print("dur")
print("-------------------------------------")

a=0
while a<4:
    print(a)
    a=a+1

print("-------------------------------------")

i=0
while i<len(krediler):
    print(krediler[i])
    i=i+1

print("----------------while 1.döngü---------------------")

i=0
while i<len(krediler):
    if krediler[i]=="Düğün":
        break
    print(krediler[i])
    i=i+1
print("---------------while 2.döngü----------------------")

i=0
while i<len(krediler):
    print(krediler[i])
    if krediler[i]=="Düğün":
        break
    i=i+1
print("-------------------- FONKSİYONLAR -----------------")

fiyat=100
indirim=20
#def fonksiyon_adi
def calculate():
    print(fiyat-indirim)

calculate()
print("--------------------parametreli FONKSİYONLAR  -----------------")

def CalculateWithParams(a,b,c):
    if(b-c>a):
        print("b ile c nin farkı a dan büyüktür")
    elif(b-a>c):
        print("b ile a nın farkı c 'den büyüktür")
    else:
        print(f"a = {a} , b = {b} , c = {c}")
CalculateWithParams(23,16,11)
CalculateWithParams(42,111,5)
print("--------------------parametreli FONKSİYONLAR-2  -----------------")
def SayHelloWithName(name):
    print(f"{name} kişisi giriş yaptı.")

SayHelloWithName("Fırat")
SayHelloWithName("Sedat")

print("--------------------parametreli değer döndüren FONKSİYONLAR  -----------------")

def calculateAndReturn(price,discount):
    price= price-discount
    return price

indirimliFiyat = calculateAndReturn(100,42)
print(f"indirimli fiyatınız : {indirimliFiyat}")


students1=["Ali Demir","Beyhan Yılmaz","Sedat Öncü","Derya Nur Yılmaz","Seher Yeli","Faruk Pekmez"]
print(f" Ödev öncesi listemiz : {students1} ")
print("--- ///   ÖDEV 1     \\\ --- ")
def addStudentToList(nameSurname):
    students1.append(nameSurname)
    for student in students1:
        print(student)
    print(f"\nSon eklenen öğrenci : {nameSurname}")
addStudentToList("Aslı Zong")

print("\n--- ///   ÖDEV 2     \\\ --- ")
students2=["Ali Demir","Beyhan Yılmaz","Sedat Öncü","Derya Nur Yılmaz","Seher Yeli","Faruk Pekmez"]

def deleteStudent(nameSurname):
    result= nameSurname in students2
    if result:
        print(f"{nameSurname} isimli öğrenci listeden kaldırılmıştır\n")
        students2.remove(nameSurname)
    else:
        print("Silinmeye çalışılan öğrenci listede yok.\n")
print(f"Listenin ilk hali : {students2}\n")

deleteStudent("Ahmet Öncü")
deleteStudent("Sedat Öncü")
deleteStudent("Ali Demir")
print(f"Listenin son hali : {students2}\n")

print("\n--- ///   ÖDEV 3     \\\ --- ")
students3=["Ali Demir","Beyhan Yılmaz","Sedat Öncü","Derya Nur Yılmaz","Seher Yeli","Faruk Pekmez"]

def addNewStudentsToList(*params):
    liste=[]
    for param in params:
        liste.append(param)
    print(f"Gelen veriler listeye eklendi.\nYeni öğrenci listesi : {students3+liste}") 

print(f"Listenin ilk hali : {students3}\n")

addNewStudentsToList("ASLI GÜLEN","FERİDE DURAN","AYÇA ZINGILDAYAN")

print("\n--- ///   ÖDEV 4     \\\ --- ")
students4=["Ali Demir","Beyhan Yılmaz","Sedat Öncü","Derya Nur Yılmaz","Seher Yeli","Faruk Pekmez"]
i=0
while i<len(students4):
    print(students4[i])
    i=i+1

print("\n--- ///   ÖDEV 5     \\\ --- ")
students5=["Ali Demir","Beyhan Yılmaz","Sedat Öncü","Derya Nur Yılmaz","Seher Yeli","Faruk Pekmez"]
       
def findStudentNumber(nameSurname):
    if nameSurname in students5:
        studentNo =students5.index(nameSurname)
        if studentNo>=0:
             print(f"{nameSurname} isimli öğrencinin numarası : {studentNo}")
    elif (nameSurname in students5)==False:
        print(f"{nameSurname} isminde bir kayıt yok.")

findStudentNumber("Derya Nur Yılmaz")
print("---")
findStudentNumber("Faruk Ak")

print("\n--- ///   ÖDEV 6    \\\ --- ")
students5=["Ali Demir","Beyhan Yılmaz","Sedat Öncü","Derya Nur Yılmaz","Seher Yeli","Faruk Pekmez"]
# del students5[1:3]
def deleteStudentsWithIndexRange(a,b):
    i=0
    if (a>0 and b>0) and a<b:
        for i in range(len(students5)):
            if i>=a and i<=b:
                print(f"Listeden silinen öğrenciler {students5[i]}")
                i=i+1
            elif len(students5)<a or len(students5)<b:
                print("girilen aralık listeye ait değil")
        del students5[a:b+1]
    elif(a>0 and b>0) and a>=b:
        print("ilk değer ikinci değerden küçük olmalıdır.")
    elif a<0 or b<0:
        print("pozitif değerler giriniz")

    print(f"Listenin son hali : {students5}")

print(students5)
deleteStudentsWithIndexRange(1,3)
print("-------------------")
deleteStudentsWithIndexRange(-4,3)
print("-------------------")
deleteStudentsWithIndexRange(14,3)
print("-------------------")
deleteStudentsWithIndexRange(11,32)
print("-------------------")