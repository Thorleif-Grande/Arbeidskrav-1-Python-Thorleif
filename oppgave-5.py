from datetime import datetime


# Oppgave 5 - Aktivitetsplanlegger


class Activity:
    # Konstruktøren kjøres når me lager et nytt Activity-objekt
    def __init__(
        self,
        title,
        category,
        date,
        estimated_minutes,
        status="planned"
    ):
        # self lagrer verdiene som attributter på akkurat denne aktiviteten
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    # Gir oss en lesbar tekst med informasjon om aktiviteten
    def get_info(self):
        return (
            f"{self.title} | "
            f"Kategori: {self.category} | "
            f"Dato: {self.date.strftime('%d.%m.%Y')} | "
            f"Varighet: {self.estimated_minutes} minutter | "
            f"Status: {self.status}"
        )


# Hjelpefunksjon for tekstfelt som ikkje kan være tomme
def read_text(prompt):
    while True:
        # strip fjerner mellomrom før og etter teksten
        text = input(prompt).strip()

        if text == "":
            print("Feltet kan ikke være tomt. Prøv igjen.")
            continue

        return text


# Leser inn dato og sjekker at den faktisk finnes
def read_date(prompt):
    while True:
        date_text = input(prompt).strip()

        try:
            # Gjør teksten om til en faktisk dato som me kan sortere senere
            return datetime.strptime(date_text, "%d.%m.%Y").date()

        except ValueError:
            print(
                "Ugyldig dato. Bruk formatet dd.mm.åååå "
                "og en dato som finnes."
            )


# Leser inn og sørger for at me får et positivt heltall
def read_positive_int(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print(
                    "Ugyldig input. Skriv inn et positivt heltall."
                )
                continue

            return number

        except ValueError:
            print(
                "Ugyldig input. Skriv inn et positivt heltall."
            )


# Registrerer en ny aktivitet og legger den til i lista
def register_activity(activities):
    print()
    print("===== REGISTRER AKTIVITET =====")

    title = read_text("Tittel: ")
    category = read_text("Kategori: ")
    date = read_date("Dato (dd.mm.åååå): ")
    estimated_minutes = read_positive_int(
        "Estimert varighet i minutter: "
    )

    # Status blir automatisk planned når me lager en ny aktivitet
    activity = Activity(
        title,
        category,
        date,
        estimated_minutes
    )

    activities.append(activity)

    print("Aktiviteten ble registrert.")


# Viser alle aktivitetene som ligg i lista
def show_activities(activities):
    print()
    print("===== AKTIVITETER =====")

    if len(activities) == 0:
        print("Ingen aktiviteter er registrert.")
        return

    # enumerate gjør at aktivitetene får nummer fra 1 og oppover
    for number, activity in enumerate(activities, start=1):
        print(f"{number}. {activity.get_info()}")


def main():
    # Her ligg Activity-objektene så lenge programmet kjører
    activities = []

    # Menyen kjører heilt til brukeren velger å avslutte
    while True:
        print()
        print("===== AKTIVITETSPLANLEGGER =====")
        print("1. Registrer aktivitet")
        print("2. Vis aktiviteter")
        print("3. Avslutt")

        choice = input("Velg et alternativ: ").strip()

        if choice == "1":
            register_activity(activities)

        elif choice == "2":
            show_activities(activities)

        elif choice == "3":
            print("Programmet avsluttes.")
            break

        else:
            print("Ugyldig valg. Velg 1, 2 eller 3.")


main()