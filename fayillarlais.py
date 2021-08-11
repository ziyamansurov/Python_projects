#
# companyPSWRD='Ziyacmpny@@!!2330'
# adminpswrd=input('admin kodunuzu yaradin: ')
#
# def qiymethesabla(setr):
#     setr = setr[:-1]
#     listecevrmk = setr.split(':')
#     telebeadi = listecevrmk[0]
#     telebeqiymeti = listecevrmk[1].split(',')
#     qiy1 = int(telebeqiymeti[0])
#     qiy2 = int(telebeqiymeti[1])
#     qiy3 = int(telebeqiymeti[2])
#     ortalama = (qiy1 + qiy2 + qiy3) / 3
#
#     if 90 < ortalama <= 100:
#         qiymet = "AA"
#     elif 85<=ortalama<=89:
#         qiymet = "BA"
#     elif ortalama >= 65:
#         qiymet = 'CC'
#     else:
#         qiymet = 'FF'
#     print(telebeadi+': '+qiymet)
#     return telebeadi+': '+qiymet
#
#
#
# def qiymet_gosderen():
#     with open('qiymetler.txt', 'r', encoding='utf-8') as file:
#         for setr in file:
#             qiymethesabla(setr)
#
#
# def qiymet_yazan():
#     ad = input("adinizi yazin: ")
#     soyad = input("soyadiniziz yazin: ")
#
#     qiy1 = input("1-ci qiymetiniziz yazin: ")
#     qiy2 = input("2-ci qiymetiniziz yazin: ")
#     qiy3 = input("3-cu qiymetiniziz yazin: ")
#     ortalama=int(qiy1+qiy2+qiy3)/3
#     if ortalama<=100:
#
#         with open("qiymetler.txt", 'a', encoding='utf-8') as file:
#             file.write(ad + ' ' + soyad + ':' + qiy1 + ',' + qiy2 + ',' + qiy3 + '\n')
#     else:
#         print('Qiymetler elave edile bilmedi duzgun daxil edilmemisdir')
#
# def qiymet_saveeden():
#     with open("qiymetler.txt",'r',encoding='utf-8') as file:
#         saver=[]
#         for i in file:
#             saver.append(qiymethesabla(i))
#         with open('neticeler.txt','w',encoding='utf-8') as file1:
#             for i in saver:
#                 file1.write(i+'\n')
#
# def createPSW():
#
#           for i in range(0,5):
#             check = input('ZiyaCompany parlounu yazin...')
#             if check==companyPSWRD:
#                 global adminpswrd
#                 adminpswrd=input("\nyeni kodunuzuz yaradin: ")
#                 print("kod muveffeqiyetle yaradildi")
#                 break
#
#
#             else:
#                 print(f'Kod yalnisdir {4-i} haqqiniz qaldi')
#
#
#
#
#
# def checkpasswrd(pswrd):
#     if pswrd==adminpswrd:
#        return True
# def netice_del():
#     with open('neticeler.txt','w',encoding='utf-8') as file:
#         file.write('')
#
# def qiymet_del():
#     with open('qiymetler.txt', 'w', encoding='utf-8') as file:
#         file.write('')
#
# if checkpasswrd(input("admin kodunuzu yazin: ")):
#     while True:
#
#         sorgu = input(''
#                       'qiymetlere baxmaq ucun 1\n'
#                       'ad soyad qiymet elave etmek ucun 2\n'
#                       'neticeleri yadda saxlamaq ucun 3\n'
#                       'qiymetleri silmek ucun 4\n'
#                       'neticeleri silmek ucun 5\n'
#
#                       'cixmaq uxun 6\n')
#
#         if sorgu == '1':
#             qiymet_gosderen()
#         elif sorgu == '2':
#             qiymet_yazan()
#         elif sorgu == '3':
#             qiymet_saveeden()
#         elif sorgu=='4':
#             qiymet_del()
#         elif sorgu=='5':
#             netice_del()
#         else:
#             break
# else:
#         print('Kod sehvdir')
#         print('yeni kod yaratmaq isdeyirsinizse b duymesine basin cixmaq ucunse e')
#         sorgu1=input()
#         if sorgu1=='b':
#
#            if createPSW()==True:
#                pass
#
#
#         else:
#             print("ZiyaCompany secdiyiniz ucun tesekkurler")
#
a={211,33,1}
b={5,6,2}
print(a|b)