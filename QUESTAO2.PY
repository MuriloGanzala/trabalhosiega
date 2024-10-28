class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, item):
        self.pilha.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.pilha.pop()
        return None

    def esta_vazia(self):
        return len(self.pilha) == 0


def eh_palindromo(string):
    pilha = Pilha()
    # Normalizar a string, removendo espaços e convertendo para minúsculas
    string = string.replace(" ", "").lower()
    
    # Empilhar a primeira metade da string
    for i in range(len(string) // 2):
        pilha.empilhar(string[i])

    # Determinar o ponto de início para comparar a segunda metade
    start = (len(string) // 2) + (len(string) % 2)

    # Comparar a segunda metade da string com os itens desempilhados
    for i in range(start, len(string)):
        if string[i] != pilha.desempilhar():
            return False
    return True


# Teste
entrada = input("Digite uma palavra para verificar se é um palíndromo: ")
if eh_palindromo(entrada):
    print(f"'{entrada}' é um palíndromo!")
else:
    print(f"'{entrada}' não é um palíndromo.")
