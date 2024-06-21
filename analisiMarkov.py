import string  # modulo string di python https://docs.python.org/3/library/string.html
from collections import defaultdict


def leggi_pulisci_testo(nome_file):
    """Apre il file di testo gestendo eventuali errori, lo pulisce da elementi non necessari e restituisce una lista di parole
    """
    lista_parole = []  # crea una lista dove andrò a memorizzare le parole del testo
    try:
        with open(nome_file, 'r', encoding='utf-8') as testo:  # apre il file e crea un oggetto 'testo' iterabile

            taglia_testo(testo)

            for riga in testo:
                if riga.startswith('*** END OF THIS'):
                    break
                else:
                    elabora_riga(riga, lista_parole)

            return lista_parole
        
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

    for parola in riga.split():  # suddivide la riga in una lista di stringhe
        parola = parola.strip()
        parola = parola.lower()  # converti tutto in lettere minuscole (in realtà crea una nuova stringa dato che sono immutabili)
        lista.append(parola)  # aggiungi ciascuna parola alla lista

    return lista


def costruisci_catena_markov(lista_parole, lunghezza_prefisso=2):
    """Costruisce una catena di Markov a partire da una lista di parole
    
    lista_parole: lista di parole del testo
    lunghezza_prefisso: numero di parole nel prefisso (default 2)
    
    Ritorna un dizionario che mappa ciascun prefisso a una lista di possibili suffissi
    """
    # crea il dizionario speciale di tipo 'deafultdict'
    catena_markov = defaultdict(list)  
    # costrutto che ha questa funzione: quando si accede ad una chiave inesistente, 'defaultdict' creerà automaticamente una nuova lista vuota come valore associato a quella chiave; 
    # serve per evitare errori e per garantire che ogni chiave nel dizionario, quando acceduta per la prima volta, abbia una lista vuota come valore predefinito

    prefisso = ()  # crea una tupla vuota
    suffisso = []  # crea una lista vuota

    for i in range(len(lista_parole) - lunghezza_prefisso):
        prefisso = tuple(lista_parole[i:i + lunghezza_prefisso])  # crea un prefisso come tupla di lunghezza_prefisso, la tuple funge da chiave nel dizionario
        suffisso = lista_parole[i + lunghezza_prefisso]  # il suffisso è la parola che segue il prefisso
        catena_markov[prefisso].append(suffisso)  # aggiungiamo il suffisso alla lista dei possibili suffissi per il prefisso

    return dict(catena_markov)  # dict() converte in un dizionario ordinario




#ESECUZIONE
if __name__ == "__main__":
    testo_pulito = leggi_pulisci_testo('prova.txt')

    # uso l'espressione bool 'if testo_pulito:' per controllare la veridicità di una variabile; controlla che la variabile non sia 'None' o da altri valori "falsi", come ad esempio liste vuote; 
    # questo approccio è in linea con le convenzioni Python e rende il codice più chiaro e leggibile
    if testo_pulito:
        lunghezza_prefisso = 2
        catena_markov = costruisci_catena_markov(testo_pulito, lunghezza_prefisso)

        for chiave, valore in catena_markov.items():
            print(f"{chiave}: {valore}")