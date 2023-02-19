class Godzina_i_Data:

    def __init__(self, rok, miesiac, dzien, godzina, minuta, sekunda):
        self.rok = rok
        self.miesiac = miesiac
        self.dzien = dzien
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def __str__(self):
        return f'Data: {self.rok}-{self.miesiac}-{self.dzien}, Godzina: {self.godzina}:{self.minuta}:{self.sekunda}'


czas = Godzina_i_Data(2023, 2, 4, 8, 40, 15)
print(czas)
