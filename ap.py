nome = str(input('Qual é seu nome? '))
if nome == "layza":
    print('Que nome lindo você tem!')
elif nome == 'pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome')
else:
    print('Seu nome é bem normal.')
print('Bom dia, {}! '.format(nome))