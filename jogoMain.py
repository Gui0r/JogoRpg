class MageOfAddition:
    def add(self, a, b):
        return a + b

class WarriorOfSubtraction:
    def subtract(self, a, b):
        return a - b

class RangerOfMultiplication:
    def multiply(self, a, b):
        return a * b

class ClericOfDivision:
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Divisão por zero não permitida!"

# Criação dos objetos (heróis)
mage = MageOfAddition()
warrior = WarriorOfSubtraction()
ranger = RangerOfMultiplication()
cleric = ClericOfDivision()

# Resolver o enigma mágico
# Substituam as variáveis x1, x2, x3, x4, x5 pelos valores apropriados para cada fórmula

resultado = warrior.subtract(cleric.divide(ranger.multiply(mage.add(10, 5),4),2),3)
print(resultado)

resultado2 = warrior.subtract(cleric.divide(mage.add(ranger.multiply(8, 3),7),5),2)
print(resultado2) 

resultado3 = mage.add(ranger.multiply(cleric.divide(warrior.subtract(25, 5),4), 6), 10)
print(resultado3)  

resultado4 = mage.add(ranger.multiply(cleric.divide(warrior.subtract(2, 4), 9), 3), 5)
print(resultado4)         

# Bem loco



"""
adicao multiplicacao divisao e subtração
Resultado = (x1+x2)*x3 -x5
               x4
Inputs:
x1 = 10
x2 = 5
x3 = 4
x4 = 2
x5 = 3

13
40
"""
