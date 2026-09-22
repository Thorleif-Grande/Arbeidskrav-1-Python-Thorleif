# Oppgave 1.1 - Beregn tidsbruk
def read_positive_int(prompt):
    # Spør på nytt heilt til brukeren skriver inn et positivt heltall
    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print("Ugyldig input. Skriv inn et positivt heltall, for eksempel 5.")
                continue

            return number

        except ValueError:
            print("Ugyldig input. Skriv inn et positivt heltall, for eksempel 5.")


def calculate_study_time():
    study_sessions = read_positive_int("Antall studieøkter: ")
    minutes_per_session = read_positive_int("Minutter per økt: ")

    total_minutes = study_sessions * minutes_per_session

    # // finner hele timer, mens % finner minuttene som er igjen
    hours = total_minutes // 60
    minutes = total_minutes % 60

    hour_word = "time" if hours == 1 else "timer"
    minute_word = "minutt" if minutes == 1 else "minutter"

    print(
        f"Samlet tidsbruk: {hours} {hour_word} "
        f"og {minutes} {minute_word}"
    )


# Oppgave 1.2 - Tekstanalyse
def analyze_text():
    while True:
        text = input("Skriv inn en tekst: ")

        # strip fjerner mellomrom slik at bare mellomrom ikkje blir godkjent
        if text.strip() == "":
            print("Teksten kan ikke være tom eller bare mellomrom. Prøv igjen.")
            continue

        break

    characters_with_spaces = len(text)
    characters_without_spaces = len(text.replace(" ", ""))
    lowercase_text = text.lower()
    reversed_text = text[::-1]

    # Bruker små bokstaver slik at søket ikkje blir påvirket av store bokstaver
    contains_python = "python" in lowercase_text
    contains_sql = "sql" in lowercase_text

    print(f"Antall tegn med mellomrom: {characters_with_spaces}")
    print(f"Antall tegn uten mellomrom: {characters_without_spaces}")
    print(f"Tekst med små bokstaver: {lowercase_text}")
    print(f"Teksten baklengs: {reversed_text}")

    if contains_python:
        print("Teksten inneholder ordet python.")
    else:
        print("Teksten inneholder ikke ordet python.")

    if contains_sql:
        print("Teksten inneholder ordet SQL.")
    else:
        print("Teksten inneholder ikke ordet SQL.")


# Oppgave 1.3 - Analyser tallintervall
def analyze_interval():
    while True:
        try:
            start = int(input("Startverdi: "))
            end = int(input("Sluttverdi: "))

            if start > end:
                print(
                    "Startverdien kan ikke være større enn sluttverdien. "
                    "Prøv igjen."
                )
                continue

            break

        except ValueError:
            print(
                "Begge verdiene må være heltall, "
                "for eksempel 3 og 10. Prøv igjen."
            )

    even_numbers = []
    divisible_by_three = []
    total = 0

    for number in range(start, end + 1):
        # Resten må være 0 for at tallet skal være delelig
        if number % 2 == 0:
            even_numbers.append(number)

        if number % 3 == 0:
            divisible_by_three.append(number)

        total += number

    if even_numbers:
        print(f"Partall: {even_numbers}")
    else:
        print("Partall: ingen")

    if divisible_by_three:
        print(f"Delelig med 3: {divisible_by_three}")
    else:
        print("Delelig med 3: ingen")

    print(f"Sum: {total}")


# Oppgave 1.4 - Meny
def main():
    # Menyen kjører heilt til brukeren velger å avslutte
    while True:
        print()
        print("===== MENY =====")
        print("1. Beregn tidsbruk")
        print("2. Analyser tekst")
        print("3. Analyser tallintervall")
        print("4. Avslutt")

        choice = input("Velg et alternativ: ").strip()

        if choice == "1":
            calculate_study_time()

        elif choice == "2":
            analyze_text()

        elif choice == "3":
            analyze_interval()

        elif choice == "4":
            print("Programmet avsluttes.")
            break

        else:
            print("Ugyldig valg. Velg 1, 2, 3 eller 4.")


main()