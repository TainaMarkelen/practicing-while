if __name__ == '__main__':
    meu_cartao = int(input("Digite o número do seu cartão: "))
    
    cartao_lido = 1
    encontrei_meu_cartao = False
    
    while cartao_lido != 0 and not encontrei_meu_cartao:
        cartao_lido = int(input("Digite o número do próximo cartão: "))
        if cartao_lido == meu_cartao:
            encontrei_meu_cartao = True
    
    if encontrei_meu_cartao:
        print("Meu cartão está lá!")
    else:
        print("Meu cartão não está lá!")