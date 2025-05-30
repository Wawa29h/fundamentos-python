
x = input('Escribe tus datos')


x = x.split()
aux = []


for i in x:
  if i not in aux:
    aux.append(i)

text = ' '.join(aux)
print(text)

