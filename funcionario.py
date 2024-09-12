class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def set_salario(self, salario):
        self.salario = salario

    def get_salario(self):
        return self.salario
    
    def calcular_desconto(self):
        """Calcula o desconto de INSS baseado na regra fornecida."""
        if self.salario > 5000:
            desconto = self.salario * 0.10
        else:
            desconto = 0
        return desconto 

    def __str__(self):
        return (
            f'Nome: {self.nome}'
            f'\nSalário: R$ {self.salario:.2f}'
            f'\nDesconto de INSS: R$ {self.calcular_desconto():.2f}'
        )

if __name__ == "__main__":
    funcionario = Funcionario("Maria", 6000)
    print("Informações do Funcionário:")
    print(funcionario)

    funcionario.set_salario(4000) 
    print("\nApós alteração do salário:")
    print(funcionario)
