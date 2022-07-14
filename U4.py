#-- The ZIP FUNCTION : crea una lista de tuples usando sus argumentos
#-- no lo puedes imprimir así nadamás debes darle un dict, list
#-- Ignora los elementos que no hagan match con las demás listas


friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3,7,15,11]

long_timers = dict(zip(friends, time_since_seen))
new_list = list(zip(friends, time_since_seen, [0,1,2,3,4,5]))
print(long_timers)
print(new_list)

print(zip(friends, time_since_seen))

#-- ENUMERATE FUNCTION : asigna un número a una lista dada

friends = ["Rolf", "John", "Anna"]

for counter, name in enumerate(friends, start=1):
    print(counter)
    print(name)

print(list(enumerate(friends)))
