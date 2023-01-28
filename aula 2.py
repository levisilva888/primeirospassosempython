a = 10
b = 5
soma = a + b
print (soma)
subtracao = a - b
multiplicacao = a * b
divisao = a / b
print (soma)
print (subtracao)
print (multiplicacao)
print (divisao)
print (f'soma: {soma}. \nSubtração: {subtracao}. '
       '\nMultiplicação: {multiplicacao}'
       '\nDivisão: {divisao}'.
       format(soma=soma,
              subtracao=subtracao,
              multiplicacao=multiplicacao,
              divisao=divisao))
