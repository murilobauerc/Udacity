'''Escreva uma função hours2days, que tenha como argumento um número inteiro, 
que é um período de tempo em horas. A função deve retornar uma tupla de quanto tempo esse 
período é em dias e horas, sendo as horas o restante, que não pode ser expresso em dias. 
Por exemplo, 39 horas são 1 dia e 15 horas, então, a função deve retornar (1,15).'''

def hours2days(n):
    return n // 24, n % 24
    
    
print (hours2days(24)) # 24 horas e um dia e zero horas
#(1, 0)

print (hours2days(39)) # 39 horas e um dia e quinze horas
# (1,15)

print (hours2days(25)) # 25 horas e um dia e uma hora
#(1, 1)

print (hours2days(10000))
#(416, 16)
