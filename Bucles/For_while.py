#Bucles o iteradores
#FOR

alimentos = ["manzanas","pan","queso","leche","platano"]

for todos_alimentos in alimentos:
    if todos_alimentos == "queso":
        #continue # hace continuar el codigo, ignoranco el valor encontrado (queso)
        break # hace un pare en el codigo
        #print("tienes que comprar leche")
    print(todos_alimentos)

print("============================================================================")

num = (1, 8)
for number in num:
    print(number) #nuetra de uno al 8

print("============================================================================")

range (1, 8)
for number in range(1,8):
    print(number) #nuetra de uno al 8

print("============================================================================")

for letra in "brian":
    print(letra) #nuetra de uno al 8

print("============================================================================")
print("Comienzo")
for i in [0,1,2]:
    print("Hola ", end="")
print()
print("Final")