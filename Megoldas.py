from Jelek import Jelek


class Megoldas:
    _jelek: list[Jelek] = []

    def __init__(self, állomány_neve: str):
        self._jelek = []
        with open(állomány_neve, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines():
                self._jelek.append(Jelek(sor))
