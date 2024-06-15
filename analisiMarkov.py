import string  # modulo string di python https://docs.python.org/3/library/string.html

"""FASE DI STALLO, BISOGNA RIPARTIRE DA CAPO SUL RAGIONAMENTO DA SEGUIRE, PROVARE A RIPRENDERE LE SOLUZIONI DI DOWNEY PER GESTIRE
   LA CREAZIONE DEL DIZIONARIO ELIMINANDO LE PARTI DI TESTO CHE NON MI SERVONO
"""


def leggi_testo(nome_file):
    """Apre il file di testo e gestisce eventuali errori
    """
    try:
        testo = open(nome_file, 'r', encoding='utf-8') # apre il file e crea un oggetto testo iterabile
        return testo
    except FileNotFoundError:
        print(f"Errore: Il file {nome_file} non è stato trovato.")
        return None
    except Exception as e:
        print(f"Errore nella lettura del file: {e}")
        return None
    # gestione delle eccezzioni in python https://docs.python.org/3/library/exceptions.html