class Pilha:
	def __init__(self):
		self.item = []

	def push(self, item):
		num1 = (input("Qual numero deseja adicionar ao topo da lista: "))
		self.item.append(item)
		print(f" {[item]} ")

	def pop(self):
		return self.item.pop()

	def peek(self):
		return self.item[-1] if self.item else None

	def is_empty(self):
		return len(self.item) == 0



def main():
	inv = Pilha()
	
	print("\n ---- Menu ----")
	print("1. Adicionar um elemento ao topo da pilha (push) ")
	print("2. remove e retorna o elemento do topo da pilha (pop) ")
	print("3. Retorna o elemento do topo da pilha sem remove-lo (peek) ")
	print("4. Retorna true se a pilha estiver vazia, false se caso contrario (is_empty) ")
	
	rep = int(input(""))
	
	if rep == 1:
		inv.push(inv)
		
		
if __name__ == "__main__":
	main()

		

        
        



"""
Exercício Prático: Simulador de Pilha
Enunciado:
Crie um simulador de pilha utilizando apenas listas em Python. A pilha deve permitir as operações básicas:
push: Adiciona um elemento ao topo da pilha.
pop: Remove e retorna o elemento do topo da pilha.
peek: Retorna o elemento do topo da pilha sem removê-lo.
is_empty: Retorna True se a pilha estiver vazia, False caso contrário.
Adicione uma funcionalidade:
max_size: Define o tamanho máximo da pilha. Se o usuário tentar adicionar um elemento quando a pilha estiver cheia, o programa deve imprimir uma mensagem de erro e não adicionar o elemento.
Crie um programa principal que:
Crie uma pilha com um tamanho máximo definido pelo usuário.
Permita que o usuário realize operações na pilha (push, pop, peek).
Imprima o estado da pilha após cada operação.
Desafio:
Gerenciamento de memória: Certifique-se de que a pilha não ultrapasse o tamanho máximo definido.
Retorno correto: O programa deve sempre retornar o estado correto da pilha, mesmo após operações inválidas.

"""