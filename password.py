import random
import os
import string

def gerar_senha(num_caracteres):

    abc = string.ascii_letters
    punctuation = string.punctuation
    caracteres = abc + punctuation

    senha = "".join(random.choices(caracteres,k=num_caracteres))
    
    print(senha)

    input("PRESS ENTER TO PASS ")

while True:
    
    os.system('cls')
    num_caracteres = int(input('>>> '))

    if num_caracteres == 0:
        break
    
    gerar_senha(num_caracteres)
