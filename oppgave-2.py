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


def print_sessions(sessions):
    for number, session in enumerate(sessions, start=1):
        print(
            f"{number}. Tema: {session['topic']} | "
            f"Varighet: {session['duration_minutes']} minutter | "
            f"Status: {session['status']}"
        )


def register_study_session(study_sessions):
    while True:
        topic = input("Tema: ").strip()

        if topic == "":
            print("Tema kan ikke være tomt. Prøv igjen.")
            continue

        break

    duration_minutes = read_positive_int("Varighet i minutter: ")

    while True:
        status = input("Status (planned/completed): ").strip().lower()

        if status not in ["planned", "completed"]:
            print("Status må være planned eller completed. Prøv igjen.")
            continue

        break

    new_session = {
        "topic": topic,
        "duration_minutes": duration_minutes,
        "status": status
    }

    # Fem eksempeløkter som brukes når programmet starter
    study_sessions = [...]
    study_sessions.append(new_session)

    print("Studieøkten ble registrert.")


def show_all_sessions(study_sessions):
    if len(study_sessions) == 0:
        print("Ingen studieøkter er registrert.")
        return

    print_sessions(study_sessions)


def show_completed_sessions(study_sessions):
    completed_sessions = []

    for session in study_sessions:
        if session["status"] == "completed":
            completed_sessions.append(session)

    if len(completed_sessions) == 0:
        print("Ingen fullførte studieøkter funnet.")
        return

    print_sessions(completed_sessions)


def search_sessions(study_sessions):
    search_word = input("Søk etter ord i tema: ").strip().lower()

    if search_word == "":
        print("Søkeordet kan ikke være tomt.")
        return

    results = []

    for session in study_sessions:
        if search_word in session["topic"].lower():
            results.append(session)

    if len(results) == 0:
        print("Ingen studieøkter passet søket.")
        return

    print_sessions(results)


def get_duration(session):
    return session["duration_minutes"]


def sort_by_duration(study_sessions):
    sorted_sessions = sorted(
        study_sessions,
        key=get_duration,
        reverse=True
    )

    if len(sorted_sessions) == 0:
        print("Ingen studieøkter å sortere.")
        return

    print_sessions(sorted_sessions)


def show_completed_statistics(study_sessions):
    total_duration = 0
    number_of_completed = 0

    for session in study_sessions:
        if session["status"] == "completed":
            total_duration += session["duration_minutes"]
            number_of_completed += 1

    if number_of_completed == 0:
        print("Ingen fullførte studieøkter å beregne.")
        return

    average_duration = total_duration / number_of_completed

    print(f"Samlet varighet: {total_duration} minutter")
    print(f"Gjennomsnittlig varighet: {average_duration:.1f} minutter")


def main():
    study_sessions = [
        {
            "topic": "Python basics",
            "duration_minutes": 45,
            "status": "completed"
        },
        {
            "topic": "Loops",
            "duration_minutes": 60,
            "status": "completed"
        },
        {
            "topic": "Functions",
            "duration_minutes": 50,
            "status": "planned"
        },
        {
            "topic": "Lists and dictionaries",
            "duration_minutes": 75,
            "status": "completed"
        },
        {
            "topic": "File handling",
            "duration_minutes": 90,
            "status": "planned"
        }
    ]

    while True:
        print()
        print("===== STUDIEØKTER =====")
        print("1. Registrer studieøkt")
        print("2. Vis alle studieøkter")
        print("3. Vis fullførte studieøkter")
        print("4. Søk etter ord i tema")
        print("5. Sorter etter varighet")
        print("6. Vis samlet og gjennomsnittlig varighet")
        print("7. Avslutt")

        choice = input("Velg et alternativ: ").strip()

        if choice == "1":
            register_study_session(study_sessions)

        elif choice == "2":
            show_all_sessions(study_sessions)

        elif choice == "3":
            show_completed_sessions(study_sessions)

        elif choice == "4":
            search_sessions(study_sessions)

        elif choice == "5":
            sort_by_duration(study_sessions)

        elif choice == "6":
            show_completed_statistics(study_sessions)

        elif choice == "7":
            print("Programmet avsluttes.")
            break

        else:
            print("Ugyldig valg. Velg et tall fra 1 til 7.")


main()