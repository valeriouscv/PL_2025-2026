#somatorio de n-primeiros numeros
# numero fornecido pelo utilizador
n = int(input("indique um numero: "))
soma = 0
#for i in range(1, n + 1):
#    soma += i
#print("somatorio: ",soma)

i=1
while i<= n:
    soma = soma + i  # soma += i
    i = i + 1        # i += 1
print("somatorio: ",soma)
