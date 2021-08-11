hesapA = {
    'ad': 'Ziya'
    , 'hesabNO': '1234567'
    , 'pul': 400,
    'exhesab': 6000,
    'hesabkod': 1234
}

hesabB = {
    'ad': 'Ferid'
    , 'hesabNO': '1294567'
    , 'pul': 800,
    'exhesab': 4000
    , 'hesabkod': 1243

}
bankfaiz = 0


def pul_cek(hesab, miqdar):
    hesabkodu = int(input('kodunuzu yazin... '))

    if hesabkodu == hesab["hesabkod"]:
        print(f'Xos geldiniz {hesab["ad"]} ')

        if hesab['pul'] >= miqdar:
            hesab['pul'] -= miqdar
            print('pulunuzu ala bilersiniz')
            hesabde(hesab)
        else:
            toplam = hesab['pul'] + hesab['exhesab']
            if toplam > miqdar:
                exhesabisledilsin = input('hesabinizda lazimi qeder pul yoxdur ekstra hesab isledilsin? (b/x):  ')
                if exhesabisledilsin == 'b':
                    exhesabpulu = miqdar - hesab['pul']
                    hesab['pul'] = 0
                    hesab['exhesab'] -= exhesabpulu
                    print(f'pulunuzu ala bilersiniz.')
                    hesabde(hesab)

            else:
                print('pulunuz yeterli deyil...')
                print('hesaba pul kocurmek ucun 1 ekstra hesaba pul kocurmek ucun 2 ye basin')
                sorqu = int(input(""))
                if sorqu == 1:
                    mebleq = int(input("meblegi qeyd edin..."))
                    hesab['pul'] += mebleq
                else:
                    mebleq = int(input("meblegi qeyd edin..."))
                    global bankfaiz
                    bankfaiz = bankfaiz + (mebleq / 100)
                    mebleq -= bankfaiz
                    hesab['exhesab'] += mebleq
                    print(f'hesabinizdan {bankfaiz} azn faiz tutuldu')
    else:

        print('yalnis sifre...')


def hesabde(hesab):
    print(
        f'{hesab["hesabNO"]} nolu hesabda  {hesab["pul"]} azn pul  ekstra hesabdaysa  {hesab["exhesab"]} azn pul var ')


pul_cek(hesapA, 120)

print("*" * 50)

print(hesapA)
print(bankfaiz)
