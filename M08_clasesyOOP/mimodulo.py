# mimodulo.py

class OperacionesParaLista:
    def __init__(self, lista):
        self.lista = lista

    def lista_primo(self):

        lista_resultados = []

        for i in self.lista:
            flag = True
            if i <= 2:
                flag = False
            else:
                for s in range(2, i):
                    if i % s == 0:
                        flag = False
                        break
            lista_resultados.append(flag)

        return lista_resultados

    def lista_modal(self):

        val = []
        rep = []

        for x, v in enumerate(self.lista):
            if self.lista[x] == self.lista[x-1]:
                rep.append(v)
                rep.append(self.lista[x-1])
                val.remove(self.lista[x-1])
            else:
                val.append(v)

        return val, rep

    def lista_temperatura(self, temp_one, temp_two):

        temp_res = []

        if temp_one == "C" and temp_two == "F":
            for i in self.lista:
                temp_res.append(((i*9)/5) + 32)
        elif temp_one == "C" and temp_two == "K":
            for i in self.lista:
                temp_res.append(i + 273.15)
        elif temp_one == "K" and temp_two == "F":
            for i in self.lista:
                temp_res.append(((i - 32)*5)/9 + 273.15)
        elif temp_one == "F" and temp_two == "K":
            for i in self.lista:
                temp_res.append(((i - 273.15)*9)/5 + 32)
        else:
            return "Ingrese un codigo valido"

        return temp_res

    def calc_factorial(self, numero):

        if type(numero) != int:
            return 'El número debe ser un entero'
        elif numero < 0:
            return 'El número debe ser positivo'
        elif numero <= 1:
            return 1
        numero = numero * self.calc_factorial(numero - 1)

        return numero

    def lista_factorial(self):

        lista_factoriales = []

        for i in self.lista:
            lista_factoriales.append(self.calc_factorial(i))

        return lista_factoriales
