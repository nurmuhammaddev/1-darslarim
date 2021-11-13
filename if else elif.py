# 1-----------------------------------------------------------------------------------

# kun=input("bugun qaysi kun?>>>")
# if kun =="shanba" or kun=="yakshanba":
#      print("bugun dam olish kuni")
# elif kun =='dushanba' or kun == 'seshanba' or kun =='chorshanba'or kun =='payshanba'or kun =='juma':
#      print("bugun ish kuni")
# else:
#      print("bunday kun mavjud emas")

# 2------------------------------------------------------------------------------------------

# menu=['osh','shashlik','non',"go'sht"]
# ovqat_tanla=input("nima ovqat yeysiz>>")
# if ovqat_tanla not in menu:
#     print("bizda bunday taom yo'q kechirasiz boshqa taom tanlang")
# else:
#     print("buyurma qabul qilindi")

# 3------------------------------------------------------------------------------------------

# menu =['osh','shashlik','lagman',"go'sht",'non']
# buyurtma =["osh","shashlik","lagman","lavash"]
# if buyurtma:
#     for taom in buyurtma:
#         if taom in menu:
#             print(f"savatchada {taom} bor ")
#         else:
#             print(f"bunday {taom} yo'q ")
# else:
#      print("savatcha bo'sh")

# 4------------------------------------------------------------------------------------

# narh = 10000
# choy = 0
# suv = 1
# if choy and suv:
#     narh += 4000
# elif choy or suv:
#     narh += 2000
# print(f"jami {narh} so'm")

# 5-----------------------------------------------------------------------------------

# son=float(input("son kiriting>>>"))
# if son % 2:
#     print(f"{son} sonimiz toq")
# else:
#     print(f"{son} sonimiz juft")

# ---------------------------------------------------------------------------------------
#       UYGA VAZIFA
# 1--------------------------------------------------------------------------------------

savdo=int(input("sotib oladigan mahsulotingizni sonini kiriting>>>"))
bor=['asal','shakar','non','piyoz']
bor_narsalar = []
mavjud_emas = []
for i in range(savdo):
    bor_narsalar.append(input(f"{i+1}-mahsulotni kiriting"))
    if not bor!=savdo:
        print(f"do'konimizda bu narsalar yo'q {i} ")
    elif savdo==bor:
        print("hamma narsa bor")
print(bor_narsalar)
print(mavjud_emas)
# 2---------------------------------------------------------------------------

# royhat=['ali','vali','hasan','husan']
# login_kirit=input("yangi login kiriting>>")
# if login_kirit not in royhat:
#     print("salom foydalanuvchi")
# else:
#     print("bunday login bor boshqasini tanlang")

# 3--------------------------------------------------------------------------------------------

# son=int(input("son kiriting>>>"))
# for son2 in range(1,son):
#     if son2 % 2:
#         print(f" {son2} qoldiqli bo'linadi  ")
#     else:
#         print(f" {son2} ga qoldiqsiz bo'linadi")

# 4---------------------------------------------------------------------------------------

# a=int(input("juft son kiriting>>"))
# if a % 2:
#     print("juft emas")
# else:
#     print("rahmat")

# 5---------------------------------------------------------------------------------------

# a=int(input("1-yoshingizni kiriting:"))
# b=int(input("2-yoshingizni kiriting:"))
# if not a>=10:
#     print("sizga kirish 5000 so'm")
# elif a<=25:
#     print("sizga kirish 10000 so'm")
# else:
#     print("sizga kirish 15000 so'm")

# 6----------------------------------------------------------------------------

# a=int(input("1- sonni kiriting:"))
# b=int(input("2- sonni kiriting:"))
# if  a==b:
#     print(f"{a} = {b}")
# elif a<b:
#     print(f"{a} < {b}")
# else:
#     print(f"{a} > {b}")






















