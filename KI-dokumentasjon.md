# KI-dokumentasjon – Arbeidskrav 1 Python

**Student: Thorleif K. Grande**

## Om KI-bruken

Jeg har brukt generativ KI som et støtteverktøy gjennom deler av arbeidskravet.

Jeg har selv arbeidet med, skrevet og satt sammen koden i oppgavene, og har
kjørt og testet programmene underveis i PyCharm. ChatGPT ble hovedsakelig
brukt når jeg hadde spørsmål om Python-konsepter, ønsket å diskutere et
løsningsvalg, trengte hjelp til å finne en feil eller ville ha en ekstra
gjennomgang av kode jeg allerede jobbet med.

Når KI foreslo korrigeringer eller kodeendringer, gikk jeg gjennom forslagene,
vurderte om de passet løsningen og testet dem selv før de eventuelt ble
beholdt. På den måten ble KI brukt som støtte i utviklingsprosessen, mens jeg
selv hadde ansvar for den endelige løsningen og for å kontrollere at den
fungerte.

Jeg brukte også Claude enkelte ganger som en second opinion på løsninger som
allerede var laget, for å se om en annen kodegjennomgang fanget opp svakheter
eller forbedringsmuligheter.

**Merknad om prompts:** Noen av promptene nedenfor er lett språklig ryddet
eller formulert mer sammenhengende enn de opprinnelige chatmeldingene. Dette
er gjort for lesbarhet, men problemstillingen og betydningen er den samme.

Svarene er forkortet til de delene som hadde betydning for løsningen.
Generelle samtaler som ikke påvirket det som leveres, er ikke tatt med.

---

# Oppgave 1 – Validering og modulo

## Positivt heltall

### Prompt

> Jeg bruker positive heltall flere steder. Hvordan kan jeg validere input slik
> at tekst, 0 og negative tall blir avvist, men brukeren får prøve igjen uten
> at programmet stopper?

### Relevant del av KI-svaret

Det ble forklart hvordan `while True` sammen med `try/except ValueError` kan
brukes for å fortsette å spørre til brukeren skriver et gyldig tall.

Eksempel:

```text
try:
    number = int(input(prompt))

    if number <= 0:
        continue

    return number

except ValueError:
    ...
```

### Hvordan det påvirket løsningen

Jeg brukte dette prinsippet i `read_positive_int()` og gjenbrukte samme type
validering senere i andre oppgaver.

Jeg testet selv blant annet med positive tall, `0`, negative tall og tekst.

---

## Modulo

### Prompt

> Jeg er litt usikker på modulo. Kan du forklare hvorfor `% 2 == 0` betyr
> partall, og hvordan samme prinsipp brukes for tall som er delelige med 3?

### Relevant del av KI-svaret

KI forklarte at `%` gir resten etter divisjon.

```text
number % 2 == 0
```

betyr at tallet kan deles på 2 uten rest, mens:

```text
number % 3 == 0
```

betyr at tallet kan deles på 3 uten rest.

### Hvordan det påvirket løsningen

Dette ble brukt i tallintervallanalysen i Oppgave 1.

---

# Oppgave 2 – Valg av datastruktur

### Prompt

> Hver studieøkt har tema, varighet og status. Oppgaven tillater dictionary
> eller tuple. Hva er mest oversiktlig å bruke her, og hvorfor?

### Relevant del av KI-svaret

Det ble forklart at dictionaries passer godt fordi hvert felt kan få et navn:

```text
{
    "topic": "Python basics",
    "duration_minutes": 45,
    "status": "completed"
}
```

Dette gjør blant annet:

```text
session["topic"]
```

mer lesbart enn å hente verdier fra faste indeksposisjoner.

### Hvordan det påvirket løsningen

Jeg valgte derfor en liste med dictionaries for studieøktene.

Jeg bygget videre funksjonene for registrering, søk, filtrering, sortering og
statistikk rundt denne strukturen.

---

# Oppgave 3 – Dato og tid

## Validering av dato

### Prompt

> Hvordan kan jeg bruke `datetime` til å sjekke både datoformatet og om datoen
> faktisk finnes? Jeg vil for eksempel at `31.02.2026` skal bli avvist.

### Relevant del av KI-svaret

Det ble forklart at `datetime.strptime()` både tolker formatet og gir
`ValueError` dersom datoen ikke finnes.

```text
datetime.strptime(date_text, "%d.%m.%Y").date()
```

### Hvordan det påvirket løsningen

Dette ble brukt i datovalideringen.

Jeg testet blant annet ugyldige datoer og skuddår:

```text
31.02.2026
29.02.2025
29.02.2024
```

---

## Beregning av sluttid

### Prompt

> Hvordan kan jeg legge for eksempel 90 minutter til et starttidspunkt med
> Python sitt standardbibliotek?

### Relevant del av KI-svaret

Det ble forklart hvordan `timedelta` kan brukes sammen med `datetime`:

```text
start = datetime.strptime(start_time, "%H:%M")
end = start + timedelta(minutes=duration_minutes)
```

### Hvordan det påvirket løsningen

Dette prinsippet ble brukt i `calculate_end_time()`.

Jeg testet blant annet at `14:30 + 90 minutter` ga `16:00`.

---

# Oppgave 4 – CSV og feilhåndtering

## Ugyldige CSV-rader

### Prompt

> CSV-filen har noen ugyldige rader. Hvordan kan jeg behandle hver rad separat,
> slik at én feil rad blir hoppet over uten at hele programmet stopper?

### Relevant del av KI-svaret

Det ble anbefalt å validere hver rad inne i løkken og bruke målrettet
`try/except`.

Det ble også forklart hvorfor:

```text
enumerate(reader, start=2)
```

er nyttig når første linje i CSV-filen inneholder overskriftene.

### Hvordan det påvirket løsningen

Dette ble brukt i `read_support_requests()`.

Programmet kunne dermed rapportere ugyldige rader og fortsette med resten av
filen.

Jeg kontrollerte resultatet mot datafila og fikk 15 gyldige henvendelser.

---

## Feilretting i Oppgave 4.4

### Prompt

> Jeg vil forstå feilene i funksjonen i Oppgave 4.4, ikke bare rette dem.
> Hvorfor er `=`, summeringen og returverdien feil?

### Relevant del av KI-svaret

Det ble forklart at:

```text
=
```

tilordner en verdi, mens:

```text
==
```

sammenligner verdier.

Det ble også forklart at:

```text
total = request["minutes"]
```

overskriver totalen, mens:

```text
total += request["minutes"]
```

legger verdien til den eksisterende totalen.

Til slutt måtte riktig variabel returneres, og funksjonen måtte få
`requests` som argument.

### Hvordan det påvirket løsningen

Jeg rettet funksjonen og brukte forklaringene i README-dokumentasjonen.

---

# Oppgave 5 – Aktivitetsplanlegger

## Activity-klassen

### Prompt

> Hvordan kan jeg lage en enkel `Activity`-klasse på introduksjonsnivå med
> attributtene oppgaven krever, uten å gjøre objektorienteringen unødvendig
> avansert?

### Relevant del av KI-svaret

Det ble foreslått en klasse med:

```text
title
category
date
estimated_minutes
status
```

og en enkel metode for å vise informasjon om aktiviteten.

### Hvordan det påvirket løsningen

Jeg brukte dette som grunnstruktur og bygget resten av aktivitetsplanleggeren
rundt en liste med `Activity`-objekter.

---

## Dato som `date`-objekt

### Second opinion

Jeg brukte Claude til en ekstra kodegjennomgang av en allerede fungerende
versjon.

Det ble påpekt at datoen ble validert med `strptime`, men fortsatt lagret som
tekst. Det kunne gi feil sortering når datoene var skrevet som
`dd.mm.åååå`.

Forslaget var:

```text
return datetime.strptime(date_text, "%d.%m.%Y").date()
```

og å bruke `strftime()` når datoen skulle vises.

### Hvordan det påvirket løsningen

Jeg tok endringen inn fordi den gjorde kronologisk sortering enklere og mer
robust.

Jeg testet deretter sortering med aktiviteter på forskjellige datoer.

---

## JSON-lagring

### Prompt

> Jeg har en liste med `Activity`-objekter og trenger å lagre dem til fil.
> Hvordan kan jeg gjøre dette enkelt med JSON, spesielt siden datoen nå er et
> `date`-objekt?

### Relevant del av KI-svaret

Det ble forklart at JSON ikke kan lagre Python sitt `date`-objekt direkte.

Derfor ble det foreslått å gjøre objektet om til en dictionary og lagre datoen
som tekst:

```text
"date": self.date.strftime("%d.%m.%Y")
```

Ved innlasting blir teksten konvertert tilbake til en dato.

### Hvordan det påvirket løsningen

Dette ble brukt i `to_dict()`, `save_activities()` og `load_activities()`.

Jeg testet løsningen ved å lagre aktiviteter, avslutte programmet og starte
det på nytt. Aktivitetene ble da lest inn igjen fra `activities.json`.

---

## Robust innlasting

### Second opinion

Ved en senere kodegjennomgang ble det påpekt at en JSON-fil kunne være gyldig
som JSON, men fremdeles inneholde én aktivitet med for eksempel ugyldig dato
eller manglende felt.

Det ble foreslått å validere hver aktivitet separat i stedet for å la én feil
stoppe hele innlastingen.

### Hvordan det påvirket løsningen

`load_activities()` ble forbedret slik at ugyldige aktiviteter kan hoppes over.

Jeg testet dette ved å endre én dato i `activities.json` til:

```text
99.99.2026
```

Programmet meldte at aktiviteten var ugyldig og fortsatte med de andre
aktivitetene.

Etter testen satte jeg datoen tilbake til en gyldig verdi.

---

# README og dokumentasjon

### Prompt

> Kan du hjelpe meg å strukturere README ut fra det jeg faktisk har laget og
> testet? Jeg trenger blant annet funksjon, kodevalg, testtilfeller, kjente
> begrensninger og forbedringsmuligheter.

### Relevant del av KI-svaret

KI ble brukt til å foreslå struktur og formulering av README, blant annet
seksjoner for:

- oppgavene
- testtilfeller
- kodevalg
- dokumentasjonskilde
- kjente begrensninger
- forbedringsmuligheter
- Git
- video
- KI-dokumentasjon

### Hvordan det påvirket løsningen

README ble strukturert med KI-støtte, men innholdet ble kontrollert opp mot
programmene og testene jeg faktisk hadde gjennomført.

Jeg brukte også en ekstra KI-gjennomgang for å kontrollere README mot
leveransekravene. Dette fanget blant annet opp manglende kjøreinstruksjoner,
navn, Git-historikk og plass for videolenke.

---

# Testing og egen kontroll

Testing var en viktig del av arbeidsprosessen.

KI ble brukt til enkelte forslag til testtilfeller, men jeg kjørte programmene
og gjennomførte testene selv i PyCharm.

Jeg testet blant annet:

- tomme tekstfelt
- tekst der heltall var forventet
- 0 og negative tall
- ugyldige datoer
- skuddår
- søk og filtrering
- sortering
- fullføring av aktiviteter
- ugyldige CSV-rader
- manglende datafil
- lagring og innlasting
- ugyldige data i JSON

Når jeg gjorde endringer etter en kodegjennomgang, kjørte jeg programmet på
nytt for å kontrollere at endringen fungerte før jeg gikk videre.

---

# Oppsummering

KI ble først og fremst brukt når jeg ønsket:

- en forklaring på et Python-konsept
- en vurdering av et løsningsvalg
- hjelp med feilsøking
- en ekstra kodegjennomgang
- forslag til forbedringer
- hjelp med strukturering av dokumentasjon

Jeg har selv arbeidet med koden, implementert og testet løsningene og gjort
vurderinger underveis om hvilke KI-forslag som var relevante å bruke.
Korrigeringer og forbedringsforslag fra KI ble kontrollert mot programmet før
de ble beholdt i den endelige løsningen.

KI ble også brukt som støtte til struktur og formulering av denne
dokumentasjonen.
