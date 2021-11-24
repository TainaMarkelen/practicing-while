if __name__ == '__main__':
    n = int(input("Digite um número inteiro: "))
    i = 2
    resto = 1
    primo = True
    
    while i < n and primo:  
        resto = n % i
        i += 1
        if resto == 0:
            primo = False       
    print (primo)
