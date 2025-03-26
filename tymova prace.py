def scitani(cislo1, cislo2):
    print(cislo1+cislo2)

def odcitani(cislo1, cislo2):
    print(cislo1-cislo2)

def nasobeni(cislo1, cislo2):
    print(cislo1*cislo2)

def deleni(cislo1, cislo2):
    print(cislo1/cislo2)


opakovat = "ano"

while(opakovat=="ano"):


    cislo1 = int(input("Zadejte první číslo: "))
    cislo2 = int(input("Zadejte druhé číslo: "))

    print("Vyberte početní operaci(pište pouze číslo): ")
    print("1. sčítání")
    print("2. odčítání")
    print("3. násobení")
    print("4. dělení")

    cislo=int(input())

    if cislo==1:
        scitani(cislo1,cislo2)

    elif cislo==2:
        odcitani(cislo1, cislo2)

    elif cislo==3:
        nasobeni(cislo1, cislo2)

    elif cislo==4:
        deleni(cislo1, cislo2)

    opakovat = input("Chcete opakovat program?(ano/ne)")