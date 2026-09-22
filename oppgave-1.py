def calculate_study_time():
    while True:
        try:
            study_sessions = int(input("Antall studieøkter: "))

            if study_sessions <= 0:
                print("Antall studieøkter må være større enn 0.")
                continue

            break

        except ValueError:
            print("Du må skrive inn et positivt heltall.")

    while True:
        try:
            minutes_per_session = int(input("Minutter per økt: "))

            if minutes_per_session <= 0:
                print("Antall minutter per økt må være større enn 0.")
                continue

            break

        except ValueError:
            print("Du må skrive inn et positivt heltall.")

    total_minutes = study_sessions * minutes_per_session
    hours = total_minutes // 60
    minutes = total_minutes % 60

    print(f"Samlet tidsbruk: {hours} timer og {minutes} minutter")


def analyze_text():
    while True:
        text = input("Skriv inn en tekst: ")

        if text.strip() == "":
            print("Teksten kan ikke være tom.")
            continue

        break

    characters_with_spaces = len(text)
    characters_without_spaces = len(text.replace(" ", ""))
    lowercase_text = text.lower()
    reversed_text = text[::-1]
    contains_python = "python" in text.lower()

    print(f"Antall tegn med mellomrom: {characters_with_spaces}")
    print(f"Antall tegn uten mellomrom: {characters_without_spaces}")
    print(f"Tekst med små bokstaver: {lowercase_text}")
    print(f"Teksten baklengs: {reversed_text}")

    if contains_python:
        print("Teksten inneholder ordet python.")
    else:
        print("Teksten inneholder ikke ordet python.")


def analyze_interval():
    while True:
        try:
            start = int(input("Startverdi: "))
            end = int(input("Sluttverdi: "))

            if start > end:
                print("Startverdien kan ikke være større enn sluttverdien.")
                continue

            break

        except ValueError:
            print("Begge verdiene må være heltall.")

    even_numbers = []
    divisible_by_three = []
    total = 0

    for number in range(start, end + 1):
        if number % 2 == 0:
            even_numbers.append(number)

        if number % 3 == 0:
            divisible_by_three.append(number)

        total += number

    print(f"Partall: {even_numbers}")
    print(f"Delelig med 3: {divisible_by_three}")
    print(f"Sum: {total}")


def main():
    while True:
        print()
        print("===== MENY =====")
        print("1. Beregn tidsbruk")
        print("2. Analyser tekst")
        print("3. Analyser tallintervall")
        print("4. Avslutt")

        choice = input("Velg et alternativ: ")

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