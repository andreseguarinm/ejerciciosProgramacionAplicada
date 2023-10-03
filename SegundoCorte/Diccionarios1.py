sensor = {"living room":21,"bedroom":20,"kitchen":23,"pantry":22}
print(sensor)
#Es válido que los argumentos sean listas, pero no es válido que 
#las palabras clave sean listas. Por ejemplo:
#powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
#print(powers)

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

my_empty_dictionary =  {}
print(my_empty_dictionary)

#Se pueden agregar elementos a las listas
animals_in_zoo = {"zebras":8,"monkeys":12}
print("antes:", animals_in_zoo)
animals_in_zoo["dinosaurs"]=0
print("despues",animals_in_zoo)
animals_in_zoo = {"horses":2}
print("muy despues: ", animals_in_zoo)

#también se pueden agregar palabras clave:

sensor.update({"mesas":5,"habitaciones":8})
print(sensor)

#además, se pueden actualizar valores

menu = {"cafe":5,"Sandwich":10,"pie":5}
print("antes: ", menu)
menu["cafe"]=8
print("después: ", menu)

#Podemos crear diccionarios a partir de dos listas

nombres = ['Jenny','Alexis','Sam','Grace']
print(nombres)
alturas = [61,70,67,64]
print(alturas)

#con el siguiente comando se crea nuestra lista:

estudiantes = {key:value for key, value in zip(nombres,alturas)}
print(estudiantes)
#El comando zip combina ambas listas

# #zip() combina dos listas en un iterador de tuplas con los elementos de la lista emparejados. Este dictado de comprensión:

drinks = ["espresso", "chai", "decaf", "drip"]
print("Bebidas: ",drinks)
caffeine = [64, 40, 0, 120]
print("Cantidad de cafeína: ", caffeine)

zipped_drinks = zip(drinks, caffeine)
print("Dirección de las bebidas: ", zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print("Bebidas y cantidad de cafeína: ",drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
print("Lista de canciones: ", songs)
playcounts = [78, 29, 44, 21, 89, 5]
print("Recuentos: ", playcounts)
plays = {key:value for key, value in zip(songs, playcounts)}
print("Lista de canciones y su recuento: ",plays)

#A continuación se agregará un nuevo elemento al diccionario:
plays.update({"Purple Haze": 1})

#A continuación, se actualizará el recuento de la canción "Respect":
plays.update({"Respect": 94})
print("Después: ", plays)

#A continuación, se creará un diccionario que contiene diccionarios:
library = {"Las mejores canciones": plays, "Sentimientos domingueros": drinks_to_caffeine}
print(library)