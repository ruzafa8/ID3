import math
def log(x):
    if x == 0:
        return 1.0
    else:
         return math.log(x,2)

def entropia(x):
    res = 0
    d = dict.fromkeys(x,0) # Frecuencias de valores de atributos
    totalValues = len(x)
    for i in x:
        d[i] = d[i] + 1
    
    for key,value in d.items():
        prob = value/totalValues
        res = res - (prob * log(prob))
    return res

def ocurrencias(l, item):
    indices = []
    for i in range(len(l)):
        if l[i] == item:
            indices.append(i)
    return indices

def entropiaRelativaPosAttribute(values, s, listOcurrencias):
    d = dict.fromkeys(s,0) # Frecuencias de ese atributo en cada valor del atributo target
    times = len(listOcurrencias)

    for ocurrencia in listOcurrencias:
        salida = s[ocurrencia]
        d[salida] = d[salida] + 1

    res = 0
    for key,value in d.items():
        prob = value/times
        res = res - (prob * log(prob))
    return res

def entropiaRelativa(values, s):

    resultado = 0
    nValues = len(values)

    for value in dict.fromkeys(values):
        print("Para el valor",value)
        listOcurrencias = ocurrencias(values,value)
        res = entropiaRelativaPosAttribute(values,s,listOcurrencias)
        resultado = resultado - res * (len(listOcurrencias)/nValues)
    return entropia(s) + resultado
