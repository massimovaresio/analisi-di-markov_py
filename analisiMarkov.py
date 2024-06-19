import string  # modulo string di python https://docs.python.org/3/library/string.html


def leggi_pulisci_testo(nome_file):
    """Apre il file di testo gestendo eventuali errori, lo pulisce da elementi non necessari e restituisce una lista di parole
    """
    lista_testo = [] # crea una lista dove andrò a memorizzare le parole del testo
    try:
        with open(nome_file, 'r', encoding='utf-8') as testo: # apre il file e crea un oggetto 'testo' iterabile
            taglia_testo(testo)

            for riga in testo:
                if riga.startswith('*** END OF THIS'):
                    break

            elabora_riga(riga, lista_testo)

            return lista_testo
        
    except FileNotFoundError:
        print(f"Errore: Il file {nome_file} non è stato trovato.")
        return None
    
    except Exception as e:
        print(f"Errore nella lettura del file: {e}")
        return None
    # gestione delle eccezzioni in python https://docs.python.org/3/library/exceptions.html


def taglia_testo(testo):
    """Legge da 'testo' finché non trova la riga che termina l'intestazione

    testo: oggetto file aperto
    """
    for riga in testo:
        if riga.startswith('*** START OF THIS'):
            break


def elabora_riga(riga, lista):
    """Per ogni riga separa le parole e converti tutto il lettere minuscole
    """
    riga = riga.replace('-', ' ')  # metodo delle stringhe replace vedi docs https://docs.python.org/3/library/stdtypes.html#string-methods

    for parola in riga.split(' '):  # suddivide la riga in una lista di stringhe
        parola = parola.lower()  # converti tutto in lettere minuscole (in realtà crea una nuova stringa dato che sono immutabili)
        lista.append(parola)  # aggiungi ciascuna parola alla lista

    return lista   


#ESECUZIONE
t = leggi_pulisci_testo(prova.txt)