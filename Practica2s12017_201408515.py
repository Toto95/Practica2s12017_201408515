from flask import Flask, request
app = Flask("WebServiceCorreos")

# nodos para las estructuras
class nodoCola:
    def __init__(self, numero, siguiente=None):
        self.numero = numero
        self.siguiente = siguiente

    def __str__(self):
        return str(self.numero)
class nodoLista:
    def __init__(self, numero, siguiente=None):
        self.numero = numero
        self.siguiente = siguiente

    def __str__(self):
        return str(self.numero)
class nodoCorreo:
    siguiente = None
    anterior = None
    direccion = ""

    def __init__(self, direcc):
        self.siguiente
        self.anterior
        self.direccion = direcc
class nodoMatriz:
    arriba = None
    abajo = None
    izquierda = None
    derecha = None
    lista = None
    dominio = ""
    inicialDireccion = ""

    def __init__(self, letra, dom):
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        self.dominio = dom
        self.inicialDireccion = letra
        self.lista = listaAsociadaNodoMatriz()
class nodoCabezaHorizontal:
    siguiente = None
    anterior = None
    domini = ""
    lista = None

    def __init__(self, valor):
        self.siguiente = None
        self.anterior = None
        self.domini = valor
        self.lista = listaAsociadaCabeceraHorizontal()
class nodoCabezaVertical:
    siguiente = None
    anterior = None
    primerLetra = ""
    lista = None

    def __init__(self, valor):
        self.siguiente = None
        self.anterior = None
        self.primerLetra = valor
        self.lista = listaAsociadaCabeceraVertical()
# estructuras basicas
class listaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, nuevo):
        nodo = nodoLista(nuevo)
        if self.cabeza == None:
            nodo.siguiente = None
            self.cabeza = nodo
            self.cola = nodo
        else:
            self.cola.siguiente = nodo
            self.cola = nodo

    def imprimirLista(self):
        if self.cabeza == None:
            print "vacio"
            return

        self.temporal = self.cabeza
        while self.temporal != None:
            print self.temporal
            self.temporal = self.temporal.siguiente

    def eliminarPorIndice(self, numero):
        if self.cabeza == None:
            print("lita vacia")
            return

        temporal = temporal2 = self.cabeza
        contador = 0
        while temporal != None:
            if contador == numero:
                print("encuentra el indice")
                if temporal == self.cabeza:
                    self.cabeza = self.cabeza.siguiente
                elif temporal == self.cola:
                    temporal2.siguiente = None
                    self.cola = temporal2
                else:
                    temporal2.siguiente = temporal.siguiente
                return
            else:
                temporal2 = temporal
                temporal = temporal.siguiente
                contador = contador + 1
    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)
    def reporteLista(self):
        if self.cabeza == None:
            print "vacio"
            return
        file = open("C:\Users\Ottoniel\Desktop\ytemporal\lista.dot", "w")
        file.write("digraph G{\n")
        temporal = self.cabeza
        while temporal != None:
            file.write("nodo" + self.obtenerHASH(temporal) + "[label = \"" + str(
                temporal) + "\", style = filled, fillcolor = \"#FF4000\"]\n")
            if temporal.siguiente != None:
                file.write("nodo" + self.obtenerHASH(temporal) + " -> nodo" + self.obtenerHASH(temporal.siguiente) + "\n")
            temporal = temporal.siguiente
        file.write("}\n")
        file.close()


    def buscar(self, numero):
        contador = 0
        if self.cabeza == None:
            return "LA LISTA ESTA VACIA"
        temporal = self.cabeza
        while temporal != None:
            if temporal.numero == numero:
                return "EL DATO SE ENCUENTRA EN EL INDICE " + str(contador)
            temporal = temporal.siguiente
            contador = contador + 1
        return "NO SE ENCONTRO EL DATO"
class pila:
    top = None

    def __init__(self):
        self.top = None
    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)
    def insertar(self, num):
        nuevo = nodoCola(num)
        if self.top == None:
            self.top = nuevo
        else:
            nuevo.siguiente = self.top
            self.top = nuevo

    def pop(self):
        if self.top == None:
            return "Pila Vacia"
        temporal = self.top
        self.top = self.top.siguiente
        return str(temporal.numero)

    def imprimirPila(self):
        if self.top == None:
            print "Pila Vacia"
            return
        temporal = self.top
        while temporal != None:
            print temporal
            temporal = temporal.siguiente

    def reportePila(self):
        if self.top == None:
            return

        file = open("C:\Users\Ottoniel\Desktop\ytemporal\pila.dot", "w")
        file.write("digraph G{\n")
        temporal = self.top
        while temporal != None:
            file.write("nodo" + self.obtenerHASH(temporal) + "[label = \"" + str(
                temporal) + "\", style = filled, fillcolor = \"#FF4000\"]\n")
            if temporal.siguiente != None:
                file.write("nodo" + self.obtenerHASH(temporal) + " -> nodo" + self.obtenerHASH(temporal.siguiente) + "\n")
            temporal = temporal.siguiente
        file.write("}\n")
        file.close()
        #os.system("dot -Tpng pila.dot > pila.png")
class cola:
    cabeza = None
    cola = None

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, numero):
        nuevo = nodoCola(numero)
        nuevo.siguiente = None
        if self.cabeza == None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def eliminar(self):
        if self.cabeza == None:
            return "Cola vacia"
        temporal = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return str(temporal.numero)

    def mostrar(self):
        if self.cabeza == None:
            print "vacio"
            return
        temporal = self.cabeza
        while temporal != None:
            print temporal
            temporal = temporal.siguiente
    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)
    def reporteCola(self):
        if self.cabeza == None:
            return
        file = open("C:\Users\Ottoniel\Desktop\ytemporal\cola.dot", "w")
        file.write("digraph G{\n")
        temporal = self.cabeza
        while temporal != None:
            file.write("nodo" + self.obtenerHASH(temporal) + "[label = \"" + str(
                temporal) + "\", style = filled, fillcolor = \"#FF4000\"]\n")
            if temporal.siguiente != None:
                file.write("nodo" + self.obtenerHASH(temporal) + " -> nodo" + self.obtenerHASH(temporal.siguiente) + "\n")
            temporal = temporal.siguiente
        file.write("}\n")
        file.close()
        #os.system("dot -Tpng cola.dot > cola.png")
# estructuras para la matriz
class listaAsociadaNodoMatriz:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    # metodo para insertar recibe como parametro nuevo que es un nodoCorreo
    def insertar(self, nuevo):
        print "inserto"
        if self.primero == None:
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            nuevo.siguiente = None
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def eliminar(self, direccion):
        if self.primero == None:
            return

        temporal = self.primero
        while temporal != None:
            if temporal.direccion == direccion:
                if self.primero == temporal and temporal.siguiente != None:
                    self.primero.siguiente.anterior = None
                    self.primero = self.primero.siguiente
                    return
                elif self.primero == temporal and temporal.siguiente == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.anterior
                    self.ultimo.siguiente = None
                    return
                else:
                    temporal.siguiente.anterior = temporal.anterior
                    temporal.anterior.siguiente = temporal.siguiente
                    return
            else:
                temporal = temporal.siguiente
class listaAsociadaCabeceraHorizontal:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, nuevo):
        if (self.primero == None):
            self.primero = self.ultimo = nuevo
            return

        if nuevo.inicialDireccion < self.primero.inicialDireccion:
            nuevo.abajo = self.primero
            nuevo.arriba = None
            self.primero.arriba = nuevo
            self.primero = nuevo
            return
        elif nuevo.inicialDireccion > self.ultimo.inicialDireccion:
            nuevo.abajo = None
            nuevo.arriba = self.ultimo
            self.ultimo.abajo = nuevo
            self.ultimo = nuevo
            return
        else:
            temporal = self.primero
            while temporal != None:
                if temporal.inicialDireccion > nuevo.inicialDireccion:
                    nuevo.arriba = temporal.arriba
                    nuevo.abajo = temporal
                    temporal.arriba.abajo = nuevo
                    temporal.arriba = nuevo
                    return
                temporal = temporal.abajo

    # recibe como parametro y que es la letra inicial de la direccion de correo
    def eliminar(self, y):
        if self.primero == None:
            return

        temporal = self.primero
        while temporal != None:
            if temporal.inicialDireccion == y:
                if self.primero == temporal and temporal.abajo != None:
                    self.primero.abajo.arriba = None
                    self.primero = self.primero.abajo
                    return
                elif self.primero == temporal and temporal.abajo == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.arriba
                    self.ultimo.abajo = None
                    return
                else:
                    temporal.abajo.arriba = temporal.arriba
                    temporal.arriba.abajo = temporal.abajo
                    return
            else:
                temporal = temporal.abajo
class listaAsociadaCabeceraVertical:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    # nuevo es un nodo matriz
    def agregar(self, nuevo):
        if self.primero == None:
            self.primero = self.ultimo = nuevo
            return

        if nuevo.dominio < self.primero.dominio:
            nuevo.derecha = self.primero
            nuevo.izquierda = None
            self.primero.izquierda = nuevo
            self.primero = nuevo
            return
        elif nuevo.dominio > self.ultimo.dominio:
            nuevo.derecha = None
            nuevo.izquierda = self.ultimo
            self.ultimo.derecha = nuevo
            self.ultimo = nuevo
            return
        else:
            temporal = self.primero
            while temporal != None:
                if temporal.dominio > nuevo.dominio:
                    nuevo.izquierda = temporal.izquierda
                    nuevo.derecha = temporal
                    temporal.izquierda.derecha = nuevo
                    temporal.izquierda = nuevo
                    return
                temporal = temporal.derecha

    # recibe como parametro x que es el dominio del correo
    def eliminar(self, x):
        if self.primero == None:
            return

        temporal = self.primero
        while temporal != None:
            if temporal.dominio == x:
                if self.primero == temporal and temporal.derecha != None:
                    self.primero.derecha.izquierda = None
                    self.primero = self.primero.derecha
                    return
                elif self.primero == temporal and temporal.derecha == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.izquierda
                    self.ultimo.derecha = None
                    return
                else:
                    temporal.derecha.izquierda = temporal.izquierda
                    temporal.izquierda.derecha = temporal.derecha
                    return
            else:
                temporal = temporal.derecha
class listaCabecerasHorizontales:
    listaVertical = None

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.listaVertical = listaAsociadaCabeceraVertical()

    def insertar(self, dominio):
        nuevo = nodoCabezaHorizontal(dominio)
        if self.primero == None:
            self.primero = self.ultimo = nuevo
            return

        if nuevo.domini < self.primero.domini:
            nuevo.siguiente = self.primero
            nuevo.anterior = None
            self.primero.anterior = nuevo
            self.primero = nuevo
            return
        elif nuevo.domini > self.ultimo.domini:
            nuevo.siguiente = None
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            return
        else:
            temporal = self.primero
            while temporal != None:
                if temporal.domini > nuevo.domini:
                    nuevo.anterior = temporal.anterior
                    nuevo.siguiente = temporal
                    temporal.anterior.siguiente = nuevo
                    temporal.anterior = nuevo
                    return
                temporal = temporal.siguiente

    def eliminar(self, dominio):
        if self.primero == None:
            return
        temporal = self.primero
        while temporal != None:
            if temporal.domini == dominio:
                if self.primero == temporal and temporal.siguiente != None:
                    self.primero.siguiente.anterior = None
                    self.primero = self.primero.siguiente
                    return
                elif self.primero == temporal and temporal.siguiente == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.anterior
                    self.ultimo.siguiente = None
                    return
                else:
                    temporal.siguiente.anterior = temporal.anterior
                    temporal.anterior.siguiente = temporal.siguiente
                    return
            else:
                temporal = temporal.siguiente

    def existeH(self, dom):
        if self.primero == None:
            return False
        temporal = self.primero
        while temporal != None:
            if temporal.domini == dom:
                return True
            temporal = temporal.siguiente
        return False

    def existeNodoMatriz(self, dom, letra):
        if self.primero == None:
            return False
        temporal = self.primero
        while temporal != None:
            if temporal.domini == dom:
                aux = temporal.lista.primero
                while aux != None:
                    if aux.inicialDireccion == letra:
                        return True
                    aux = aux.abajo
            temporal = temporal.siguiente
        return False

    def insertarDirectoANodo(self, di, do):
        if self.primero == None:
            return
        tm = self.primero
        while tm != None:
            if tm.domini == do:
                aux = tm.lista.primero
                while aux != None:
                    if aux.inicialDireccion == di[0]:
                        nu = nodoCorreo(di + do)
                        aux.lista.insertar(nu)
                    aux = aux.abajo
            tm = tm.siguiente

    def eliminarEnNodo(self, di, do):
        bandera = False
        if self.primero == None:
            return
        tm = self.primero
        while tm != None:
            if tm.domini == do:
                aux = tm.lista.primero
                while aux != None:
                    if aux.inicialDireccion == di[0]:
                        aux.lista.eliminar(di + do)
                        print "elimino "+ di+ do
                        if aux.lista.primero == None:
                            bandera = True
                            return bandera
                    aux = aux.abajo
            tm = tm.siguiente
        return bandera

    def noTieneNada(self, domin):
        temporal = self.primero
        while temporal != None:
            if temporal.domini == domin:
                if temporal.lista.primero == None:
                    return True
            temporal = temporal.siguiente
        return False
class listaCabecerasVerticales:
    concatenador = ""
    bandera = False

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, primerLetra):
        nuevo = nodoCabezaVertical(primerLetra)
        if self.primero == None:
            self.primero = self.ultimo = nuevo
            return

        if nuevo.primerLetra < self.primero.primerLetra:
            nuevo.siguiente = self.primero
            nuevo.anterior = None
            self.primero.anterior = nuevo
            self.primero = nuevo
            return
        elif nuevo.primerLetra > self.ultimo.primerLetra:
            nuevo.siguiente = None
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            return
        else:
            temporal = self.primero
            while temporal != None:
                if temporal.primerLetra > nuevo.primerLetra:
                    nuevo.anterior = temporal.anterior
                    nuevo.siguiente = temporal
                    temporal.anterior.siguiente = nuevo
                    temporal.anterior = nuevo
                    return
                temporal = temporal.siguiente

    def eliminar(self, primerLetra):
        if self.primero == None:
            return

        temporal = self.primero
        while temporal != None:
            if temporal.primerLetra == primerLetra:
                if self.primero == temporal and temporal.siguiente != None:
                    self.primero.siguiente.anterior = None
                    self.primero = self.primero.siguiente
                    return
                elif self.primero == temporal and temporal.siguiente == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.anterior
                    self.ultimo.siguiente = None
                    return
                else:
                    temporal.siguiente.anterior = temporal.anterior
                    temporal.anterior.siguiente = temporal.siguiente
                    return
            else:
                temporal = temporal.siguiente

    def concatenar(self, pedaso):
        if self.bandera == False:
            self.concatenador = self.concatenador + pedaso
            self.bandera = True
        else:
            self.concatenador = self.concatenador + "," + pedaso

    def buscarLetra(self, letra):
        if self.primero == None:
            return "no existe"
        temporal = self.primero
        while temporal != None:
            if temporal.primerLetra == letra:
                aux = temporal.lista.primero
                while aux != None:
                    aux2 = aux.lista.primero
                    while aux2 != None:
                        self.concatenar(aux2.direccion)
                        aux2 = aux2.siguiente
                    aux = aux.siguiente
                resultado = self.concatenador
                self.concatenador = ""
                self.bandera = False
                return resultado
            temporal = temporal.siguiente

    def existeV(self, indi):
        if self.primero == None:
            return False
        temporal = self.primero
        while temporal != None:
            if temporal.primerLetra == indi:
                return True
            temporal = temporal.siguiente
        return False

    def noTieneNada(self, indice):
        temporal = self.primero
        while temporal != None:
            if temporal.primerLetra == indice:
                if temporal.lista.primero == None:
                    return True
            temporal = temporal.siguiente
        return False
class matriz:
    def __init__(self):
        self.verticales = listaCabecerasVerticales()
        self.horizontales = listaCabecerasHorizontales()

    def insertar(self, cad):

        pedasos = cad.split("@")
        dir = pedasos[0]
        do = "@" + pedasos[1]
        caracterUno = dir[0]
        if self.verticales.existeV(caracterUno) == False:
            self.verticales.insertar(caracterUno)

        if self.horizontales.existeH(do) == False:
            self.horizontales.insertar(do)

        if self.horizontales.existeNodoMatriz(do, caracterUno) == False:
            nodom = nodoMatriz(caracterUno, do)
            tm = self.horizontales.primero
            while tm != None:
                if tm.domini == do:
                    tm.lista.agregar(nodom)
                    break
                tm = tm.siguiente
            tm2 = self.verticales.primero
            while tm2 != None:
                if tm2.primerLetra == caracterUno:
                    tm2.lista.agregar(nodom)
                    break
                tm2 = tm2.siguiente

        self.horizontales.insertarDirectoANodo(dir, do)

    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)

    def buscarPorLetra(self, letra):
        concatenadora = ""
        temporal = self.verticales.primero
        while temporal != None:
            if temporal.primerLetra == letra:
                aux = temporal.lista.primero
                while aux != None:
                    aux2 = aux.lista.primero
                    while aux2 != None:
                        concatenadora = concatenadora + "," + aux2.direccion
                        aux2 = aux2.siguiente
                    aux = aux.derecha
            temporal = temporal.siguiente
        return concatenadora

    def graficarMatriz(self):
        if self.horizontales.primero == None or self.verticales.primero == None:
            return
        cabeza = self.horizontales.primero
        lateral = self.verticales.primero
        file = open("C:\Users\Ottoniel\Desktop\ytemporal\matriz.dot", "w")
        file.write("digraph G{\n")
        file.write("nodoR[label=\"Inicio\", style = filled, fillcolor = \"#FF4000\", group = rr]\n")
        file.write("{rank = same; nodoR nodoc" + self.obtenerHASH(cabeza) + "}\n")
        file.write("nodoR -> nodoc" + self.obtenerHASH(cabeza) + "\n")
        # graficando cabezas
        while cabeza != None:

            file.write("nodoc" + self.obtenerHASH(cabeza) + "[label = \"" + cabeza.domini + "\", style = filled, fillcolor = \"#FF4000\", group = r" + self.obtenerHASH(cabeza) + "]\n")
            if cabeza.siguiente != None:
                file.write("{rank = same; nodoc" + self.obtenerHASH(cabeza) + " nodoc" + self.obtenerHASH(cabeza.siguiente) + "}\n")
                file.write("nodoc" + self.obtenerHASH(cabeza) + " -> nodoc" + self.obtenerHASH(cabeza.siguiente) + "\n")
            if cabeza.anterior != None:
                file.write("{rank = same; nodoc" + self.obtenerHASH(cabeza) + " nodoc" + self.obtenerHASH(
                    cabeza.anterior) + "}\n")
                file.write("nodoc" + self.obtenerHASH(cabeza) + " -> nodoc" + self.obtenerHASH(cabeza.anterior) + "\n")
            cabeza = cabeza.siguiente
        file.write("nodoR -> nodol" + self.obtenerHASH(lateral) + "\n")
        while lateral != None:
            file.write("nodol" + self.obtenerHASH(
                lateral) + "[label = \"" + lateral.primerLetra + "\", style = filled, fillcolor = \"#FF4000\", group = rr]\n")
            if lateral.siguiente != None:
                file.write(
                    "nodol" + self.obtenerHASH(lateral) + " -> nodol" + self.obtenerHASH(lateral.siguiente) + "\n")
            if lateral.anterior != None:
                file.write(
                    "nodol" + self.obtenerHASH(lateral) + " -> nodol" + self.obtenerHASH(lateral.anterior) + "\n")
            lateral = lateral.siguiente
        cabeza = self.horizontales.primero
        while cabeza != None:
            enMatriz = cabeza.lista.primero
            file.write("subgraph s" + self.obtenerHASH(cabeza) + "{\n")
            while enMatriz != None:
                file.write("nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                    enMatriz) + "[label = \"" + enMatriz.lista.primero.direccion + "\", style = filled, fillcolor = \"#FF4000\", group = r" + self.obtenerHASH(
                    cabeza) + "]\n")
                if enMatriz.lista.primero.siguiente != None:
                    tm = enMatriz.lista.primero.siguiente
                    file.write("nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + " -> nodoS" + self.obtenerHASH(tm) + "\n")
                    file.write("nodoS" + self.obtenerHASH(tm) + " -> " + "nodoc" + self.obtenerHASH(
                        enMatriz) + "l" + self.obtenerHASH(enMatriz) + "\n")
                    while tm != None:
                        file.write("nodoS" + self.obtenerHASH(
                            tm) + "[label = \"" + tm.direccion + "\", style = filled, fillcolor = \"#00FF00\"]\n")
                        if tm.siguiente != None:
                            file.write(
                                "nodoS" + self.obtenerHASH(tm) + " -> nodoS" + self.obtenerHASH(tm.siguiente) + "\n")
                            file.write(
                                "nodoS" + self.obtenerHASH(tm.siguiente) + "-> nodoS" + self.obtenerHASH(tm) + "\n")
                        tm = tm.siguiente
                enMatriz = enMatriz.abajo
            file.write("}\n")
            cabeza = cabeza.siguiente
        cabeza = self.horizontales.primero
        while cabeza != None:
            enMatriz = cabeza.lista.primero
            while enMatriz != None:
                if enMatriz.derecha != None:
                    file.write("nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + " -> " + "nodoc" + self.obtenerHASH(enMatriz.derecha) + "l" + self.obtenerHASH(
                        enMatriz.derecha) + "\n")
                    file.write("{rank = same; " + " nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + " " + "nodoc" + self.obtenerHASH(enMatriz.derecha) + "l" + self.obtenerHASH(
                        enMatriz.derecha) + "}\n")
                if enMatriz.izquierda != None:
                    file.write("nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + " -> " + "nodoc" + self.obtenerHASH(enMatriz.izquierda) + "l" + self.obtenerHASH(
                        enMatriz.izquierda) + "\n")
                    file.write("{rank = same; " + " nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + " " + "nodoc" + self.obtenerHASH(enMatriz.izquierda) + "l" + self.obtenerHASH(
                        enMatriz.izquierda) + "}\n")
                if enMatriz.abajo != None:
                    file.write("nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + " -> " + "nodoc" + self.obtenerHASH(enMatriz.abajo) + "l" + self.obtenerHASH(
                        enMatriz.abajo) + "\n")
                    # file.write("{rank = same; " + " nodoc" + enMatriz.dominio + "l" + enMatriz.inicialDireccion + " " + "nodoc" + enMatriz.arriba.dominio + "l" + enMatriz.arriba.inicialDireccion)
                if enMatriz.arriba != None:
                    file.write("nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + " -> " + "nodoc" + self.obtenerHASH(enMatriz.arriba) + "l" + self.obtenerHASH(
                        enMatriz.arriba) + "\n")
                    # file.write("{rank = same; " + " nodoc" + enMatriz.dominio + "l" + enMatriz.inicialDireccion + " " + "nodoc" + enMatriz.arriba.dominio + "l" + enMatriz.arriba.inicialDireccion)
                enMatriz = enMatriz.abajo
            cabeza = cabeza.siguiente

        lateral = self.verticales.primero
        while lateral != None:
            enMatriz = lateral.lista.primero
            if lateral.lista.primero != None:
                file.write("nodol" + self.obtenerHASH(lateral) + " -> " + "nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(enMatriz) + "\n")
                file.write("nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(enMatriz)+ " -> " + "nodol" + self.obtenerHASH(lateral)  + "\n")
                file.write("{rank = same; " + "nodol" + self.obtenerHASH(lateral) + " " + "nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(enMatriz) + "}\n")
            lateral = lateral.siguiente
        # file.write("}\n")
        cabeza = self.horizontales.primero
        while cabeza != None:
            enMatriz = cabeza.lista.primero
            if cabeza.lista.primero != None:
                file.write("nodoc" + self.obtenerHASH(cabeza) + " -> nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(enMatriz) + "\n")
                file.write("nodoc"+self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(enMatriz) + " -> " + "nodoc" + self.obtenerHASH(cabeza) + "\n")
            cabeza = cabeza.siguiente

        file.write("}\n")
        file.close()
        #os.system("dot -Tpng matriz.dot > matriz.png")

    def buscarPorDominio(self, dominio):
        concatenadora = " "
        temporal = self.horizontales.primero
        while temporal != None:
            if temporal.domini == dominio:
                aux = temporal.lista.primero
                while aux != None:
                    aux2 = aux.lista.primero
                    while aux2 != None:
                        concatenadora = concatenadora + "," + aux2.direccion
                        aux2 = aux2.siguiente
                    aux = aux.abajo
            temporal = temporal.siguiente
        return concatenadora

    def eliminar(self, cad):
        pedasos = cad.split("@")
        dir = pedasos[0]
        do = "@" + pedasos[1]
        caracterUno = dir[0]
        if self.verticales.existeV(caracterUno) == False:
            return " "

        if self.horizontales.existeH(do) == False:
            return " "

        if self.horizontales.existeNodoMatriz(do, caracterUno) == False:
            return " "
        if self.horizontales.eliminarEnNodo(dir, do) == True:
            # print "pasa eliminacion desde nodoMatriz"
            temporal = self.horizontales.primero
            while temporal != None:
                if temporal.domini == do:
                    #       print "entra eliminacion de la lista asociada a nodo horizontal"
                    temporal.lista.eliminar(caracterUno)
                    #      print"pasa eliminacion de la lista asociada a nodo horizontal"
                    break
                temporal = temporal.siguiente
            if self.horizontales.noTieneNada(do) == True:
                # print "entra a la eliminacion de nodo horizontal"
                self.horizontales.eliminar(do)
                # print"pasa eliminacion de nodo horizontal"
            temporal2 = self.verticales.primero
            while temporal2 != None:
                if temporal2.primerLetra == caracterUno:
                    #   print "entra eliminacion de la lista asociada a nodo vertical"
                    temporal2.lista.eliminar(do)
                    #  print "pasa eliminacion de la lista asociada a nodo vertical"
                    break
                temporal2 = temporal2.siguiente
            if self.verticales.noTieneNada(caracterUno) == True:
                # print "entra eliminacion de nodo vertical"
                self.verticales.eliminar(caracterUno)
                # print "pasa eliminacion de nodo vertical"
matri = matriz()
stack = pila()
fifo = cola()
lista = listaSimple()

@app.route('/metodoPrueba', methods= ['POST'])
def hello_world():
    parametro = str(request.form['parametro'])
    return 'Hello World!'+str(parametro)+"Jose"

@app.route('/insertarLista', methods= ['POST'])
def insertaLista():
    parametro = str(request.form['parametro'])
    lista.agregar(parametro)
    lista.reporteLista()
    return "ya inserto"+ parametro


@app.route('/eliminarLista', methods= ['POST'])
def eliminarLista():
    parametro = str(request.form['parametro'])
    lista.eliminarPorIndice(int(parametro))
    lista.reporteLista()
    return "eliminando..."
@app.route('/buscarLista', methods= ['POST'])
def buscaLista():
    parametro = str(request.form['parametro'])
    return lista.buscar(parametro)

@app.route('/queue', methods= ['POST'])
def insertarCola():
    parametro = str(request.form['parametro'])
    fifo.agregar(int(parametro))
    fifo.reporteCola()
    return "ya lo inserto"
@app.route('/dequeue', methods= ['POST'])
def eliminarCola():
    parametro = str(request.form['parametro'])
    temporal = fifo.eliminar()
    fifo.reporteCola()
    return temporal

@app.route('/push', methods= ['POST'])
def insertarPila():
    parametro = str(request.form['parametro'])
    stack.insertar(int(parametro))
    stack.reportePila()
    return "ya lo inserto"
@app.route('/pop', methods= ['POST'])
def eliminaPila():
    parametro = str(request.form['parametro'])
    temporal = stack.pop()
    stack.reportePila()
    return temporal

@app.route('/insertarMatriz', methods= ['POST'])
def insertarMatriz():
    parametro = str(request.form['parametro'])
    matri.insertar(parametro)
    matri.graficarMatriz()
    return "Insertado"
@app.route('/buscarPorLetra', methods= ['POST'])
def buscarPorLetra():
    parametro = str(request.form['parametro'])
    return matri.buscarPorLetra(parametro)
@app.route('/buscarPorDominio', methods= ['POST'])
def buscarPorDominio():
    parametro = str(request.form['parametro'])
    return matri.buscarPorDominio(parametro)
@app.route('/eliminarMatriz', methods= ['POST'])
def eliminarMatriz():
    parametro = str(request.form['parametro'])
    matri.eliminar(parametro)
    matri.graficarMatriz()
    return "elimino"

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
