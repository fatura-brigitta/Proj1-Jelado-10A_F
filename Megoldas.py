from Jelek import Jelek


class Megoldas:
    _jelek: list[Jelek] = []

    def __init__(self, állomány_neve: str):
        self._jelek = []
        with open(állomány_neve, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines():
                self._jelek.append(Jelek(sor))

    def x_kordináta_keres(self, sorszám: int) -> int:
        index = sorszám - 1
        return self._jelek[index].x_kord

    def y_kordináta_keres(self, sorszám: int) -> int:
        index = sorszám - 1
        return self._jelek[index].y_kord

    def eltelt(self, első_idő: int, második_idő: int) -> int:
        return második_idő - első_idő
