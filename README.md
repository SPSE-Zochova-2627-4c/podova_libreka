# Libreka

Libreka je webova aplikacia pre skolsky/maturitny projekt. Cielom projektu je vytvorit jednoduche prostredie pre pracu s pouzivatelmi a kniznicnym obsahom, ktore sa bude postupne rozsirovat o prihlasovanie, profil pouzivatela a dalsie funkcie.

Projekt je momentalne vo vyvoji a obsahuje zakladnu Django aplikaciu so strankami:

- uvodna stranka,
- prihlasenie,
- profil pouzivatela,
- administracia cez Django admin.

## Pouzite technologie

- Python
- Django
- SQLite
- HTML
- CSS

## Spustenie projektu

Najjednoduchsi sposob spustenia vo Windows je cez pripraveny subor:

```bat
run_django.bat
```

Skript vytvori virtualne prostredie, nainstaluje Django, ak chyba, a spusti vyvojovy server.

Projekt sa da spustit aj rucne:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install django
python manage.py runserver
```

Po spusteni je aplikacia dostupna na adrese:

```text
http://127.0.0.1:8000/
```

## Planovane funkcie

- prihlasovanie a registracia pouzivatelov,
- profil pouzivatela,
- sprava kniznicnych zaznamov,
- databazovy model aplikacie,
- krajsie a prehladnejsie pouzivatelske rozhranie.

## Stav projektu

Projekt je v pociatocnej faze vyvoja. README aj funkcionalita sa budu priebezne doplnat pocas prace na maturitnom projekte.
