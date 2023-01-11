import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import random
from shutil import rmtree
from PyQt5 import QtWidgets, uic


class ADN: 
    def __init__(self, pob_ini,pob_max, prob_cruza, prob_muta_indi, prob_muta_gen , val_min, val_max, precision, n_generaciones, tipo_valor):
        self.pob_ini = pob_ini
        self.pob_max = pob_max
        self.prob_cruza = prob_cruza
        self.prob_muta = prob_muta_indi
        self.prob_muta = prob_muta_gen
        self.val_min = val_min
        self.val_max = val_max
        self.precision = precision
        self.n_generaciones = n_generaciones
        self.tipo_valor = tipo_valor
        pass
    
    def get_pob_ini(self, pob_ini):
        self.pob_ini = pob_ini
        pass
    
    def calculoBits(valor):
        valor_bits = math.ceil(math.log(valor,2))
        return valor_bits

    
    def generarPoblacion(self):
        poblacion = []
        valor = self.calcularValor(self.val_min, self.val_max, self.precision)
        for i in range(self.pob_ini):
            gen = [np.random.randint(0, 2) for i in range(self.calculoBits(valor))]
            poblacion.append(gen)
        return poblacion
    

    def calcularValor(self,val_min, val_max, precision):
        valor = ((val_max-val_min)/precision)+1
        return valor
    
    
    def conversionDecimal(self, item):
        valor_decimal = 0 #inicializado en 0
        cadena = ""
        for i in range(len(item)):
            cadena += str(item[i])    
        for posicion, digito_string in enumerate(cadena[::-1]):
            valor_decimal += int(digito_string) * 2 ** posicion
        return(valor_decimal, cadena)

    def evaluoPoblacion(self, poblacion):
        x = 0.0
        valor = self.calcularValor(self.val_min, self.val_max, self.precision)
        valor_bits = self.calculoBits
        delta = (self.val_max - self.val_min) / valor_bits
        valor = 0
        poblacion = poblacion
        fitness = []	
        for i in range(len(poblacion)):
            i = self.conversionDecimal(poblacion.__getitem__(i))
            x = a + (i[0] * delta) 
            print(x)
            valor = (i.__getitem__(1),x,self.funcion(x),i.__getitem__(0))
            fitness.append(valor)
        return fitness

    def poda(poblacion, poblacion_maxima):
        if len(poblacion) > poblacion_maxima:
                while len(poblacion) > poblacion_maxima:
                    poblacion.remove(poblacion[-1])  
        return poblacion

    def insercion(poblacion, hijos):
        poblacion.extend(hijos)
        return poblacion

    def calculoAptitudNuevo(self, genes_mut, poblacion):
        poblacion = poblacion.copy()
        x = 0.0
        valor = self.calcularValor(self.val_min, self.val_max, self.presicion)
        delta = (self.val_max - self.val_min) / self.calculoBits(valor)
        decimal = 0
        poblacion_nue = []
        gen_comp = []
        for i in range(len(genes_mut)):
            for posicion, digito_string in enumerate(genes_mut[i][::-1]):
                decimal += int(digito_string) * 2 ** posicion
            x = self.val_min + decimal * delta    
            gen_comp = (genes_mut[i], x, self.funcion(x), decimal)
            poblacion_nue.append(gen_comp)
            decimal = 0 
        
        poblacion_final = self.insercion(poblacion_nue, poblacion)
        j=0
        for i in range(len(poblacion_final)):
            if (poblacion_final[j].__getitem__(1) > self.val_max or poblacion_final[j].__getitem__(1) < self.val_min):
                poblacion_final.remove(poblacion_final[j])
                j = j - 1
            j=j+1
        return poblacion_final


    def mutacion(self, prob_muta_indi, prob_muta_gen, hijos):
        prob_muta_indi = prob_muta_indi
        prob_muta_gen = prob_muta_gen
        probabilidad = prob_muta_indi * prob_muta_gen
        poblacion_final = []
        genes = []
        valor = self.calcularValor(self.val_min,self.val_max,self.precision)
        for i in range(hijos):
            numero_aleatorio = [np.random.rand() for i in range(self.calculoBits(valor))]
            gen = (hijos[i], numero_aleatorio)
            genes.append(gen)
            
        for i in range(hijos):
            for j in range(len(genes[i].__getitem__(1))):
                if genes[i].__getitem__(1)[j] < probabilidad:
                    gen = list(genes[i].__getitem__(0))
                    if gen[j] == "0":
                        gen[j] = "1"
                        genMutado = "".join(gen)
                        genes[i] = (genMutado, genes[i].__getitem__(1))
                    else:
                        gen[j] = "0"
                        genMutado = "".join(gen)
                        genes[i] = (genMutado, genes[i].__getitem__(1))
        for i in range(genes.__len__()):            
            poblacion_final.append(genes[i].__getitem__(0))
        return poblacion_final


    def cruza(padres,prob_cruza):
        hijos = []    
        padre = padres._getitem(0).getitem_(0)
        punto_cruza =int(padre._len_()/2)
        probabilidad = np.random.rand()
        if probabilidad <= prob_cruza:
            for i in range(int(len(padres)-2)):
                    prim_hijo_cabeza = padre[:punto_cruza]
                    prim_hijo_cola = padres[i+1]._getitem_(0)[punto_cruza:]
                    seg_hijo_cabeza = padres[i+1]._getitem_(0)[:punto_cruza]
                    seg_hijo_cola = padre[punto_cruza:]
                    prim_hijo = prim_hijo_cabeza +""+ prim_hijo_cola
                    seg_hijo = seg_hijo_cabeza +""+ seg_hijo_cola
                    hijos.append(prim_hijo)
                    hijos.append(seg_hijo)
            else:
                pass
        return hijos


    def funcion(x):
        valor = ((x*x)*(math.sin(x)))-((2*(x*x))*(math.cos(x)))
        return valor
    
    
    def ordenarValores(self, valores, tipo_valor):
        valores_ordenados = []
        valores_ordenar = []
        
        for i in range(len(valores)):
            valores_ordenar.append(valores.__getitem__(i).__getitem__(2))
            
        if tipo_valor:
            valores_ordenados = sorted(valores_ordenar, key = lambda x:float(x), reverse=True)
        else:
            valores_ordenados = sorted(valores_ordenar, key = lambda x:float(x)) 
        return valores_ordenados


    def calculoAptitud(self, tipo_valor, valor):
        fitness = valor.copy()
        genes_padre = []
        fitness.sort(key=lambda x: x[2], reverse=tipo_valor)
        for i in range(int(len(fitness)/2)):
            fitness.pop()
        for i in range(int(len(fitness))):
            genes_padre.append(fitness[np.random.randint(0, len(fitness))])
        if len(genes_padre) % 2 != 0:
            genes_padre.pop()
        genes_padre.sort(key=lambda x: x[2], reverse=tipo_valor)      
        return genes_padre


def main(adn, interfaz):
    poblacion = []
    generaciones = []
    genes_sin_poda = []
    mejor_gen = []
    peor_gen = []
    promedio = []
    
    poblacion_generado = adn.generarPoblacion()
    
    poblacion = adn.evaluoPoblacion(poblacion_generado) 
     
    print("Poblacion inicial: (Generacion 1)",poblacion)
    
    for generacion in range(adn.n_generaciones):
        fitness = adn.calculoAptitud(adn.tipo_valor,poblacion)
        cruza = adn.cruza(fitness, adn.prob_cruza)
        mutacion = adn.mutacion(adn.prob_muta_indi, adn.prob_muta_gen, cruza)
        genes_sin_poda = adn.calculoAptitudNuevo(mutacion,poblacion)
        
        poblacion_ordenada = adn.ordenarValores(genes_sin_poda, adn.tipo_valor)
        
        mejor_gen.append(poblacion_ordenada[0])
        promedio.append(np.mean(poblacion_ordenada))
        peor_gen.append(poblacion_ordenada[-1])
        
        genes_sin_poda.sort(key=lambda x: float(x.__getitem__(2)), reverse=adn.tipo_valor)
        poblacion = adn.poda(genes_sin_poda, adn.pob_max)
        generaciones.append(poblacion)
        
    interfaz.estado2.setText("Mejor Gen: " + str(mejor_gen[-1]))
    for i in range(len(generaciones)):
        print("Generacion: ",i+1," ",generaciones[i])
    
    plt.plot(mejor_gen, label="Mejor individuo", color="red", linestyle="-",)
    plt.plot(promedio, label="Promedio", color="blue", linestyle="-",)
    plt.plot(peor_gen, label="Peor individuo", color="green", linestyle="-")
    plt.legend()
    os.makedirs("ag\Graficas/", exist_ok=True)
    plt.savefig("ag\Graficas/Grafica.png")
    plt.close()
    
    try:
        rmtree("ag\Graficas\individual/")
    except:
        pass
    finally:
        os.makedirs("ag\Graficas\individual", exist_ok=True)
    for i in range(len(generaciones)):
        listaX = []
        listaY = []
        for j in range(len(generaciones[i])):
            listaX.append(generaciones[i].__getitem__(j).__getitem__(1))
            listaY.append(generaciones[i].__getitem__(j).__getitem__(2))

        plt.title("Generacion: " + str(i+1))
        plt.scatter(listaX, listaY)
        plt.xlim(0,adn.val_max+1)
        plt.ylim(-1, 5)
        plt.savefig("ag\Graficas\individual/generado"+str(i+1)+".png")
        plt.close()
    print("OK")
    pass
    
def send():
    
    run = True
    try:
        pob_ini = int(interfaz.poblacion_i.text())
        pob_max = int(interfaz.poblacion_m.text())
        precision = float(interfaz.presicion.text())
        prob_muta_gen = float(interfaz.pmg.text())
        prob_muta_indi = float(interfaz.pmi.text())
        prob_cruza = float(interfaz.pcruza.text())
        val_max = int(interfaz.xmax.text())
        val_min = int(interfaz.xmin.text())
        tipo_valor = bool(interfaz.maximizar.isChecked())
        n_generaciones = int(interfaz.generaciones.text())
    
    
        if(pob_ini < 1 or pob_max < 1 or precision <= 0 or prob_muta_gen <= 0 or prob_muta_indi <= 0 or prob_cruza <= 0 or n_generaciones <= 1):
            interfaz.estado.setText("Error al ingresar los datos")
            interfaz.estado.setStyleSheet("color: red")
            run = False

        if(val_min > val_max):
            interfaz.estado.setText("Error, el valor mínimo no puede ser mayor que el valor máximo")
            interfaz.estado.setStyleSheet("color: red")
            run = False

        if( prob_cruza >= 1):
            interfaz.estado.setText("Error La probabilidad debe ser menor a 1")
            interfaz.estado.setStyleSheet("color: red")
            run = False
    
    except:
        interfaz.estado.setText("Error al ingresar los datos")
        interfaz.estado.setStyleSheet("color: red")
        run = False
           
    if(run):
        interfaz.estado.setText("")
        adn = ADN(pob_ini = pob_ini, pob_max = pob_max , prob_cruza = prob_cruza , prob_muta_indi = prob_muta_indi , prob_muta_gen = prob_muta_gen , val_min=val_min, val_max = val_max, precision = precision, n_generaciones = n_generaciones, tipo_valor = tipo_valor)
        main(adn,interfaz)

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    interfaz = uic.loadUi("interfaz.ui")
    interfaz.show()
    interfaz.btn_ok.clicked.connect(send)
    
    sys.exit(app.exec())  
    