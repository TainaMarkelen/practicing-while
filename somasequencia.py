if __name__ == '__main__':
    soma = 0
    
    valor = int(input("Digite uma sequência de números: ")) # ex: 122
    
    while valor > 0:
        resto = valor % 10
        valor = valor // 10       
        soma = soma + resto
    print(soma)
        