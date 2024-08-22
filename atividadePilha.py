class Pilha:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if len(self.items) >= self.max_size:
            print("Não é possível adicionar mais elementos.")
        else:
            self.items.append(item)
            print(f"O elemento '{item}' foi adicionado")

    def pop(self):
        if len(self.items) == 0:
            print("Não tem elementos para serem removidos!")
        else:
            item = self.items.pop()
            print(f"O elemento '{item}' foi removido da pilha.")
#item = self.items.pop 
    def peek(self):
        if len(self.items) == 0:
            print("A pilha está vazia!.")
        else:
            item = self.items[-1]
            print(f"O elemento no topo da pilha é: '{item}'.")

    def is_empty(self):
        if len(self.items) == 0:
            print("A pilha está vazia.")
        else:
            print("A pilha não está vazia.")

    def display(self):
        if len(self.items) == 0:
            print("A pilha está vazia.")
        else:
            print("Estado atual da pilha:", self.items)


def main():
    tamanho = int(input("Digite o tamanho máximo da pilha: "))
    pilha = Pilha(tamanho)

    while True:
        print("\nMenu de Operações:")
        print("1. Push (Adicionar elemento)")
        print("2. Pop (Remover elemento)")
        print("3. Peek (Ver topo da pilha)")
        print("4. Verificar se a pilha está vazia")
        print("5. Exibir pilha")
        print("6. Sair")

        resposta = input("Escolh uma opção: ")

        if resposta == '1':
            elemento = input("Digite o elemento que deseja adicionar: ")
            pilha.push(elemento)
        elif resposta == '2':
            pilha.pop()
        elif resposta == '3':
            pilha.peek()
        elif resposta == '4':
            pilha.is_empty()
        elif rrsposta == '5':
            pilha.display()
        elif resposta == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida! ")

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