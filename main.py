from Megoldas import Megoldas


def main() -> None:
    # 1. feladat
    mo: Megoldas = Megoldas('jel.txt')

    # 2. feladat
    print('2. feladat')
    try:
        jel_input: int = int(input('Adja meg a jel sorszámát! '))
    except ValueError:
        print('A sorszámnak egy 0-nál nagyobb egész számnak kell lennie')
        jel_input: int = int(input('Adja meg a jel sorszámát! '))

    print(f'x={mo.x_kordináta_keres(jel_input)} y={mo.y_kordináta_keres(jel_input)}\n')

    # 4. feladat
    print('4. feladat')
    print(f'Időtartam: {mo.mspből_óra}:{mo.maradék_perc}:{mo.maradék_msperc}\n')

    # 5. feladat
    print('5. feladat')
    print(f'Bal alsó: {mo.bal_also_x_keres} {mo.bal_also_y_keres}, jobb felső: {mo.jobb_felso_x_keres} {mo.jobb_felso_y_keres}\n')

    # 6. feladat
    print('6. feladat')
    print(f'Elmozdulás: {mo.táv_pontok_közt} egység\n')

    # 7. feladat
    print('7. feladat')
    print('kimaradt.txt')
    állomány: str = 'kimaradt.txt'
    mo.kimaradtak_kigyujtese(állomány)


if __name__ == "__main__":
    main()
