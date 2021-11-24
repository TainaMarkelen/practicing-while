if __name__  == '__main__':
    n = int(input("Digite o valor de n: "))
    quantidade = 0
    i = 0
    
    while quantidade != n:
        i += 1
        if i % 2 != 0:
            print(i)
            quantidade += 1
            
        