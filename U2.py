#-- destructuring syntax

# currencies = 0.8, 1.2
# usd, eur = currencies  #Doble asignación

# friends = [("rolf", 25),("anne", 37),("charlie", 31),("bob", 22)]

# for name, age in friends:
#         print(f"{name} is {age} years old.")

#---Iterating over dictionaries
#-- Cuando iteras sobre un diccionario te da las Keys
#-- para obtener los valores usa .values
#-- si deseas trabajar con los dos usa .items

# dictionary = {"juan" : 23, "jesus" : 25, "mich" : 21}
# for name in dictionary:
#         print(f"hola {name}")

# for age in dictionary.values():
#         print(f"age :  {age}")

# for name, age in dictionary.items():
#         print(f"{name} is {age} years old. ")


#--- Break and Continue

cars = ["ok","ok", "faulty", "ok"]

# for status in cars:
#         if status == "faulty":
#                 print(f"Stopping the production line")
#                 break
#         print(f"This car is {status}")

for status in cars:
        if status == "faulty":
                print(f"Found faulty one, skipping")
                continue
        print(f"This car is {status}")
        print(f"shipping new car to customer")
