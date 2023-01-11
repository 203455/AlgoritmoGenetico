import math
import numpy as np

class ADN: 
    def __init__(self, pob_ini,pob_max, prob_cruza, prob_muta_indi, prob_muta_gen , intervalo, val_min, val_max, precision, n_generaciones, tipo_valor):
        self.pob_ini = pob_ini
        self.pob_max = pob_max
        self.prob_cruza = prob_cruza
        self.prob_muta = prob_muta_indi
        self.prob_muta = prob_muta_gen
        self.intervalo = intervalo
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

    def evaluoPoblacion(self, valor_min, valor_max, precision):
        x = 0.0
        a = valor_min
        valor = self.calcularValor(valor_min, valor_max, precision)
        valor_bits = self.calculoBits
        delta = (valor_max - valor_min) / valor_bits
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
    
    

def obtencionDatos():
    adn = ADN()
    pass
    

if __name__ == "__main__":
    obtencionDatos()
    
    pass  
    