print("============================")
print("        NILAI AKHIR         ")
print("============================\n")
print("       KETENTUAN NILAI       ")
print(" 1. NILAI PRESENSI 10%      ")
print(" 2. NILAI TUGAS 20%     ")
print(" 3. NILAI UTS 30%      ")
print(" 4. Nilai UAS 40 %     ")
print("============================")

# Raihan Adi Wijiyanto
# 2411501550

#INPUT
nilai_presensi = int(input("Masukkan Nilai Presensi Anda : "))
nilai_tugas = int(input("Masukkan Nilai Tugas Anda : "))
nilai_uts = int(input("Masukkan Nilai UTS Anda : "))
nilai_uas = int(input("Masukkan Nilai UAS Anda : "))

# PROSES
hasil = 0.1 * nilai_presensi + 0.2 * nilai_tugas + 0.3 * nilai_uts + 0.4 * nilai_uas 

if hasil >=85 and hasil <=100 :
  grade = "A"
elif hasil >=80 and hasil <=84 :
  grade = "A-"
elif hasil >=75 and hasil <=79 :
  grade = "B+"
elif hasil >=70 and hasil <=74 :
  grade = "B"
elif hasil >=60 and hasil <=69 :
  grade = "C"
elif hasil >=0 and hasil <=50 :
  grade = "D"
else:
  grade = "Nilai tidak Valid Silahkan Masukan Ulang"

print("Nilai Presensi Anda : " , nilai_presensi)
print("Nilai Tugas Anda :" , nilai_tugas)
print("Nilai UTS Anda : " , nilai_uts)
print("Nilai UAS Anda : " , nilai_uas )
print("Hasil Nilai Akhir Anda : " , hasil )
print("Hasil Grade Anda : " , grade )
print("\n")

print("============================")
print("        Terima Kasih         ")
print("============================\n")