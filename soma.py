if __name__ == '__main__':
    soma = 0
    valor = ()
    print("Digite uma sequência de números, quando desejar parar, digite 0.")
    
    while valor != 0:
        valor = int(input("Digite um valor a ser somado: "))
        soma = soma + valor
    print("A soma dos valores digitados é", soma)