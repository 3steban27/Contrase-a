import random

Elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitude = int(input(" Introduzca la longitud de la contraseña"))
password = ""

for i in range(longitude):
    password = password + random.choice(Elementos)

print(password)
