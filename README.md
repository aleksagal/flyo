# <img width="58" height="24" alt="Logo" src="https://github.com/user-attachments/assets/dd28dfce-560b-4088-9414-f04fcaabeaff" /> (aplikacja do rezerwacji lotów) 

Flyo to aplikacja webowa napisana w Pythonie z wykorzystaniem frameworka Django. Projekt umożliwia użytkownikom przeglądanie dostępnych kierunków lotów, filtrowanie ofert, rezerwowanie biletów oraz zarządzanie własnymi rezerwacjami. Design został oparty na mockupie w figmie.

<img width="1006" height="265" alt="image" src="https://github.com/user-attachments/assets/c1dc0225-583c-4042-84a2-5070bc5fa85f" />

## Technologie

- Python
- Django
- HTML
- Bootstrap 5
- CSS
- JavaScript
- 
https://github.com/user-attachments/assets/aaf29c03-c525-4fca-a881-ce0945d9714f

## Główne funkcjonalności

- rejestracja użytkownika,
- logowanie i wylogowanie,
- lista dostępnych destynacji,
- szczegóły wybranej destynacji,
- filtrowanie lotów po mieście wylotu, linii lotniczej i dacie,
- wybór typu podróży: one way lub both way,
- rezerwacja lotu,
- blokada ponownej rezerwacji tego samego lotu w tej samej dacie,
- lista rezerwacji przypisana do zalogowanego użytkownika,
- anulowanie rezerwacji,
- upload obrazków,
- panel administracyjny Django,
- responsywny interfejs z użyciem Bootstrap i CSS.

## Struktura bazy danych

Aplikacja wykorzystuje bazę danych zarządzaną przez Django ORM.

### Destination

Model przechowuje informacje o dostępnych kierunkach lotów.

Pola:

- `name` — nazwa destynacji,
- `country` — kraj,
- `starting_price` — cena początkowa,
- `image` lub `image_path` — obrazek destynacji.

### Airline

Model przechowuje dostępne linie lotnicze.

Pola:

- `name` — nazwa linii lotniczej.

### FlightOffer

Model reprezentuje konkretną ofertę lotu.

Pola:

- `from_city` — miasto wylotu,
- `to_destination` — destynacja,
- `airline` — linia lotnicza,
- `price` — cena lotu,
- `duration` — czas trwania lotu,
- `baggage_included` — informacja, czy bagaż jest w cenie.

### Reservation

Model przechowuje rezerwacje użytkowników.

Pola:

- `user` — użytkownik, który wykonał rezerwację,
- `destination` — miejsce docelowe,
- `departure_city` — miasto wylotu,
- `airline` — linia lotnicza,
- `price` — cena,
- `baggage` — informacja o bagażu,
- `trip_type` — typ podróży,
- `departure_date` — data wylotu,
- `return_date` — data powrotu,
- `created_at` — data utworzenia rezerwacji.

## Widoki aplikacji

### Login / Register

<img width="1835" height="957" alt="image" src="https://github.com/user-attachments/assets/21c67d78-5b3d-4a47-9174-f3b63d868b2e" />


Strona startowa aplikacji. Użytkownik może się zalogować albo utworzyć konto za pomocą formularza w modalu.

### Flights

<img width="1822" height="941" alt="image" src="https://github.com/user-attachments/assets/b59c9701-70ae-4fb4-b5e4-abddb550d859" />


Widok listy destynacji. Użytkownik widzi dostępne kierunki oraz ceny początkowe. Z tego poziomu może przejść do szczegółów wybranej destynacji.

### Booking

<img width="1807" height="968" alt="image" src="https://github.com/user-attachments/assets/4e3d43da-3855-4a0e-aa02-4326e60e96e6" />

Widok szczegółów destynacji. Użytkownik wybiera:

- miasto wylotu,
- linię lotniczą,
- typ podróży,
- datę wylotu,
- datę powrotu dla podróży w obie strony.

Po wyszukaniu aplikacja pokazuje dostępne oferty lotów. Użytkownik może zarezerwować wybraną ofertę.

### Reservations

<img width="1842" height="957" alt="image" src="https://github.com/user-attachments/assets/a5472a50-8af4-40b1-bb57-ad6ff97fee2e" />


Widok rezerwacji zalogowanego użytkownika. Użytkownik może zobaczyć swoje rezerwacje oraz anulować wybraną rezerwację.

## Zarządzanie rezerwacjami

Każda rezerwacja jest przypisana do konkretnego użytkownika. Dzięki temu użytkownik widzi tylko swoje rezerwacje.

Aplikacja sprawdza, czy użytkownik nie próbuje zarezerwować ponownie tego samego lotu w tym samym terminie. Jeśli taka rezerwacja już istnieje, aplikacja wyświetla komunikat o błędzie i prosi o wybranie innego terminu lub innej oferty.

## Uruchomienie projektu

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/aleksagal/flyo.git
cd flyo
```

### 2. Instalacja zależności

```bash
python -m pip install django pillow
```

### 3. Migracje bazy danych

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Utworzenie administratora

```bash
python manage.py createsuperuser
```

### 5. Uruchomienie serwera

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:8000/
```

Panel administratora:

```text
http://127.0.0.1:8000/admin/
```

## Przykładowy przebieg działania

1. Użytkownik tworzy konto.
2. Loguje się do aplikacji.
3. Przechodzi do listy destynacji.
4. Wybiera kierunek lotu.
5. Filtruje oferty według miasta wylotu, linii lotniczej i dat.
6. Rezerwuje wybraną ofertę.
7. Przechodzi do swoich rezerwacji.
8. Może anulować wybraną rezerwację.

