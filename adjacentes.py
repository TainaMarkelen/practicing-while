if __name__ == '__main__':
    adjacentes = False
    last_remainder = 0
    remainder = -1
    
    valor = int(input("Digite uma sequência de números: ")) # ex: 1567889
    
    # o código verifica se existem dois ou mais valores iguais, um seguido do outro, na sequência informada
    while valor > 0:
        last_remainder = remainder
        remainder = valor % 10
        valor = valor // 10
        if remainder == last_remainder:
            adjacentes = True     
    if adjacentes:
        print("sim")
    else:
        print("não")
    