import random
from operator import index


class Domanda:
    def __init__(self, testo, livello, corretta, errate):
        self.testo = testo
        self.livello = livello
        self.corretta = corretta
        self.errate = errate

    def opzioni_random(self):
        opzioni = []
        for i in range(0, len(self.errate)):
            opzioni.append(self.errate[i])
        opzioni.append(self.corretta)
        random.shuffle(opzioni)
        return opzioni

class Giocatore:
    def __init__(self, nickname, punti):
        self.nickname = nickname
        self.punti = punti



lista_domande = []
with open("domande.txt", "r", encoding="utf-8") as file:
    righe = [line.strip() for line in file]
    for i in range(0, len(righe), 7):
        if i + 5 < len(righe):
            testo = righe[i]
            livello = int(righe[i+1])
            corretta = righe[i+2]
            errate = [righe[i+3], righe[i+4], righe[i+5]]

            nuova_domanda = Domanda(testo, livello, corretta, errate)
            lista_domande.append(nuova_domanda)

gioca = True
livello_attuale = 0
livello_massimo = max(lista_domande, key=lambda x: x.livello).livello
punti_totalizzati = 0

while gioca:
    domande_livello_attuale = [d for d in lista_domande if int(d.livello) == livello_attuale]
    domanda_scelta = random.choice(domande_livello_attuale)
    opzioni = domanda_scelta.opzioni_random()

    print(f"Livello {livello_attuale}) {domanda_scelta.testo}")
    for i in range(0, len(opzioni)):
        print(f"{i+1}. {opzioni[i]}")

    risposta_inserita = int(input("Inserisci la risposta: "))

    if opzioni[risposta_inserita-1] == domanda_scelta.corretta:
        punti_totalizzati += 1
        livello_attuale += 1
        print("Risposta corretta!")
        if (livello_attuale-1 == livello_massimo):
            gioca = False

    else:
        print(f"Risposta sbagliata! La risposta corretta era: {opzioni.index(domanda_scelta.corretta)+1}")
        gioca = False

print(f"Hai totalizzato: {punti_totalizzati} punti!")
nickname = input("Inserisci il tuo nickname: ")

classifica = []
with open("punti.txt", "r", encoding="utf-8") as file:
    righe = [line.strip() for line in file]
    for i in range(0, len(righe)):
        g = Giocatore(righe[i].split(' ')[0], righe[i].split(' ')[1])
        classifica.append(g)

classifica.append(Giocatore(nickname, punti_totalizzati))
classifica.sort(key=lambda x: int(x.punti), reverse=True)

with open("punti.txt", "w", encoding="utf-8") as file:
    for g in classifica:
        nickname = g.nickname
        punti = g.punti
        file.write(nickname+ ' ' +str(punti) + '\n')


