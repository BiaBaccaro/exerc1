class Estudante:
    
    def __init__(self, nome):
        self.nome = nome
        self.notas = [0] * 4

    def adicionar_nota(self, bimestre, nota):
        """Adiciona uma nota para o bimestre especificado (1 a 4)."""
        if 1 <= bimestre <= 4:
            self.notas[bimestre - 1] = nota
        else:
            raise ValueError("Bimestre deve estar entre 1 e 4.")

    def calcular_media(self):
        """Calcula a média das notas dos 4 bimestres."""
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        notas_formatadas = ', '.join(f'Bimestre {i+1}: {nota:.2f}' for i, nota in enumerate(self.notas))
        return (
            f'Nome: {self.nome}'
            f'\nNotas: {notas_formatadas}'
            f'\nMédia: {self.calcular_media():.2f}'
        )

if __name__ == "__main__":
    estudante = Estudante("Ana")
    
    estudante.adicionar_nota(1, 7.5)
    estudante.adicionar_nota(2, 8.0)
    estudante.adicionar_nota(3, 6.5)
    estudante.adicionar_nota(4, 9.0)
    
    print(estudante)
