import texttable as tt
import getpass
from perhitungan.penilaian import nilai_mahasiswa
from perhitungan.pembayaran import pembayaran
from perhitungan.calculator import pilihan

def menu():
    print("==========================================")
    print("\n\t----pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. calculator")
    
    pilih=input("\n\tsilakan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2":
        pembayaran()
    elif pilih == "3":
        pilihan()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y\t)?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input................!!!")

print("\nprogram aplikasi mahasiswa pelita bangsa")
print("\nkelas : TI 17C1")
print("\nNama : ASEP SEPTIAN MUHAMAD IQBAL")
print("\nNIM : 311710595")
print("\nAssalamu alaikum silahkan masukkan username anda untuk memulai aplikasi ini terima kasih")
username=input("\nUsername : ")
password=getpass.getpass()
print("======================================================")
if username == "asep" and password == "asep23":
    menu()

else:
    print("maaf password salah...!!!")



    
          
