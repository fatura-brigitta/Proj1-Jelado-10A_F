from jelek import Jelek


class Megoldas:
    _jelek: list[Jelek] = []

    @ property
    def első_utolsó_között_mspben(self) -> int:
        return self.eltelt(self._jelek[0].idő_mspercben, self._jelek[-1].idő_mspercben)
    
    @ property
    def mspből_óra(self) -> int:
        return round(self.első_utolsó_között_mspben / 3600)

    @ property
    def maradék_perc(self) -> int:
        return round((self.első_utolsó_között_mspben - self.mspből_óra) / 60)

    @ property
    def maradék_msperc(self) -> int:
        return self.első_utolsó_között_mspben - self.mspből_óra - self.maradék_perc

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
