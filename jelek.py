class Jelek:
    _óra: int
    _perc: int
    _másodperc: int
    _x_koordináta: int
    _y_koordináta: int

    def __init__(self, sor: str) -> None:
        óra, perc, msperc, x_kord, y_kord = sor.split(' ')
        self._óra = int(óra)
        self._perc = int(perc)
        self._másodperc = int(msperc)
        self._x_koordináta = int(x_kord)
        self._y_koordináta = int(y_kord)