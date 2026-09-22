import csv


# Oppgave 4.1 - Les og kontroller data
def read_support_requests(filename):
    valid_requests = []

    try:
        # with sørger for at fila blir lukka etter bruk
        with open(filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            # Startar på 2 siden rad 1 i CSV-fila er overskriftene
            for row_number, row in enumerate(reader, start=2):
                try:
                    required_fields = [
                        "id",
                        "category",
                        "minutes",
                        "is_resolved"
                    ]

                    # Sjekkar at alle feltene faktisk har en verdi
                    if any(
                        row.get(field) is None or row.get(field).strip() == ""
                        for field in required_fields
                    ):
                        raise ValueError("Et eller flere felt mangler.")

                    request_id = int(row["id"])

                    if request_id <= 0:
                        raise ValueError(
                            "id må være et positivt heltall."
                        )

                    minutes = int(row["minutes"])

                    if minutes < 0:
                        raise ValueError(
                            "minutes må være 0 eller større."
                        )

                    if row["is_resolved"] not in ["yes", "no"]:
                        raise ValueError(
                            "is_resolved må være yes eller no."
                        )

                    valid_request = {
                        "id": request_id,
                        "category": row["category"],
                        "minutes": minutes,
                        "is_resolved": row["is_resolved"]
                    }

                    valid_requests.append(valid_request)

                except ValueError as error:
                    # En dårlig rad skal ikkje stoppa resten av fila
                    print(
                        f"Rad {row_number} er ugyldig: {error}"
                    )

    except FileNotFoundError:
        print(f"Fant ikke filen: {filename}")

    except OSError as error:
        print(f"Kunne ikke lese filen: {error}")

    return valid_requests


# Oppgave 4.2 - Analyser data
def analyze_requests(requests):
    category_counts = {}
    total_minutes = 0
    resolved_count = 0
    unresolved_count = 0
    unresolved_requests = []

    for request in requests:
        category = request["category"]

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1
        total_minutes += request["minutes"]

        if request["is_resolved"] == "yes":
            resolved_count += 1
        else:
            unresolved_count += 1
            unresolved_requests.append(request)

    if len(requests) > 0:
        average_minutes = total_minutes / len(requests)
    else:
        average_minutes = 0

    if category_counts:
        most_common_category = max(
            category_counts,
            key=category_counts.get
        )
    else:
        most_common_category = "Ingen kategorier"

    # Mest tidkrevande uløste henvendelse skal komma først
    unresolved_requests.sort(
        key=lambda request: request["minutes"],
        reverse=True
    )

    return {
        "total_requests": len(requests),
        "category_counts": category_counts,
        "total_minutes": total_minutes,
        "average_minutes": average_minutes,
        "resolved_count": resolved_count,
        "unresolved_count": unresolved_count,
        "most_common_category": most_common_category,
        "unresolved_requests": unresolved_requests
    }


# Oppgave 4.3 - Skriv rapport
def create_report(analysis, filename):
    # "w" oppretter fila, eller overskriver den om den finnes fra før
    with open(filename, "w", encoding="utf-8") as file:
        file.write("SUPPORT-RAPPORT\n")
        file.write("================\n\n")

        file.write("ANTALL HENVENDELSER\n")
        file.write(
            f"Totalt antall gyldige henvendelser: "
            f"{analysis['total_requests']}\n\n"
        )

        file.write("HENVENDELSER PER KATEGORI\n")

        for category, count in analysis["category_counts"].items():
            file.write(f"{category}: {count}\n")

        file.write("\nTIDSBRUK\n")
        file.write(
            f"Samlet tidsbruk: "
            f"{analysis['total_minutes']} minutter\n"
        )
        file.write(
            f"Gjennomsnittlig tidsbruk: "
            f"{analysis['average_minutes']:.1f} minutter\n\n"
        )

        file.write("STATUS\n")
        file.write(
            f"Løste henvendelser: "
            f"{analysis['resolved_count']}\n"
        )
        file.write(
            f"Uløste henvendelser: "
            f"{analysis['unresolved_count']}\n\n"
        )

        file.write("KATEGORI MED FLEST HENVENDELSER\n")
        file.write(f"{analysis['most_common_category']}\n\n")

        file.write(
            "ULØSTE HENVENDELSER - MEST TIDSKREVENDE FØRST\n"
        )

        if analysis["unresolved_requests"]:
            for request in analysis["unresolved_requests"]:
                file.write(
                    f"ID {request['id']} | "
                    f"{request['category']} | "
                    f"{request['minutes']} minutter\n"
                )
        else:
            file.write("Ingen uløste henvendelser.\n")


# Oppgave 4.4 - Finn og rett feil
def sum_resolved_minutes(
    requests: list[dict[str, str | int]]
) -> int:
    total = 0

    for request in requests:
        # == sammenligner verdien, mens = brukes til å sette en verdi
        if request["is_resolved"] == "yes":
            # Legger til minuttene i stedet for å overskriva totalen
            total += request["minutes"]

    # Variabelen heter total, ikkje total_minutes
    return total


def main():
    filename = "supporthenvendelser.csv"

    requests = read_support_requests(filename)
    analysis = analyze_requests(requests)

    create_report(analysis, "support-rapport.txt")

    print()
    print("===== SUPPORTANALYSE =====")
    print(f"Gyldige henvendelser: {analysis['total_requests']}")
    print(
        f"Samlet tidsbruk: "
        f"{analysis['total_minutes']} minutter"
    )
    print(
        f"Gjennomsnittlig tidsbruk: "
        f"{analysis['average_minutes']:.1f} minutter"
    )
    print(f"Løste: {analysis['resolved_count']}")
    print(f"Uløste: {analysis['unresolved_count']}")
    print(
        f"Kategori med flest henvendelser: "
        f"{analysis['most_common_category']}"
    )

    print()
    print("Rapport skrevet til support-rapport.txt")


main()