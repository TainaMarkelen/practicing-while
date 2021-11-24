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
    
    if n == 1 or not primo:   
        print("não primo")
    else:
        print("primo")
            
    


        