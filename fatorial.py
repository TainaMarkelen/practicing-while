if __name__ == '__main__':
    contagem = 1
    mult = 1
    valor = int(input("Informe um valor: "))
    
    while valor > 1:
        mult = mult * valor
        valor = valor - 1
    print(mult)
        