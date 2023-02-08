from math import floor
import math
from jelek import Jelek


class Megoldas:
    _jelek: list[Jelek] = []

    @ property
    def első_utolsó_között_mspben(self) -> int:
        return self.eltelt(self._jelek[0].idő_mspercben, self._jelek[-1].idő_mspercben)

    @ property
    def mspből_óra(self) -> int:
        return floor(self.első_utolsó_között_mspben / 3600)

    @ property
    def maradék_perc(self) -> int:
        return floor((self.első_utolsó_között_mspben - self.mspből_óra * 3600) / 60)

    @ property
    def maradék_msperc(self) -> int:
        return self.első_utolsó_között_mspben - self.mspből_óra * 3600 - self.maradék_perc * 60

    @property
    def bal_also_x_keres(self) -> int:
        legkisebb_x = self._jelek[0].x_kord
        for jel in self._jelek:
            if jel.x_kord < legkisebb_x:
                legkisebb_x = jel.x_kord
        return legkisebb_x

    @property
    def bal_also_y_keres(self) -> int:
        legkisebb_y = self._jelek[0].y_kord
        for jel in self._jelek:
            if jel.y_kord < legkisebb_y:
                legkisebb_y = jel.y_kord
        return legkisebb_y

    @property
    def jobb_felso_x_keres(self) -> int:
        legnagyobb_x = self._jelek[0].x_kord
        for jel in self._jelek:
            if jel.x_kord > legnagyobb_x:
                legnagyobb_x = jel.x_kord
        return legnagyobb_x

    @property
    def jobb_felso_y_keres(self) -> int:
        legnagyobb_y = self._jelek[0].y_kord
        for jel in self._jelek:
            if jel.y_kord > legnagyobb_y:
                legnagyobb_y = jel.y_kord
        return legnagyobb_y

    @property
    def tav(self) -> list[float]:
        asd: list[float] = []
        for i, e in enumerate(self._jelek):
            # math.sqrt((e.x_kord[i] - e.x_kord[i + 1])**2 + (e.y_kord[i] - e.y_kord[i + 1])**2)
            asd.append(round(math.sqrt((e.x_kord - self._jelek[i + 1].x_kord)**2 + (e.y_kord - self._jelek[i + 1].y_kord)**2), 3))
            if i == 249:
                break
        new_list = sum(asd)
        return new_list

        

    @property
    def elmozdulás_összesen(self):
        összesen = 0
        for i in range(len(self._jelek)-1):
            összesen += self.táv_pontok_közt(self._jelek[i], self._jelek[i+1])
        return összesen


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
