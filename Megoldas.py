from math import sqrt
from math import floor
from jelek import Jel


class Megoldas:
    _jelek: list[Jel] = []

    @property
    def első_utolsó_között_mspben(self) -> int:
        return self.eltelt(self._jelek[0].idő_mspercben, self._jelek[-1].idő_mspercben)

    @property
    def mspből_óra(self) -> int:
        return floor(self.első_utolsó_között_mspben / 3600)

    @property
    def maradék_perc(self) -> int:
        return floor((self.első_utolsó_között_mspben - self.mspből_óra * 3600) / 60)

    @property
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
    def elmozdulás_összesen(self) -> float:
        összesen: float = 0
        for i in range(len(self._jelek) - 1):
            összesen += float(self.táv_pontok_közt(self._jelek[i], self._jelek[i + 1]))  # type: ignore
        return összesen

    def __init__(self, állomány_neve: str):
        self._jelek = []
        with open(állomány_neve, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines():
                self._jelek.append(Jel(sor))

    def x_kordináta_keres(self, sorszám: int) -> int:
        index = sorszám - 1
        return self._jelek[index].x_kord

    def y_kordináta_keres(self, sorszám: int) -> int:
        index = sorszám - 1
        return self._jelek[index].y_kord

    def eltelt(self, első_idő: int, második_idő: int) -> int:
        return második_idő - első_idő

    def távolság_kimaradtakhoz(self, jel_i: Jel, jel_i_meg_egy: Jel) -> int:
        x_kordok_kulonbsege: int = abs(jel_i_meg_egy.x_kord - jel_i.x_kord)
        y_kordok_kulonbsege: int = abs(jel_i_meg_egy.y_kord - jel_i.y_kord)
        tavolsag: int = max(x_kordok_kulonbsege, y_kordok_kulonbsege)
        return tavolsag

    def kimaradtak_ido_szerint(self, jel_1_ido_msp: int, jel_2_ido_msp: int) -> int:
        kimaradt_ido: int = 0
        idokulonbseg: int = self.eltelt(jel_1_ido_msp, jel_2_ido_msp)
        if idokulonbseg > 300:
            kimaradt_ido = (idokulonbseg - 1) // 300
        return kimaradt_ido

    def kimaradtak_tav_szerint(self, jel_1: Jel, jel_2: Jel) -> int:
        kimaradtak_tav: int = 0
        tav = self.távolság_kimaradtakhoz(jel_1, jel_2)
        if tav > 10:
            kimaradtak_tav = (tav - 1) // 10
        return kimaradtak_tav

    def kimaradtak_kigyujtese(self, állomány_neve: str):
        with open(állomány_neve, 'w', encoding='utf-8') as file:
            for i, jel in enumerate(self._jelek):
                if i == 0:
                    continue
                ido_kim: str = f'{jel.óra} {jel.perc} {jel.másodperc} időeltérés {self.kimaradtak_ido_szerint(self._jelek[i - 1].idő_mspercben, jel.idő_mspercben)}'
                tav_kim: str = f'{jel.óra} {jel.perc} {jel.másodperc} koordináta-eltérés {self.kimaradtak_tav_szerint(self._jelek[i - 1], jel)}'
                if self.kimaradtak_ido_szerint(self._jelek[i - 1].idő_mspercben, jel.idő_mspercben) > self.kimaradtak_tav_szerint(self._jelek[i - 1], jel):
                    file.write(f'{ido_kim}\n')
                elif self.kimaradtak_ido_szerint(self._jelek[i - 1].idő_mspercben, jel.idő_mspercben) < self.kimaradtak_tav_szerint(self._jelek[i - 1], jel):
                    file.write(f'{tav_kim}\n')
