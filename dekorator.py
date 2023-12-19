def moja_funkcja(func):
    print("start dekoratora")
    func()
    print("koniec dekoratora")

@moja_funkcja
def druga_funkcja():
    print("Jestem inna funkcja")

druga_funkcja()
    