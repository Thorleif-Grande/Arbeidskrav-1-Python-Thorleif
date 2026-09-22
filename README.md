# Arbeidskrav 1 – Python

**Levert av: Thorleif K. Grande**

Dette repositoryet inneholder løsningene mine på Arbeidskrav 1 i Python.

Oppgavene dekker blant annet grunnleggende programflyt, lister og dictionaries,
funksjoner, dato og tid, CSV-behandling, feilhåndtering, objektorientering,
fillagring og bruk av Git.

---

## Kjøre programmene

Programmene krever Python 3.

Kjør ønsket oppgave fra prosjektmappen, for eksempel:

```text
python oppgave-1.py
```

De andre oppgavene kan kjøres på samme måte:

```text
python oppgave-2.py
python oppgave-3.py
python oppgave-4.py
python oppgave-5.py
```

Oppgave 4 bruker `supporthenvendelser.csv`. CSV-filen må derfor ligge i samme
prosjektmappe som `oppgave-4.py` når programmet kjøres.

Oppgave 5 bruker `activities.json` til lagring og innlasting av aktiviteter.

---

## Filstruktur

```text
Arbeidskrav-1-Python-Thorleif/
│
├── oppgave-1.py
├── oppgave-2.py
├── oppgave-3.py
├── oppgave-4.py
├── oppgave-5.py
│
├── supporthenvendelser.csv
├── support-rapport.txt
├── activities.json
│
├── README.md
├── AI-dokumentasjon.md
└── git-historikk.txt
```

`supporthenvendelser.csv` brukes i Oppgave 4.

`support-rapport.txt` blir generert av Oppgave 4.

`activities.json` brukes til lagring og innlasting av aktiviteter i Oppgave 5,
og fungerer også som eksempeldatafil.

`AI-dokumentasjon.md` beskriver hvordan AI-verktøy ble brukt under arbeidet.

`git-historikk.txt` inneholder Git-historikken for prosjektet.

---

## Oppgave 1 – Grunnleggende programflyt

Oppgave 1 består av flere mindre funksjoner samlet i en meny.

Programmet kan:

- beregne samlet studietid
- analysere tekst
- analysere et tallintervall
- gå tilbake til hovedmenyen etter hver handling

Input blir validert slik at blant annet tom tekst, ugyldige tall og negative
verdier ikke stopper programmet.

Jeg brukte egne hjelpefunksjoner for validering slik at samme kode ikke måtte
skrives flere ganger.

Som en liten egen utvidelse sjekker tekstanalyse-delen også om teksten
inneholder `SQL`, på samme måte som kontrollen for `Python`.

---

## Oppgave 2 – Lister og dictionaries

I Oppgave 2 lagres studieøktene i en liste med dictionaries.

Et eksempel på en studieøkt:

```text
{
    "topic": "Python basics",
    "duration_minutes": 45,
    "status": "completed"
}
```

Jeg valgte dictionaries fremfor tuples fordi feltene får navn. Det gjør for
eksempel:

```text
session["topic"]
```

lettere å forstå enn å hente data basert på en bestemt indeks i en tuple.

Programmet kan:

- registrere studieøkter
- vise alle studieøkter
- vise fullførte studieøkter
- søke etter ord i tema
- sortere etter varighet
- beregne samlet og gjennomsnittlig varighet

---

## Oppgave 3 – Funksjoner og standardbibliotek

Oppgave 3 bruker `datetime` fra Python sitt standardbibliotek.

Programmet inneholder blant annet funksjoner for å:

- konvertere tekst i formatet `dd.mm.åååå` til en dato
- beregne sluttid fra starttid og varighet
- beregne antall dager mellom to datoer
- sortere datoer kronologisk

Jeg valgte å bruke faktiske datoobjekter i stedet for å behandle datoer som
vanlig tekst. Det gjør det enklere å validere og sortere datoene riktig.

### Dokumentasjon brukt

Python-dokumentasjon:

**datetime — Basic date and time types**

https://docs.python.org/3/library/datetime.html

`datetime.strptime()` brukes for å tolke og validere tekst som dato eller
tidspunkt.

`timedelta` brukes for å legge et antall minutter til et starttidspunkt.

### Testing av Oppgave 3

Jeg testet blant annet følgende:

1. **Gyldig dato og tidspunkt**
   - Input: `22.09.2026`, `14:30`, `90 minutter`
   - Forventet resultat: sluttid `16:00`
   - Resultat: bestått

2. **Ugyldig dato**
   - Input: `31.02.2026`
   - Forventet resultat: feilmelding og nytt forsøk
   - Resultat: bestått

3. **Ugyldig måned**
   - Input: `16.16.2036`
   - Forventet resultat: feilmelding og nytt forsøk
   - Resultat: bestått

4. **Ugyldig varighet**
   - Input: `0` eller negativt tall
   - Forventet resultat: avvises
   - Resultat: bestått

5. **Tekst som varighet**
   - Input: `hei`
   - Forventet resultat: avvises
   - Resultat: bestått

6. **Ugyldig skuddårsdag**
   - Input: `29.02.2025`
   - Forventet resultat: avvises
   - Resultat: bestått

7. **Gyldig skuddårsdag**
   - Input: `29.02.2024`
   - Forventet resultat: godtas
   - Resultat: bestått

8. **Sortering av datoer**
   - Input: flere datoer i tilfeldig rekkefølge
   - Forventet resultat: datoene vises kronologisk
   - Resultat: bestått

### Kjent begrensning

Hvis en økt starter for eksempel kl. 23:30 og varer i 60 minutter, vil
sluttiden bli 00:30.

Programmet viser sluttiden riktig, men sier ikke eksplisitt at sluttiden er
neste kalenderdag.

Dette kunne blitt forbedret ved å kombinere dato og tidspunkt i samme
`datetime`-objekt.

---

## Oppgave 4 – CSV og feilhåndtering

Oppgave 4 leser supporthenvendelser fra:

```text
supporthenvendelser.csv
```

CSV-filen leses med `csv.DictReader`.

Hver rad blir kontrollert før den blir brukt.

Programmet sjekker blant annet:

- at alle nødvendige felt finnes
- at `id` er et positivt heltall
- at `minutes` er 0 eller større
- at `is_resolved` er enten `yes` eller `no`

Ugyldige rader blir hoppet over, men resten av filen blir fortsatt behandlet.

Programmet beregner blant annet:

- totalt antall gyldige henvendelser
- antall per kategori
- samlet tidsbruk
- gjennomsnittlig tidsbruk
- løste og uløste henvendelser
- kategorien med flest henvendelser
- uløste henvendelser sortert etter tidsbruk

Resultatet skrives til:

```text
support-rapport.txt
```

### Resultat fra eksempeldata

Med datafilen fikk jeg:

```text
Gyldige henvendelser: 15
Samlet tidsbruk: 466 minutter
Gjennomsnittlig tidsbruk: 31.1 minutter
Løste: 9
Uløste: 6
Kategori med flest henvendelser: utstyr
```

Fem ugyldige rader ble hoppet over uten at programmet stoppet.

### Oppgave 4.4 – Feilretting

Den opprinnelige funksjonen inneholdt flere feil.

#### 1. Feil sammenligningsoperator

Opprinnelig:

```text
if request["is_resolved"] = "yes":
```

Rettet til:

```text
if request["is_resolved"] == "yes":
```

`=` brukes til å tilordne en verdi, mens `==` brukes til å sammenligne to
verdier.

#### 2. Totalen ble overskrevet

Opprinnelig:

```text
total = request["minutes"]
```

Rettet til:

```text
total += request["minutes"]
```

Ellers ville bare minuttene fra den siste løste henvendelsen blitt beholdt.

#### 3. Feil variabel ble returnert

Opprinnelig:

```text
return total_minutes
```

Rettet til:

```text
return total
```

Variabelen `total_minutes` eksisterte ikke i funksjonen.

#### 4. Funksjonskallet manglet argument

Opprinnelig:

```text
sum_resolved_minutes()
```

Funksjonen forventer en liste med henvendelser og må derfor kalles med for
eksempel:

```text
sum_resolved_minutes(requests)
```

---

## Oppgave 5 – Aktivitetsplanlegger

Oppgave 5 er et konsollprogram for planlegging og oppfølging av aktiviteter.

En aktivitet inneholder:

```text
title
category
date
estimated_minutes
status
```

Status er enten:

```text
planned
completed
```

### Activity-klassen

Aktivitetene representeres av klassen `Activity`.

Klassen har attributtene som oppgaven krever og inneholder blant annet
metodene:

```text
get_info()
mark_completed()
to_dict()
```

`get_info()` lager en lesbar tekstversjon av aktiviteten.

`mark_completed()` endrer statusen fra `planned` til `completed`.

`to_dict()` gjør et `Activity`-objekt om til en dictionary slik at det kan
lagres som JSON.

### Dato

Dato blir lagret som et ekte Python `date`-objekt.

Dette gjør at aktiviteter kan sorteres kronologisk.

Sorteringen bruker:

```text
key=lambda activity: activity.date
```

Det betyr at `sorted()` bruker datoen til hvert `Activity`-objekt når
rekkefølgen skal bestemmes.

Ved lagring i JSON blir datoen først gjort om til tekst:

```text
self.date.strftime("%d.%m.%Y")
```

Når data blir lest inn igjen, blir teksten konvertert tilbake til et
datoobjekt.

### Funksjoner

Programmet er delt opp i flere funksjoner med egne ansvarsområder.

Blant de viktigste er:

```text
read_text()
read_date()
read_positive_int()
register_activity()
show_activities()
search_activities()
filter_by_status()
sort_activities()
complete_activity()
show_statistics()
save_activities()
load_activities()
```

Jeg laget også `print_activity_list()` fordi samme utskriftskode ellers måtte
brukes flere steder ved visning, søk, filtrering og sortering.

### Bruk

Når programmet starter blir tidligere lagrede aktiviteter lest fra
`activities.json`.

Hvis filen ikke finnes, vises en melding og programmet starter med en tom
liste.

Menyen lar brukeren:

1. Registrere aktivitet
2. Vise aktiviteter
3. Søke etter tittel eller kategori
4. Filtrere etter status
5. Sortere etter dato eller varighet
6. Markere aktivitet som fullført
7. Vise statistikk
8. Lagre aktiviteter til fil
9. Lese aktiviteter fra fil
10. Avslutte

### Fillagring

Aktivitetene lagres i:

```text
activities.json
```

Jeg valgte JSON fordi dataene passer naturlig som dictionaries med navngitte
felt.

Ved lagring konverteres hvert `Activity`-objekt til en dictionary.

Ved innlasting blir dictionaryene gjort tilbake til `Activity`-objekter.

Programmet håndterer blant annet:

- manglende datafil
- ugyldig JSON
- manglende felt i en aktivitet
- ugyldig dato
- ugyldig varighet
- ugyldig status

Hvis én aktivitet i datafilen er ugyldig, blir den hoppet over uten at resten
av programmet stopper.

### Statistikk

Statistikken viser:

- antall aktiviteter
- samlet estimert tid
- antall fullførte aktiviteter

### Testing av Oppgave 5

Jeg testet blant annet følgende:

1. **Tom tittel**
   - Input: kun mellomrom
   - Forventet resultat: feilmelding og nytt forsøk
   - Resultat: bestått

2. **Ugyldig dato**
   - Input: `31.02.2026`
   - Forventet resultat: feilmelding og nytt forsøk
   - Resultat: bestått

3. **Varighet 0**
   - Input: `0`
   - Forventet resultat: avvises
   - Resultat: bestått

4. **Tekst som varighet**
   - Input: `hei`
   - Forventet resultat: avvises
   - Resultat: bestått

5. **Ugyldig menyvalg**
   - Input: `20`
   - Forventet resultat: feilmelding og menyen vises igjen
   - Resultat: bestått

6. **Søk**
   - Input: søkeord i tittel eller kategori
   - Forventet resultat: riktige aktiviteter vises
   - Resultat: bestått

7. **Statusfilter**
   - Input: `planned` eller `completed`
   - Forventet resultat: bare aktiviteter med riktig status vises
   - Resultat: bestått

8. **Sortering etter dato**
   - Input: flere aktiviteter med forskjellige datoer
   - Forventet resultat: kronologisk rekkefølge
   - Resultat: bestått

9. **Markere aktivitet som fullført**
   - Input: nummeret til en aktivitet
   - Forventet resultat: status endres til `completed`
   - Resultat: bestått

10. **Markere samme aktivitet igjen**
    - Input: aktivitet som allerede er `completed`
    - Forventet resultat: programmet sier at aktiviteten allerede er fullført
    - Resultat: bestått

11. **Lagring og innlasting**
    - Aktivitetene ble lagret til `activities.json`
    - Programmet ble avsluttet og startet på nytt
    - Forventet resultat: aktivitetene blir lest inn igjen
    - Resultat: bestått

12. **Ugyldig aktivitet i JSON**
    - Jeg endret én dato manuelt til `99.99.2026`
    - Forventet resultat: aktiviteten hoppes over uten at programmet krasjer
    - Resultat: bestått

Etter testen med ugyldige JSON-data ble eksempeldatafilen satt tilbake til
gyldige verdier.

### Valg jeg gjorde

Jeg valgte en liste med `Activity`-objekter fordi programmet arbeider med flere
aktiviteter med samme struktur.

Dato blir lagret som `date` i programmet i stedet for vanlig tekst fordi dette
gjør sortering og validering sikrere.

JSON ble valgt for lagring fordi formatet passer godt til objektene og er
enkelt å lese både for Python og mennesker.

Programmet er delt opp i flere små funksjoner i stedet for å legge all logikk
i `main()`.

### Kjente begrensninger

Programmet lagrer ikke automatisk når det avsluttes.

Brukeren må velge `Lagre aktiviteter til fil` før avslutning dersom nye
endringer skal beholdes.

Hvis brukeren velger å lese inn filen på nytt, blir aktivitetene som ligger i
minnet erstattet av innholdet i datafilen.

Programmet viser derfor en advarsel om at ulagrede aktiviteter kan gå tapt.

### Mulige forbedringer

Programmet kunne senere blitt forbedret med:

- automatisk lagring ved avslutning
- mulighet til å redigere en aktivitet
- mulighet til å slette en aktivitet
- ID på hver aktivitet
- flere sorteringsvalg
- statistikk per kategori
- lagring av både dato og tidspunkt
- grafisk brukergrensesnitt

---

## Git og versjonskontroll

Jeg brukte Git gjennom utviklingen og pushet prosjektet til GitHub.

Repository:

https://github.com/Thorleif-Grande/Arbeidskrav-1-Python-Thorleif

Arbeidsflyten bestod hovedsakelig av:

```text
git status
git add <fil>
git commit -m "beskrivelse"
git push
```

Oppgave 5 ble utviklet i flere steg i stedet for én stor commit.

Git-historikken viser blant annet utvikling fra:

```text
grunnstruktur og datohåndtering
→ søk, filtrering, sortering og fullføring
→ statistikk og fillagring
→ forbedret feilhåndtering og opprydding
```

Dette gjorde det mulig å teste hver del før neste del ble lagt til.

En egen kopi av Git-historikken leveres i:

```text
git-historikk.txt
```

---

## Oppgave 6 – Video

Videoen demonstrerer programmet og forklarer blant annet:

- programflyt
- fil- og funksjonsstruktur
- `Activity`-klassen
- datastrukturer
- parametere, argumenter og returverdier
- testing av normal og ugyldig input
- utfordringer og feilsøking
- valg og forbedringsmuligheter
- hvordan AI ble brukt og kvalitetssikret

**Videolenke:** Legges inn før levering.

---

## AI-dokumentasjon

Bruk av AI-verktøy er dokumentert separat i:

```text
AI-dokumentasjon.md
```

Dokumentet beskriver hvilke verktøy som ble brukt, hva de ble brukt til,
eksempler på hvordan de påvirket løsningen, og hvordan forslagene ble
kontrollert og testet underveis.