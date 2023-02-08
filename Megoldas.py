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

    def táv_pontok_közt(self, első_jel: int, második_jel: int) -> float:
        jel1x = self._jelek[első_jel + 1].x_kord
        jel1y = self._jelek[első_jel + 1].y_kord
        jel2x = self._jelek[második_jel + 2].x_kord
        jel2y = self._jelek[második_jel + 2].y_kord
        return math.sqrt((jel2x - jel1x)**2 + (jel2y - jel1y)**2)

    @property
    def elmozdulás_összesen(self):
        összesen = 0
        for i in range(len(self._jelek)-1):
            összesen += self.táv_pontok_közt(self._jelek[i], self._jelek[i+1])


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
