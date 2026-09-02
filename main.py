from klasser import Allmän
from klasser import Chefer

personal = {}
avdelningar = []
manager = {}

while True:
    avdelning = input("Lägg till avdelningar (eller skriv'klar': )")
    if avdelning.lower() == "klar":
        break
    avdelningar.append(avdelning)
print("Avdelningar: ", avdelningar)

while True:
    print("Vad vill du göra? ")
    print("1. Lägga till anställd! ")
    print("2. Lägga till avdelningschef")
    print("3. Visa alla anställda")
    print("4. visa information om en specifik anställd")
    print("5. Visa avdelningsschef")
    val = input("Välj ett alternativ: ")
    print(val)

    if val == "1":
        def skapa():
            namn = input("Ange anställdens efternamn: ")
            lön = float(input("Ange anställdens lön: "))
            avdelning = input("Vilken avdelning jobbar anställden i? ")
            person = Allmän(namn, lön, avdelning)

            name = person.namn 
            sal = person.lön 
            dept = person.avdelning 
            return name, sal, dept

        name, sal, dept = skapa()

        if dept not in avdelningar:
            print("Den avdelningen finns inte")
        else:
            personal[name] = {
                "namn": name,
                "avdelning": dept,
                "lön": sal
            }
            for value in personal[name].values():
                print(value)
            print("Anställd har lagts till!")

    elif val == "2":
        def create():
            if len(avdelningar) == 0:
                print("Det finns inga avdelningar inlagda")
                return

            print("Tillgängliga avdelningar:")
            print(avdelningar)

            chef = input("Ange vilken avdelning chefen avser: ")

            if chef not in avdelningar:
                print("avdelningar finns inte. Vänligen välj en befintlig avdelning.")
                return

            meow = input("Ange chefens namn: ")

            return chef, meow
        resultat = create()
        if resultat is not None:
            chef, meow = resultat
            manager[chef] = meow
            print("Avdelningschef har lagts till!")


    elif val == "3":
        if len(personal) == 0:
            print("Det finns inga anställda")
        else:
            for name, information in personal.items():
                print("---------")
                print("Namn :", information["namn"])
                print("avdelningar :", information["avdelning"])
                print("Lön :", information["lön"])

    elif val == "4":
        välja = input("Ange anställdens namn: ")
        if len(personal) == 0:
            print("Inga anställda tillagd!")
        elif välja not in personal:
            print("Denna anställd finns inte. ")
        else: 
            information = personal[välja]
            print("----------")
            print("Name: ", information["namn"])
            print("lön: ", information["lön"])
            print("avdelning: ", information["avdelning"])

    elif val == "5":
    
        if len(avdelningar) == 0: 
            print("Ingen avdelning inlagd")
        else: 
            print(avdelningar)
            välj = input("Ange avdelningars namn: ")

            if välj not in avdelningar: 
                print("Denna avdelning finns inte med i vår databas")
            elif välj not in manager:
                print("Det finns ingen chef registrerad för denna avdelning")
            else:
                print("-----------")
                print("Avdelning: ", välj)
                print("Chef:", manager[välj])
    
                