import requests
from bs4 import BeautifulSoup

# Functie validare numar de telefon
def validate(phone_number):
    if len(phone_number) != 10 or phone_number[0] != '0' or phone_number[1] != '7':
        return False
    else:
        return True

print("\n")

# Validare nr de telefon
while 1:
    phone_number = input("Introduceți un număr de telefon: ")
    if validate(phone_number):
        break
    else:
        print("Numărul de telefon introdus nu este valid. Vă rugăm să încercați din nou.")

# Construirea URL-ului cu numarul de telefon introdus de la tastatura
url = 'https://www.portabilitate.ro/NumberSearch.aspx?lang=ro&number='+str(phone_number)

# Obtinerea continutului paginii web: www.portabilitate.ro
response = requests.get(url)
html = response.text

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if 'este portat' in str(response.content):
    print('Numarul ', phone_number, ' este portat')
else:
    print('Numarul ', phone_number, ' nu este portat')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Parsarea continutului HTML cu BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Selectarea containerului CSS care contine informatiile despre numarul de telefon
container = soup.select_one('#ctl00_cphBody_panelDetails > table')

# Extragerea datelor din container
if container:

    operator_curent_label = container.find(string='Operator curent:')
    if operator_curent_label:
        operator_curent = operator_curent_label.find_next().get_text(strip=True)
    else:
        operator_curent = "Informație lipsă"

    operator_initial_label = container.find(string='Operator iniţial:')
    if operator_initial_label:
        operator_initial = operator_initial_label.find_next().get_text(strip=True)
    else:
        operator_initial = "Informație lipsă"

    data_curenta_label = container.find(string='Data curentă:')
    if data_curenta_label:
        data_curenta = data_curenta_label.find_next().get_text(strip=True)
    else:
        data_curenta = "Informație lipsă"

    tip_numar_label = container.find(string='Tip număr:')
    if tip_numar_label:
        tip_numar = tip_numar_label.find_next().get_text(strip=True)
    else:
        tip_numar = "Informație lipsă"

    # Afisarea informatiilor
    print(f"Operator curent: {operator_curent}")
    print(f"Operator inițial: {operator_initial}")
    print(f"Data curentă: {data_curenta}")
    print(f"Tip număr: {tip_numar}")
else:
    print("Eroare la gasirea containerului")


