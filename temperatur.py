def convCtoF(Celcius):
    Fahrenheit = int(Celcius) * 9 / 5 + 32
    return Fahrenheit

def convFtoC(Fahrenheit):
    Celcius = (int(Fahrenheit) - 32) * 5 / 9
    return Celcius

f = input("enter temperatur in Fehrenheit: ")
c = convFtoC(f)

print(f"your temperatur in Caelcius is: {c:.2f}")

c = input("enter a tmperatur in Celcius: ")
f = convCtoF(c)
print(f"your temperatur in Fahrenheit is: {f:.2f}")
