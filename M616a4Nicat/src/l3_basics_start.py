# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)
print ("Saam Data Muhendisliyi!")
print ("BAZA stansiyasi:", "V=BAK-0207")
print (2+3)
print("2+3")
print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# TODO: cell, rsrp, drops
cell="BAK-0207"
rsrp=-95.5
print(cell,rsrp)
rsrp=-108.1

print(cell,rsrp) 
drops=2

drops=drops+1

print("drops = ", drops)


print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# TODO: type(...) və «mətn ≠ ədəd»

print(type(3))
print(type(-95.5))
print(type ("BAK-0207"))
print(type(True))
print(type(None))









print("=== Kərpic 4 ===")   # Müqayisə → True / False
# TODO: rsrp < -105, ==

print("=== Kərpic 5 ===")   # Siyahı (list)
# TODO: rsrp_list, indeks, len, orta
menimlistim=(12,1234,13434,2176,32763)
list_deyeri=int(input("deyerivi daxil et:"))
print(menim listim[list deyeri])
print("=== Kərpic 6 ===")   # Lüğət (dict)
# TODO: row = {...}, row["region"]

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# TODO: zəif ölçmələri saymaq

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd


name=input()
yas=int((input) +1)
print("Menim adim",name,"menim yasim",yas)

ad=input("ADIVI DAXIL ELE:")
soy_ad=input("YASIVI DAXIL ET:")
yas=int(input("asivi daxil et:"))
yas=yas+1;
print(yas>25)
print(yas<25)

if yas > 25 :
   print("yasiniz 25 den coxdur")
elif yas < 25:
   print ("yasainiz 25 de kicikdir")
elif yas == 25:
    print ("yasiniz 25 beraberdir")
