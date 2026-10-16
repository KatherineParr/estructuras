#for es vcuando sabemos cuantas veces se tiene que ejecutar, while es cuadno nno sabesmos cuantas veces, si se logra de una, dos, o mil


#con while
# Con while
numbers = [10, 14, 32, 24, 5]
index = 0
found = None
while index < len(numbers) and found is None:
    if numbers[index] % 7 == 0:
        found = numbers[index]
    index += 1
print(f"Encontrado con while: {found}")