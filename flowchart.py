print("accade l'incidente")
print("il cliente chiama il meccanico")
print("il meccanico arriva")
print()

c1=input("il meccanico può trasportare l'auto?")
if c1=="sì":
    print("l'automobile è straportata in officina")
else:
    print("il meccanico torna in offina senza auto")
print()
print("raccolta dati")
print()
print("Auto: targa,numero telaio")
print()
print("Proprietario: nome,cognome,cod. fiscale,data nascita,residenza")
print()
print("valutazione rischi")
print("inizio lavori")
print()

c2=input("pezzi ricambio in magazzino?")
while True:
    if c2=="sì":
        break
    else:
        print("ordinazione pezzi")
        c3=input("ci sono altri lavori?")
        if c3=="sì":
            continue
        else:
            print("blocco lavori")
            print("arrivo pezzi")
            break
print()            
print("continuazione lavori") 
print("fine riparazione")
print()

c4=input("cliente vuole altre modifiche?")
while True:
    if c2=="sì":
        break
    else:
        print("ordinazione pezzi")
        c3=input("ci sono altri lavori?")
        if c3=="sì":
            break
        else:
            print("blocco lavori")
            print("arrivo pezzi")
            break
print()
print("continuazione lavori")
print("fine modifica")
print("fattura")
print("calcolo spesa per il cliente")
print("pagamento")
print()

c4=input("cliente paga con carta di credito?")
while True:
    if c2=="sì":
        break
    else:
        print("contanti")
        break
print()
print("fine pagamento")
print("il cliente si ripende l'auto riparata")
