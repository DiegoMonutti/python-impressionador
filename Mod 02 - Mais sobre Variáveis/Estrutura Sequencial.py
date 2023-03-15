'''Lista de Estrutura Sequencial'''

'''1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.'''

print('Alo mundo')

'''2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."'''

while True:
    try:
        numero = float(input('Digite um número: '))
        print(f'O número informado foi {numero}.')
        break
    except ValueError:
        print('Entrada inválida. Tente novamente.')

'''3. Faça um Programa que peça dois números e imprima a soma.'''

numeros = []

while len(numeros) < 2:
    try:
        numero = float(input(f'Por favor informe o {len(numeros) + 1}º número a ser somado: '))
        numeros.append(numero)
    except ValueError:
        print(f'Entrada inválida. Insira o {len(numeros) + 1}º número novamente')
        continue

print(f'A soma dos dois número é de: {sum(numeros)}')

'''4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.'''

def obter_nota(bimestre):
    while True:
        try:
            nota = float(input(f'Digite a nota do {bimestre}º bimestre - entre 0 e 10: '))
            if 0 <= nota <= 10:
                print(f'A nota informada foi: {nota}.')
                return nota
            else:
                raise ValueError
        except ValueError:
            print('Entrada inválida. Insira novamente uma nota entre 0 e 10.')

notas = [obter_nota(i+1) for i in range(4)]
media = sum(notas) / len(notas)
print(f'A média bimestral desse estudante foi de: {media:.2f}')

'''5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).'''

metros = float(input('Insira o valor em metros que será convertido para centímetros: '))

print(f'{(metros*100):.2f}cm.')

'''6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.'''

largura = float(input('Insira a largura da sala em metros: '))
comprimento = float(input('Insira o comprimento da sala em metros: '))

print(f'A área da sala é de: {(largura*comprimento)}m².')

'''7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor = float(input('Informe quanto você ganha por hora trabalhada: '))
horas = int(input('Informe qual o valor do seu salário ganho por hora trabalhada: '))

print(f'Seu salário esse mês será de: R${(valor*horas):.2f}.')

'''8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5/9 * (F-32)'''

fahr = float(input('Informe a temperatura em Fahrenheit: '))

print(f'Essa temperatura equivale a: {(fahr - 32)*(5/9)}°C.')

'''9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = 9/5 * C + 32'''

celsius = float(input('Informe a temperatura em Celsius: '))

print(f'Essa temperatura equivale a: {(celsius*(9/5) + 32)}°F.')

'''10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
P = 72,7h - 58 
Lembrando que "algoritmo" nada mais é do que um programa, como todos os outros que você vem fazendo'''

altura = float(input('Informe sua altura em metros: '))

print(f'Para a altura de {altura:.2f}m, o peso ideal é de {(72.7*altura - 58):.2f}Kg.')

'''11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: P = 72,7h - 58
b. Para mulheres: P = 62,1h - 44,7'''

genero = input('Informe o seu gênero(H para Homens e M para Mulheres): ').upper()

while genero != 'H' and genero != 'M':
    genero = input('Informe o seu gênero(H para Homens e M para Mulheres): ').upper()

altura = float(input('Informe sua altura em metros: '))

if genero == 'H':
    peso = 72.7*altura - 58
else:
    peso = 62.1*altura - 44.7

print(f'Para a altura de {altura:.2f}m, o peso ideal é de {peso:.2f}Kg.')

'''12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.'''

descontos = []
valor = float(input('Informe qual o valor do seu salário ganho por hora trabalhada: '))
horas = int(input('Informe quantas horas você trabalhou esse mês: '))

'''Calcule o salário bruto (horas * salario por hora)'''

sal_bruto = valor*horas
print(f'Seu salário bruto será de: R${sal_bruto:,.2f}.')

'''Calcule o desconto do IR (11% do salário bruto)'''

ir = sal_bruto * 0.11
descontos.append(ir)

print(f'O desconto do imposto de renda será de: R${ir:,.2f}')

'''Calcule o desconto do INSS (8% do salário bruto)'''

inss = sal_bruto * 0.08
descontos.append(inss)

print(f'O desconto do INSS será de: R${inss:,.2f}')

'''Calcule o desconto do sindicato (5% do salário bruto)'''

sindicato = sal_bruto * 0.05
descontos.append(sindicato)

print(f'O desconto do sindicato será de: R${sindicato:,.2f}')

'''Calcule o salário líquido (salário bruto - descontos)'''

sal_liquido = sal_bruto - sum(descontos)

print(f'O seu salário líquido esse mês será de: R${sal_liquido:,.2f}')

'''13. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. (para simplificação nesse momento, não se preocupe em arredondar a quantidade de latas a serem compradas - vamos trabalhar isso em breve)'''

import math

# Constantes:
metro_litro = 3
capacidade_lata = 18
preco_lata = 80

area = float(input('Informe a quantidade em metros quadrados que deverá ser pintada: '))

litros = area/metro_litro

latas = math.ceil(litros/capacidade_lata)

preco = latas * preco_lata

print(f"Serão necessárias {latas} latas de tinta que custarão R${preco:,.2f}")

'''14. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
- Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. '''

tam_arquivo = float(input('Insira o tamanho do arquivo a ser baixado em MB: '))
vel_net = float(input('Insira a velocidade de sua Internet em Mbps: '))

tempo_down = (tam_arquivo * 8) / (vel_net * 60)

print(f"O tempo aproximado de download para esse arquivo é de {tempo_down:.2f} minutos")