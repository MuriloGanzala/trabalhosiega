class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.pilha = []

    def empilhar(self, item):
        if len(self.pilha) < self.tamanho:
            self.pilha.append(item)
            print(f"Item '{item}' empilhado com sucesso!")
        else:
            print("Erro: A pilha está cheia. Não é possível empilhar.")

    def desempilhar(self):
        if len(self.pilha) > 0:
            item = self.pilha.pop()
            print(f"Item '{item}' desempilhado com sucesso!")
            return item
        else:
            print("Erro: A pilha está vazia. Não é possível desempilhar.")
            return None

    def topo(self):
        if len(self.pilha) > 0:
            return self.pilha[-1]
        else:
            return None


def main():
    tamanho = int(input("Informe o tamanho da pilha: "))
    pilha = Pilha(tamanho)

    while True:
        print("\nEscolha uma operação:")
        print("a) Empilhar")
        print("b) Desempilhar")
        print("c) Sair")
        opcao = input("Opção: ").lower()

        if opcao == 'a':
            item = input("Informe o item para empilhar: ")
            pilha.empilhar(item)
        elif opcao == 'b':
            pilha.desempilhar()
        elif opcao == 'c':
            topo = pilha.topo()
            if topo is not None:
                print(f"O conteúdo no topo da pilha é: {topo}")
            else:
                print("A pilha está vazia.")
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
