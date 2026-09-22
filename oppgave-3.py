from datetime import datetime, timedelta


def parse_date(date_text):
    # Gjør tekst i formatet dd.mm.åååå om til en date-verdi
    return datetime.strptime(date_text, "%d.%m.%Y").date()


def read_date(prompt):
    # Spør på nytt heilt til brukeren skriver inn en gyldig dato
    while True:
        date_text = input(prompt)

        try:
            return parse_date(date_text)
        except ValueError:
            print(
                "Ugyldig dato. Bruk formatet dd.mm.åååå "
                "og en dato som finnes."
            )


def read_positive_int(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print("Ugyldig input. Skriv inn et positivt heltall.")
                continue

            return number

        except ValueError:
            print("Ugyldig input. Skriv inn et positivt heltall.")


def calculate_end_time(start_time, duration_minutes):
    start = datetime.strptime(start_time, "%H:%M")

    # Legger varigheten til starttiden for å finne sluttiden
    end = start + timedelta(minutes=duration_minutes)

    return end.strftime("%H:%M")


def days_between_dates(first_date, second_date):
    # abs gjør at antall dager blir positivt uansett hvilken dato som kommer først
    difference = abs((second_date - first_date).days)
    return difference


def sort_dates(dates):
    return sorted(dates)


def main():
    print("===== STUDIEPLANLEGGER =====")

    study_date = read_date("Dato (dd.mm.åååå): ")

    while True:
        start_time = input("Starttidspunkt (HH:MM): ")

        try:
            datetime.strptime(start_time, "%H:%M")
            break
        except ValueError:
            print("Ugyldig tidspunkt. Bruk formatet HH:MM.")

    duration_minutes = read_positive_int("Varighet i minutter: ")

    end_time = calculate_end_time(start_time, duration_minutes)

    print()
    print(f"Dato: {study_date.strftime('%d.%m.%Y')}")
    print(f"Starttid: {start_time}")
    print(f"Sluttid: {end_time}")

    second_date = read_date(
        "Skriv inn en annen dato (dd.mm.åååå): "
    )

    number_of_days = days_between_dates(study_date, second_date)

    print(f"Antall dager mellom datoene: {number_of_days}")

    extra_date = read_date(
        "Skriv inn en tredje dato for sortering (dd.mm.åååå): "
    )

    date_list = [
        study_date,
        second_date,
        extra_date
    ]

    sorted_date_list = sort_dates(date_list)

    print("Datoene i kronologisk rekkefølge:")

    for date in sorted_date_list:
        print(date.strftime("%d.%m.%Y"))


main()