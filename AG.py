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

def calculoValor(val_min, val_max, precision):
    valor = ((val_max-val_min)/precision)+1
    return valor

def poda(poblacion, poblacion_maxima):
    if len(poblacion) > poblacion_maxima:
            while len(poblacion) > poblacion_maxima:
                poblacion.remove(poblacion[-1])  
    return poblacion

def insercion():
    poda()
    pass

def calculoAptitudNuevo():
    insercion()
    pass


def mutacion(prob_muta_indi, prob_muta_gen, hijos):
    prob_muta_indi = prob_muta_indi
    prob_muta_gen = prob_muta_gen
    pm = prob_muta_indi * prob_muta_gen
    poblacion_final = []
    individuos = []
    for i in range(hijos):
        numero_aleatorio = [np.random.rand() for i in range(calculoBits(calculoValor(valor_min,valor_max,presicion)))]
        individuo = (hijos[i], numero_aleatorio)
        individuos.append(individuo)


    for i in range(hijos.__len__()):
        for j in range(individuos[i].__getitem__(1).__len__()):
            if individuos[i].__getitem__(1)[j] < pm:
                individuo = list(individuos[i].__getitem__(0))
                
                print("individuo: ", individuo)
                if individuo[j] == "0":
                    individuo[j] = "1"
                    individuoMutado = "".join(individuo)
                    individuos[i] = (individuoMutado, individuos[i].__getitem__(1))
                    
                    

                else:
                    individuo[j] = "0"
                    individuoMutado = "".join(individuo)
                    individuos[i] = (individuoMutado, individuos[i].__getitem__(1))
                    

    for i in range(individuos.__len__()):            
        poblacion_final.append(individuos[i].__getitem__(0))
    
    return poblacion_final
    calculoAptitudNuevo()
    pass


def cruza(padres,p_cruza):
    hijo1_head = ""
    hijo1_tail = ""
    hijo2_head = ""
    hijo2_tail = ""
    hijo1 = ""
    hijo2 = ""
    hijos = []    
    padre_ganador = padres._getitem(0).getitem_(0)
    pc = np.random.rand()
    if pc <= p_cruza:
        for i in range(int(len(padres)/2)):
                punto_cruza = np.random.randint(1,padres._getitem(0).getitem(0).len_())
                hijo1_head = padre_ganador[:punto_cruza]
                hijo1_tail = padres[i+1]._getitem_(0)[punto_cruza:]
                hijo2_head = padres[i+1]._getitem_(0)[:punto_cruza]
                hijo2_tail = padre_ganador[punto_cruza:]
                hijo1 = hijo1_head +""+ hijo1_tail
                hijo2 = hijo2_head +""+ hijo2_tail
                hijos.append(hijo1)
                hijos.append(hijo2)
        else:
            pass
    mutacion(hijos)
    return hijos
    pass


def funcion(x):
    valor = ((x*x)*(math.sin(x)))-((2*(x*x))*(math.cos(x)))
    return valor


def calculoAptitud():
    cruza()
    pass

def obtencionDatos():
    calculoAptitud()
    pass
    

if __name__ == "__main__":
    obtencionDatos()
    
    pass  
    