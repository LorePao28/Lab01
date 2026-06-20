import operator
import random
from operator import indexOf


class Domanda:
    def __init__(self, testo: str, difficoltà: int, risposta: str, opzioni: list):
        self.testo = testo
        self.difficoltà = difficoltà
        self.risposta = risposta
        self.opzioni = opzioni


# 1. Lettura file e memorizzazione delle domande
lista_domande = []
livello_max = -1
with open("domande.txt", "r", encoding="utf-8") as f:
    righe = f.read().splitlines()
    for i in range(0, len(righe), 7):
        domanda = Domanda(righe[i], righe[i+1], righe[i+2], [righe[i+3], righe[i+4], righe[i+5]])
        lista_domande.append(domanda)
        if int(domanda.difficoltà) > livello_max:
            livello_max = int(domanda.difficoltà)

# 2. Inizializzazione del gioco
flag = True
difficoltà_attuale = 0
punteggio = 0

# 3. Implementazione logica del gioco
while flag:
    domande_difficoltà_attuale = [] # lista delle sole domande con difficoltà del livello attuale
    for domanda in lista_domande:
        if int(domanda.difficoltà) == difficoltà_attuale:
            domande_difficoltà_attuale.append(domanda)

    domanda_scelta = random.choice(domande_difficoltà_attuale)  #scelta della domanda casualmente
    opzioni = domanda_scelta.opzioni
    opzioni.append(domanda_scelta.risposta)
    random.shuffle(opzioni)
    print(f"Livello {domanda_scelta.difficoltà}) {domanda_scelta.testo}")
    for i in range(0, len(opzioni)):
        print(f"{i+1}. {opzioni[i]}")
    input_utente = int(input("Inserisci la risposta: "))
    if opzioni[input_utente-1] == domanda_scelta.risposta:
        punteggio += 1
        difficoltà_attuale += 1
        print("Risposta corretta!")
        if difficoltà_attuale > livello_max:
            flag = False
    else:
        flag = False
        print(f"Risposta Sbagliata! La risposta corretta era: {indexOf(opzioni, domanda_scelta.risposta)+1}")

# 4. Conclusione del gioco
print(f"Hai totalizzato {punteggio} punti")
nickname = input("Inserisci il tuo nickname: ")
classifica = []
classifica.append((nickname, int(punteggio)))
with open("punti.txt", "r", encoding="utf-8") as f:
    for riga in f.read().splitlines():
        nickname = riga.split()[0]
        punteggio = riga.split()[1]
        classifica.append((nickname, int(punteggio)))

classifica.sort(key=operator.itemgetter(1), reverse=True)

with open("punti.txt", "w", encoding="utf-8") as f:
    for tupla in classifica:
        f.write(f"{tupla[0]} {tupla[1]}\n")

