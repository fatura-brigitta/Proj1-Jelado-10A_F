class Jelek:
    _óra: int
    _perc: int
    _másodperc: int
    _x_koordináta: int
    _y_koordináta: int

    @property
    def x_kord(self) -> int:
        return self._x_koordináta

    @property
    def óra(self) -> int:
        return self._óra

    @property
    def perc(self) -> int:
        return self._perc

    @property
    def másodperc(self) -> int:
        return self._másodperc

    @property
    def y_kord(self) -> int:
        return self._y_koordináta

    @property
    def idő_mspercben(self) -> int:
        óra_mspben = self._óra * 3600
        perc_mspben = self._perc * 60
        return óra_mspben + perc_mspben + self._másodperc

    def __init__(self, sor: str) -> None:
        óra, perc, msperc, x_kord, y_kord = sor.split(' ')
        self._óra = int(óra)
        self._perc = int(perc)
        self._másodperc = int(msperc)
        self._x_koordináta = int(x_kord)
        self._y_koordináta = int(y_kord)
