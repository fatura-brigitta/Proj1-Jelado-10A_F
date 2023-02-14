from math import sqrt
from math import floor
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
    def táv_pontok_közt(self) -> float:
        elmozdulas: list[float] = []
        for i, e in enumerate(self._jelek):
            if i == len(self._jelek) - 1:
                break
            elmozdulas.append(sqrt((e.x_kord - self._jelek[i + 1].x_kord)**2 + (e.y_kord - self._jelek[i + 1].y_kord)**2))
        return round(sum(elmozdulas), 3)

    @property
    def elmozdulás_összesen(self):
        összesen = 0
        for i in range(len(self._jelek) - 1):
            összesen += self.táv_pontok_közt(self._jelek[i], self._jelek[i + 1])
        return összesen

    def kimaradtak_ido_szerint(self) -> list[Jelek]:
        kimaradtak_ido_szerint: list[Jelek] = []
        for i, jel in enumerate(self._jelek):
            if self.eltelt(jel.idő_mspercben, self._jelek[i + 1].idő_mspercben) > 300:
                kimaradtak_ido_szerint.append(self._jelek[i + 1])
        return kimaradtak_ido_szerint

    def kimaradtak_tav_szerint(self) -> list[Jelek]:
        kimaradtak_tav_szerint: list[Jelek] = []
        for i, jel in enumerate(self._jelek):
            x_ek_abs: int = abs(self._jelek[i + 1].x_kord - jel.x_kord)
            y_ok_abs: int = abs(self._jelek[i + 1].y_kord - jel.y_kord)
            távolság: int = int(max(x_ek_abs, y_ok_abs))
            if távolság > 10:
                kimaradtak_tav_szerint.append(self._jelek[i + 1])
        return kimaradtak_tav_szerint

    def kiiras(self, állomány_neve: str):
        with open(állomány_neve, 'w', encoding='utf-8') as file:
            file.write()

    # @property
    # def kimaradtak_ido_szerint(self) -> int:
    #     kimaradtak_ido_szerint = 0
    #     for index in range(len(self._jelek) - 1):
    #         időkülönbség: int = int(self.eltelt(self._jelek[index].idő_mspercben, self._jelek[index + 1].idő_mspercben))
    #         if időkülönbség > 300:
    #             kimaradtak_ido_szerint: int = int((időkülönbség - 1) // 300)
    #     return int(kimaradtak_ido_szerint)

    # @property
    # def kimaradtak_koordinata_szerint(self) -> int:
    #     kimaradtak_kord_szerint = 0
    #     for index in range(len(self._jelek) - 1):
    #         x_ek_abs: int = abs(self._jelek[index + 1].x_kord - self._jelek[index].x_kord)
    #         y_ok_abs: int = abs(self._jelek[index + 1].y_kord - self._jelek[index].y_kord)
    #         távolság: int = int(max(x_ek_abs, y_ok_abs))
    #         if távolság > 10:
    #             kimaradtak_kord_szerint = (távolság - 1) // 10
    #     return int(kimaradtak_kord_szerint)

    # def kimaradtak_lista(self, jel):
    #     kimaradt_ido_szerint_list: list[Jelek] = []
    #     for jel in self._jelek:
    #         if self.kimaradtak_ido_szerint() > self.kimaradtak_koordinata_szerint()

    # def kimaradtak(self, fájl: str):
    #     with open(fájl, 'w', encoding='utf-8') as file:
    #         for i, e in enumerate(self._jelek):
    #             kimaradas_ido: int = int()
    #             kimaradas_kord: int = int(self.kimaradtak_koordinata_szerint(self._jelek[index]))
    #             if kimaradas_ido > kimaradas_kord:
    #                 file.write(f'{self._jelek[index + 1].óra} {self._jelek[index + 1].perc} {self._jelek[index + 1].másodperc} időeltérés {self.kimaradtak_ido_szerint()}')

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
