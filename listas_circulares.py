class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.next = None

class ListaCircularSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_ultimo(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.next = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.next = Nodo(dato)
            self.ultimo.next = self.primero

    def recorrido (self):
        aux = self.primero
        while aux.next: # != self.primero:
            print(aux.dato)
            aux = aux.next
            if aux == self.primero:
                break
        #print(aux.dato)

    def eliminar_ultimo(self):
        if self.vacia():
            print("Lista Vacia")
        elif self.primero == self.ultimo:
            self.primero = self.next = self.primero
        else:
            aux = self.primero
            while aux.next != self.ultimo:
                aux = aux.next
            aux.next = self.primero
            self.ultimo = aux

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.next = self.primero
        else:
            aux = Nodo(dato)
            aux.next = self.primero
            self.primero = aux
            self.ultimo.next = self.primero

    def eliminar_inicio(self):
        if self.vacia():
            print("Lista Vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.next
            self.ultimo.next = self.primero

try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCircularSimple

        while opcion != 7:
            print("Lista Circular Simple: \n1. Agregar Ultimo\n2. Eliminar Ultimo\n3. Lista Vacia?\n4. Agregar Inicio\n5. Eliminar Inicio\n6. Mostrar\n7. Salir ")
            opcion = int(input("Ingrese Opcion: "))

            if opcion == 1:
                dato = input("ingrese un dato: ")
                lista.agregar_ultimo(dato)
            elif opcion == 2:
                lista.eliminar_ultimo()
            elif opcion == 3:
                print("si" if lista.vacia()else "No")
            elif opcion == 4:
                dato = input("ingrese un dato: ")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.eliminar_inicio()
            elif opcion == 6:
                lista.recorrido
            elif opcion == 7:
                print("FIN")
            else:
                print("agrege un dato correcto: ")
except Exception as e:
    print(e)