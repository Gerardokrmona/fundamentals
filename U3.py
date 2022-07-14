#-- ELSE with loops

cars = ["ok","ok", "ok", "faulty"]

for status in cars:
        if status == "faulty":
                print(f"Stopping the production line")
                break
        print(f"This car is {status}")
        print("Shipping new car to customer")

#-- Si quiero imprimir algo en caso de que todo salga bien
#-- ¿Que debo hacer? para ello se ocupa un else al nivel del for

for status in cars:
        if status == "faulty":
                print(f"Stopping the production line")
                break
        print(f"This car is {status}")
        print("Shipping new car to customer")
else:
    print("All cars built successfully. No faulty cars")

#-- El else solo se corre si no hubo errores o algún break
#-- Haremos un programa que encuentra número primos del 1 al 10

for n in range(2,100):
    for x in range(2,n):
        if n % x ==0:
            break
    else:
        print(f"{n} is prime")

#-- SLICING  es el proceso de obtener la parte de una lista
#-- o de algún iterable

friends = ["rolf", "paola", "ricardo", "hugo","luis","enrique"]
print(friends[:4])
print(friends[2:])

#-- Poner NEGATIVOS indica un conteo al reves empezando con 1

print(friends[-4:-1])

#-- LIST COMPREHENSION: Es una característica de Python para crear
#-- nuevas listas de forma versatil

numbers = [0,1,2,3,4]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number*2)
print(doubled_numbers)

#-- Veamos a continuación el list comprehension

doubled_numbers2 = [number*2 for number in numbers]
print(doubled_numbers2)

friends = ["rolf", "paola", "ricardo", "hugo","luis","enrique"]
friends_upper =[name.upper() for name in friends]
print(friends_upper)

#-- podemos usar los atributos .lower(), .upper(),  .title()
#-- List Comprehension with conditionals

ages = [22,35,27,20,25]
odds = [age for age in ages if age % 2 == 1]
print(odds)

friends = ["Rolf", "ruth", "charlie", "jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

lower_friends = [f.lower() for f in friends]

present_friends = [name.title() for name in guests if name.lower() in lower_friends]
print(present_friends)


#-- Se puede usar lo mismo con los CONJUNTOS y DICCIONARIOS

friends = ["Rolf", "ruth", "charlie", "jen"]
guests = ["jose", "Bob", "rolf", "Charlie", "michael"]

friends_set = {f.lower() for f in friends}
guests_set= {g.lower() for g in guests}
presentes = {p.title() for p in guests_set.intersection(friends_set)}
print(presentes)

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3,7,15,11]

long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}
print(long_timers)