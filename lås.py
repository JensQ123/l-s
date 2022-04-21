användare = [
    {
        "rfid": "865FF858",
        "finger": "mdh"
    },
    {
        "rfid": "72418574",
        "finger": "gym"
    }
]

rfid = input()

for id in användare:

    if rfid == id["rfid"]:
        finger = input()

    else:
        print("Ingen användare registrerad")

        if id["finger"] == finger:
            print("okej")
        else:
            print("Ingen matchning")





