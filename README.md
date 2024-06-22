# analisi-di-markov_py
Esercitazione sull'analisi di Markov applicata su un file di testo per descrivere la probabilità nella sequenza di parole

## Descrizione del progetto
In questa esercitazione scriverò un programma che legge un file di testo ed esegue l'analisi di Markov che permette di analizzare la relazione tra parole successive. Data una sequenza di parole, descrive la probabilità della parola che potrebbe seguire. Questa è solo una semplice applicazione di alcune delle teorie sviluppate dal matematico [Markov](https://it.wikipedia.org/wiki/Andrej_Andreevi%C4%8D_Markov_(1856-1922)), i cui contributi vanno ben al di là di questa semplice trattazione.

Il file di testo che verrà processato e analizzato è relativo al romanzo *Emma* della scrittrice [Jane Austen](https://it.wikipedia.org/wiki/Jane_Austen). Il file fa riferimento al noto [Progetto Gutenberg](https://it.wikipedia.org/wiki/Progetto_Gutenberg) di e-book open source che tuttavia, alla data del presente progetto, sembra irrangiungibile dal browser forse a causa di un errore nel protocollo http. Pertanto ho scaricato il file `emma11.txt` dalle risorse libere di [Interne Archive](https://archive.org/details/emma00158gut); si prega di rispettare i termini di licenza e riuso previsti dal sito.

### Sintesi del codice
Le prime funzioni definite `leggi_pulisci_testo()`, `taglia_testo()`, `elabora_riga()` sono preposte ad aprire il file di testo cercando di gestire semplici casi di errore, rimuovere le parti di testo superflue ed elaborare il testo affinché venga convertito in una lista di parole.
Segue la funzione `costruisci_catena_markov()` che prende questa lista di parole e un parametro relativo alla lunghezza stabilita per i prefissi, e costruisce un dizionario in cui le chiavi sono i prefissi della lunghezza stabilita dall'utente e i valori sono rappresentati dai possibili suffissi che seguono i prefissi.
Infine, ho aggiunto una funzione `genera_testo_casuale()` che sfruttando le pontenzialità del modulo Python `random` crea un testo casuale basato sull'analisi di Markov.
Per una spiegazione dettagliata di come opera il codice si rinvia ai commenti interni, forse addirittura sovrabbondanti! :dizzy_face: Scusatemi al riguardo, ma ho sviluppato il progetto a scopo didattico per principianti, quale sono io :sweat_smile:

### Considerazioni finali
Lo scopo finale di questo progetto era infine capire cosa succede se si aumenta la lunghezza del prefisso; il testo sarà sintatticamente e semanticamente più o meno sensato? Dopo aver effettuato alcuni testi confermo che sì, più il prefisso è lungo più il testo generato sembra di senso compiuto. Tuttavia ho limitato il numero di parole per prefisso a 9, altrimenti andando oltre l'esperimento perde di significato in quando i prefissi stessi diventavano già frasi di senso compiuto, ovviamente. Questo avviene perché un prefisso più lungo consente al modello di catturare relazioni più specifiche tra le parole nel testo originale. 
In conclusione, l'aumento della lunghezza del prefisso nella tua implementazione della catena di Markov può sicuramente migliorare la qualità semantica e logica del testo generato.
**Piccolo bug**: nei casi in cui la lunghezza del prefisso è bassa, 2 o 3 parole, è possibile che alcuni suffissi siano più di una singola parola. In questo modo può succedere che andando via via ad aggiungere i suffissi al testo generato, lo stesso testo risulti di qualche parola più lungo rispetto al valore inserito dall'utente. Tuttavia ai fini dell'esperimento mi è sembrato un bug tollerabile; se qualcuno ha suggerimenti su come migliorare è benvenuto :blush:


### Licenza
Questo progetto è liberamente utilizzabile e replicabile, nel rispetto dei termini della licenza [CC 4.0](https://creativecommons.org/licenses/by/4.0/).
