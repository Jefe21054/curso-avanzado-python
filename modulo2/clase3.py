'''
TRABAJO CON ARCHIVOS CSV
'''
import csv
from pathlib import Path


FILE_PATH = Path('users.csv')


def read_csv():
    try:
        with open(FILE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row.get('first_name'), ' : ', row.get('email'))
    except FileNotFoundError:
        print('No se encontro el archivo')


def write_csv():
    try:
        with open(FILE_PATH, 'a') as file:
            writer = csv.DictWriter(
                file, fieldnames=['id', 'first_name', 'last_name', 'email']
            )

            writer.writerows([
                {
                    'id': 251,
                    'first_name': 'Ivan',
                    'last_name': 'Iglesias',
                    'email': 'ivaniglesias@ed.team',
                },
                {
                    'id': 252,
                    'first_name': 'Cesar',
                    'last_name': 'Mayta',
                    'email': 'cesarmayta@ed.team',
                }
            ])

            print('Datos Agregados con EXITO!')
    except FileNotFoundError:
        print('No se encontro el archivo')


if __name__ == '__main__':
    write_csv()
    read_csv()
