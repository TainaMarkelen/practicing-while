if __name__ == '__main__':
    tamanho = int(input("Informe o tamanho da sequência: "))
    
    produto = 1
    i = 0
    
    while i < tamanho:
        valor = int(input("Digite um valor a ser multiplicado: "))
        produto = produto * valor
        i = i + 1
    
    print("O produto dos valores digitados é", produto)