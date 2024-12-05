class Inhaber:
    def __init__(self, name, geburtsdatum):
        self.name = name
        self.konten = []
    
    def __str__(self):
        return f"Inhaber: {self.name} / Konten: {self.konten}"                                                   

    def alle_konten_anzeigen(self):
        print("Alle Konten von", self.name)
        for konto in self.konten:
            print("-", konto) # Hier wird die __str__-Methode von Konto aufgerufen

class Konto:
    def __init__(self, kontonummer, kontostand, inhaber, dispo=0):
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self.inhaber = inhaber
        self.dispo = dispo
        self.inhaber.konten.append(self)
    
    def __str__(self):
        return f"Kontonummer: {self.kontonummer} / Kontostand: {self.kontostand} / Inhaber: {self.inhaber.name} / Dispo: {self.dispo}"

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
        else:
            print("Nur positive Beträge sind erlaubt.")

    def abheben(self, betrag):
        if self.kontostand + self.dispo >= betrag:
            self.kontostand -= betrag
        else:
            print("Nicht genug Geld auf dem Konto.")
    
    def ueberweisen(self, zielkonto, betrag):
        if betrag < 0:
            print("Nur positive Beträge sind erlaubt.")
            return # Beenden der Funktion
        if self.kontostand + self.dispo >= betrag:
            self.kontostand -= betrag
            zielkonto.einzahlen(betrag)
        else:
            print("Nicht genug Geld auf dem Konto.")


class Jugendkonto(Konto):
    def __init__(self, kontonummer, kontostand, inhaber):
        super().__init__(kontonummer, kontostand, inhaber, 0) # Dispo ist 0, weil Jugendliche keinen Dispo haben dürfen.


class Sparkonto(Konto):
    def __init__(self, kontonummer, kontostand, inhaber, zinsen):
        super().__init__(kontonummer, kontostand, inhaber, 0) # Dispo ist 0, weil Sparkonten keinen Dispo haben dürfen.
        self.zinsen = zinsen
    
    def zinsen_berechnen(self):
        self.kontostand += self.kontostand * self.zinsen


if __name__ == "__main__":
    inhaber1 = Inhaber("Max Mustermann", "01.01.2000")
    inhaber2 = Inhaber("Erika Mustermann", "01.01.2005")

    print("Inhaber1:", inhaber1)
    print("Inhaber2:", inhaber2)
    print() # Leerzeile

    konto1 = Konto("123456", 1000, inhaber1, 500)
    konto2 = Jugendkonto("654321", 500, inhaber2)
    konto3 = Sparkonto("987654", 2000, inhaber1, 0.05)

    print("Konto1:", konto1)
    print("Konto2:", konto2)
    print("Konto3:", konto3)
    print() # Leerzeile

    # Testen, ob wir Geld einzahlen können
    print("Einzahlen auf Konto1:")
    print("Vorher: ", konto1)
    konto1.einzahlen(500)
    print("Nachher:", konto1)
    print() # Leerzeile

    # Testen, ob wir Geld abheben können
    print("Abheben von Konto2:")
    print("Vorher: ", konto2)
    konto2.abheben(100)
    print("Nachher:", konto2)
    print() # Leerzeile

    # Testen, ob wir über die Dispo-Grenze gehen können
    print("Konto 1 über die Dispo-Grenze belasten:")
    print("Vorher: ", konto1)
    konto1.abheben(3000)
    print("Nachher:", konto1)
    print() # Leerzeile

    # Testen, ob wir Geld überweisen können
    print("Geld von Konto1 auf Konto2 überweisen:")
    print("Vorher:")
    print("Konto1:", konto1)
    print("Konto2:", konto2)
    konto1.ueberweisen(konto2, 500)
    print("Nachher:")
    print("Konto1:", konto1)
    print("Konto2:", konto2)
    print() # Leerzeile

    # Testen, ob wir Zinsen berechnen können
    print("Zinsen berechnen:")
    print("Vorher: ", konto3)
    konto3.zinsen_berechnen()
    print("Nachher:", konto3)
    print() # Leerzeile

    # Testen, ob wir einen negativen Betrag überweisen können
    print("Negativen Betrag überweisen:")
    print("Vorher:")
    print("Konto1:", konto1)
    print("Konto2:", konto2)
    konto1.ueberweisen(konto2, -500)
    print("Nachher:")
    print("Konto1:", konto1)
    print("Konto2:", konto2)
    print() # Leerzeile

    # Nochmal alle Konten anzeigen
    inhaber1.alle_konten_anzeigen()
    inhaber2.alle_konten_anzeigen()
