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

    # Endrer statusen på aktiviteten til completed
    def mark_completed(self):
        self.status = "completed"


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


# Leser inn og sørger for at me får eit positivt heltall
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

    # Status blir automatisk planned når me lager ein ny aktivitet
    activity = Activity(
        title,
        category,
        date,
        estimated_minutes
    )

    activities.append(activity)

    print("Aktiviteten ble registrert.")


# Viser alle aktivitetene som ligger i lista
def show_activities(activities):
    print()
    print("===== AKTIVITETER =====")

    if len(activities) == 0:
        print("Ingen aktiviteter er registrert.")
        return

    # enumerate gjør at aktivitetene får nummer fra 1 og oppover
    for number, activity in enumerate(activities, start=1):
        print(f"{number}. {activity.get_info()}")


# Søker etter tekst i både tittel og kategori
def search_activities(activities):
    search_word = read_text(
        "Søk etter tittel eller kategori: "
    ).lower()

    results = []

    for activity in activities:
        if (
            search_word in activity.title.lower()
            or search_word in activity.category.lower()
        ):
            results.append(activity)

    if len(results) == 0:
        print("Ingen aktiviteter passet søket.")
        return

    print()
    print("===== SØKERESULTAT =====")

    for number, activity in enumerate(results, start=1):
        print(f"{number}. {activity.get_info()}")


# Filtrerer aktivitetene etter planned eller completed
def filter_by_status(activities):
    while True:
        status = input(
            "Status (planned/completed): "
        ).strip().lower()

        if status not in ["planned", "completed"]:
            print("Status må være planned eller completed.")
            continue

        break

    filtered_activities = []

    for activity in activities:
        if activity.status == status:
            filtered_activities.append(activity)

    if len(filtered_activities) == 0:
        print(f"Ingen aktiviteter med status {status}.")
        return

    print()
    print(f"===== {status.upper()} =====")

    for number, activity in enumerate(
        filtered_activities,
        start=1
    ):
        print(f"{number}. {activity.get_info()}")


# Sorterer aktivitetene etter dato eller estimert varighet
def sort_activities(activities):
    if len(activities) == 0:
        print("Ingen aktiviteter å sortere.")
        return

    while True:
        print()
        print("1. Sorter etter dato")
        print("2. Sorter etter varighet")

        choice = input("Velg sortering: ").strip()

        if choice == "1":
            # date er et datoobjekt, så Python kan sortere kronologisk
            sorted_activities = sorted(
                activities,
                key=lambda activity: activity.date
            )
            break

        elif choice == "2":
            sorted_activities = sorted(
                activities,
                key=lambda activity: activity.estimated_minutes
            )
            break

        else:
            print("Ugyldig valg. Velg 1 eller 2.")

    print()
    print("===== SORTERTE AKTIVITETER =====")

    for number, activity in enumerate(
        sorted_activities,
        start=1
    ):
        print(f"{number}. {activity.get_info()}")


# Lar brukeren velge hvilken aktivitet som skal fullføres
def complete_activity(activities):
    if len(activities) == 0:
        print("Ingen aktiviteter er registrert.")
        return

    show_activities(activities)

    while True:
        activity_number = read_positive_int(
            "Nummer på aktiviteten som er fullført: "
        )

        # Brukeren ser nummer fra 1, mens lista starter på indeks 0
        if activity_number > len(activities):
            print("Det finnes ingen aktivitet med dette nummeret.")
            continue

        activity = activities[activity_number - 1]

        if activity.status == "completed":
            print("Denne aktiviteten er allerede fullført.")
            return

        activity.mark_completed()

        print(
            f"{activity.title} er markert som fullført."
        )
        return


def main():
    # Her ligger Activity-objektene så lenge programmet kjører
    activities = []

    # Menyen kjører heilt til brukeren velger å avslutte
    while True:
        print()
        print("===== AKTIVITETSPLANLEGGER =====")
        print("1. Registrer aktivitet")
        print("2. Vis aktiviteter")
        print("3. Søk etter tittel eller kategori")
        print("4. Filtrer etter status")
        print("5. Sorter etter dato eller varighet")
        print("6. Marker aktivitet som fullført")
        print("7. Avslutt")

        choice = input("Velg et alternativ: ").strip()

        if choice == "1":
            register_activity(activities)

        elif choice == "2":
            show_activities(activities)

        elif choice == "3":
            search_activities(activities)

        elif choice == "4":
            filter_by_status(activities)

        elif choice == "5":
            sort_activities(activities)

        elif choice == "6":
            complete_activity(activities)

        elif choice == "7":
            print("Programmet avsluttes.")
            break

        else:
            print("Ugyldig valg. Velg et tall fra 1 til 7.")


main()