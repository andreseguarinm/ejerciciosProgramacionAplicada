dict1 = {'color':'azul','forma':'circulo'}
dict2 = {'color':'rojo','numero':42}
print(dict1)
dict1.update(dict2)
print('después',dict1)
print(dict1.keys()) # imprime solo los argumentos o encabezados, que son "color", "forma" y "numero".
print(dict1.values()) #imprime solo los valores de los argumentos, que son "rojo", "circulo" y "42".
print(dict1.items()) #imprime todos los datos como tuplas, o sea ('color','rojo'), ('forma','circulo'), ('numero',42)


