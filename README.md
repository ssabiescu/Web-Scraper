
# Portabilitate Număr de Telefon

## Descriere

Am implementat un script in Python care verifica daca un număr de telefon este portat și furnizează informații despre acesta, cum ar fi operatorul curent, operatorul inițial, data curentă și tipul de număr (📱 sau ☎️).

Scriptul utilizeaza biblioteca `requests` pentru a accesa continutul paginii web https://www.portabilitate.ro/ si biblioteca `BeautifulSoup` pentru a parsa continutul HTML al paginii web.

## Utilizare

#### :arrow_forward: Utilizatorul introduce un numar de telefon valid
#### :arrow_forward: Daca numarul nu este un numar de Romania  valid (nu are exact 10 cifre sau nu incepe cu '07'), utilizatorul este rugat sa introduca din nou numarul
#### :arrow_forward: Scriptul extrage informatii despre `phoneNumber` de pe `https://www.portabilitate.ro/ro-no-phoneNumber`

![portabilitate](https://github.com/ssabiescu/Web-Scraper/assets/156011844/5f705128-b12b-4a91-a676-e8b0b2071a50)


## Instalare si rulare

:white_check_mark: 1. Cloneaza sau descarca acest repository ```git clone https://github.com/ssabiescu/Web-Scraper.git```

:white_check_mark: 2. Instaleaza dependentele folosind ```pip install -r requirements.txt```

:white_check_mark: 3. Ruleaza scriptul folosind ```python portabilitate.py```

