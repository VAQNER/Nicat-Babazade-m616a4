# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

# ---------------------------------------------------------------

print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
print("Salam, data mühəndisliyi!")
print("Baza stansiyası:", "BAK-0207")
print(2 + 3)
print("2 + 3")

# ---------------------------------------------------------------

print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu

cell="BAK-0207"
rsrp = -95.5
print(cell, rsrp)

rsrp = -108.1
print(cell, rsrp)

drops = 2
drops = drops + 1
print("drops =", drops)

ad = "Nicat"
yas = "21"
qrup = "616a4"
xasiyyet = "orta"
print("Salam,",ad,yas,qrup,)

# ad = input("Ad: ")
# yas = input("Yas: ")
# qrup = input("Qrup: ")
# xasiyyet = input("Xasiyyet: ")

print("Salam,",ad,yas,qrup,xasiyyet)

# ---------------------------------------------------------------

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None

print(type(3))
print(type(-95.5))
print(type("BAK-0207"))
print(type(True))
print(type(None))

# ---------------------------------------------------------------

print("=== Kərpic 4 ===")   # Müqayisə → True / False


# ---------------------------------------------------------------

print("=== Kərpic 5 ===")   # Siyahı (list)

# ---------------------------------------------------------------

print("=== Kərpic 6 ===")   # Lüğət (dict)



row={"cell_id": "BAK-0207","region":"MASAZIR","rsrp_dbm":-108.1}
print(row["region"])
print(row["rsrp_dbm"])
row["band"]="LTE800"
print(row)
row["region"]="RAZIN"
print (row)

acar = input("1:")
acar2 = input("2:")
row[acar] =acar2
print(row)
# ---------------------------------------------------------------

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
weak = 0
rsrp_list=[-100.1,-110,9,-89.1,-56.2,96.3]
for i in rsrp_list:
    if i<-90:
        print(i,"asagi")
        weak=weak+1

    else: 
        print(i,"yuxari")


for i in rsrp_list :
    vurma= int(input("vurma:"))
    print(i*vurma)
# ---------------------------------------------------------------

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq

# ---------------------------------------------------------------

print("=== Kərpic 9 ===")   # Nöqtə: metod

# ---------------------------------------------------------------

print("=== Kərpic 10 ===")  # import — hazır alət qutusu