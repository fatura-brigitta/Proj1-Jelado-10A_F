from Megoldas import Megoldas


def main() -> None:
    # 1. feladat
    mo: Megoldas = Megoldas('jel.txt')

    # 2. feladat
    print('2. feladat')
    jel_input: int = int(input('Adja meg a jel sorszámát! '))
    print(f'x={mo.x_kordináta_keres(jel_input)} y={mo.y_kordináta_keres(jel_input)}\n')

    # 4. feladat
    print('4. feladat')
    print(f'Időtartam: {mo.mspből_óra}:{mo.maradék_perc}:{mo.maradék_msperc}')

if __name__ == "__main__":
    main()
