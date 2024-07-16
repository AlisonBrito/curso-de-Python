first_name = input('Por favor, digite seu nome: ') #string 
age = int(input('Agora, digite sua idade: ')) #integer

#Formas de imprimir no console 
print('Olá {}! Você tem {} anos'.format(first_name, age))
#ou 
print('Olá,', first_name, '! Você tem', age, 'anos')
#ou 
print(f'Olá, {first_name}! Você tem {age} anos')
