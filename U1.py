#--El IF debe llevar una identación en su argumento

friend = "Rolf"
user_name = input("Enter your name ")

if user_name == friend:
    print("Hello, friend")
    print("This also run")
else:
    print("Hello, stranger")

#--importante conocer el --in--
#--example

friends = ["Rolf", "Alex", "Pao"]
family = ["Gera", "Jacob", "Leo"]

user_name = input("Enter a name ")

if user_name in family:
    print("Hello, family!")
elif user_name in friends:
    print("Hello, friend")
else:
    print("I don't know you")

#-- Vamos a revisar While Loop
#-- Se utiliza cuando queremos repetir algo un número ind. de veces

user_input = input("Do you wanna run the program? (yes/no): ")
while user_input == "yes":
    print("We are running")
    user_input = input("Do you wanna run the program? (yes/no): ")

print("We stopped running")

#-- FOR Loop: it is used to repeat something a defined number of times

friends = ["rolf", "jen", "anne"]

for friend in friends:
    print(friend)

for index in range(5,10):
    print("Hola")