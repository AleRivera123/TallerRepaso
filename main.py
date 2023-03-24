from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        for e in self.elementos:
            if e == elemento:
                return True
        return False

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for e in otro_conjunto.elementos:
            self.agregar_elemento(e)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = []
        for e1 in conjunto1.elementos:
            if conjunto2.contiene(e1):
                elementos_comunes.append(e1)
        nuevo_nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nuevo_nombre)
        for e in elementos_comunes:
            nuevo_conjunto.agregar_elemento(e)
        return nuevo_conjunto

    def __str__(self):
        nombres_elementos = [e.nombre for e in self.elementos]
        return f"Conjunto {self.nombre}: ({', '.join(nombres_elementos)})"