import string  # modulo string di python https://docs.python.org/3/library/string.html
from collections import defaultdict
import random


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
    """Legge da 'testo' finché non trova la riga che termina l'intestazione, in pratica rimuove l'intestazione fino alla riga specifica

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


def genera_testo_casuale(catena_markov, lunghezza_testo, lunghezza_prefisso=2):
    """Genera un testo casuale basato sulla catena di Markov data."""
    # la funzione random.choice necessita di una sequenza come argomento, tipicamente una lista o una tupla. Il medoto .keys() restituisce una vista delle chiavi 
    # del dizionario e le viste non supportano l'indicizzazione diretta, quindi random.choice non può lavorarci direttamente,
    # pertanto occorre convertire questa vista in una vera lista
    prefisso_iniziale = random.choice(list(catena_markov.keys()))  #  sceglie casualmente un prefisso iniziale

    # random.choice(list(catena_markov.keys())) restituisce una tupla, non una lista. 
    # La conversione in lista con list(prefisso_iniziale) è necessaria per poter costruire il testo_generato come una lista di parole
    testo_generato = list(prefisso_iniziale)

    # questo ciclo si ripete lunghezza_testo - lunghezza_prefisso volte per generare il testo. L'uso di - lunghezza_prefisso è dovuto al fatto che il testo_generato 
    # è inizialmente popolato con il prefisso_iniziale, che ha già una lunghezza pari a lunghezza_prefisso.
    for _ in range(lunghezza_testo - lunghezza_prefisso):
        suffissi_possibili = catena_markov.get(prefisso_iniziale)  # suffissi_possibili è una lista, non una singola stringa; il valore associato a una chiave nel dizionario catena_markov è sempre una lista di possibili suffissi, quindi catena_markov.get(prefisso_iniziale) restituisce una lista
        if not suffissi_possibili:  # se non ci sono più suffissi disponibili, termina il ciclo
            break
        prossimo_suffisso = random.choice(suffissi_possibili)
        testo_generato.append(prossimo_suffisso)
        prefisso_iniziale = tuple(testo_generato[-lunghezza_prefisso:])  # aggiorna il prefeisso: testo_generato[-lunghezza_prefisso:] significa: "Prendi gli ultimi 'lunghezza_prefisso' elementi dalla lista 'testo_generato'"; 
                                                                         # ad esempio 'testo_generato[-2:]' prende gli ultimi due elementi della lista testo_generato; queso viene convertiro in tupla perché occorre riaccedere ai prefissi ossia alle chiavi del dizionario che sono tuple

    return ' '.join(testo_generato)  # ' '.join(testo_generato) combina gli elementi della lista testo_generato in una singola stringa separata da spazi; questo serve per rendere il testo generato leggibile come unica stringa




#ESECUZIONE
if __name__ == "__main__":
    testo_pulito = leggi_pulisci_testo('emma11.txt')

    # uso l'espressione bool 'if testo_pulito:' per controllare la veridicità di una variabile; controlla che la variabile non sia 'None' o da altri valori "falsi", come ad esempio liste vuote; 
    # questo approccio è in linea con le convenzioni Python e rende il codice più chiaro e leggibile
    if testo_pulito:
        lunghezza_prefisso = int(input("Inserisci la lunghezza del prefisso (consigliato da 2 a 9): "))

        if lunghezza_prefisso <= 9:
            catena_markov = costruisci_catena_markov(testo_pulito, lunghezza_prefisso)

            for chiave, valore in catena_markov.items():
                print(f"{chiave}: {valore}")

            lunghezza_testo = int(input("\nInserisci la lunghezza del testo desiderata (consigliato non più di 1000 parole): "))
            testo_generato = genera_testo_casuale(catena_markov, lunghezza_testo, lunghezza_prefisso)
            print("\nTesto generato:")
            print(testo_generato)
        else:
            print("Il prefisso inserito è troppo lungo e compromette il risultato dell'analisi.")        
    else:
        print("Il testo è vuoto o non è stato letto correttamente.")  