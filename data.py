from datetime import datetime

class Data:
    def __init__(self, dia, mes, ano):
        if not self._data_valida(dia, mes, ano):
            raise ValueError(f"Data inválida: {dia}/{mes}/{ano}")
        
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def _data_valida(self, dia, mes, ano):
        try:
            datetime(ano, mes, dia)
            return True
        except ValueError:
            return False
    
    def __str__(self):
        return f"{self.dia:02}/{self.mes:02}/{self.ano}"
    
    def __repr__(self):
        return f"Data(dia={self.dia}, mes={self.mes}, ano={self.ano})"

try:
    #inválida

    data1 = Data(30, 2, 2024)
    print(data1)
except ValueError as e:
    print(e)

try:
    #válida
    
    data2 = Data(15, 8, 2024) 
    print(data2)
except ValueError as e:
    print(e)
