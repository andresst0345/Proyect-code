#%%
import numpy as np
import matplotlib.pyplot as plt

# Definir los archivos y carpetas a analizar
files = ["hid.0", "hId.0", "hEd.0", "hAd.0", "had.0", "hYd.0", "hOd.0", "hod.0", "hUd.0", "hud.0", "hed.0", "heid.0", "haid.0", "haud.0", "hoid.0", "houd.0", "hied.0", "heed.0"]

folders = ["andrew", "andy", "bill", "david", "geoff", "jo", "kate", "mike", "nick", "penny", "rich", "rose", "sarah", "sue", "tim", "wendy"]

path = "C:/Poyecto PG1/hVd Database-F/"

# Funciones de análisis de audio
def importaudio(path, filename):
    with open(path + '/' + filename, 'rb') as fid:
        dataarray = np.fromfile(fid, np.int16)
        dataarray = dataarray / max(dataarray)
    return dataarray

def energia(v):
    ope = []
    for i in range(len(v)):
        c = v[i] ** 2
        ope.append(c)
    se = sum(ope)
    eng = se / len(v)
    return eng

def zero_cross(vec):
    opz = []
    for ii in range(len(vec)):
        b = np.sign(vec[ii]) 
        a = np.sign(vec[ii] - 1)
        d = b - a
        opz.append(d)
    szc = sum(opz)
    zcr = szc / (2 * len(vec))
    return zcr

def entropia(vc):
    opent = []
    vc = np.array(vc)  # Convertir la lista a un arreglo de NumPy para facilitar las operaciones vectorizadas
    eng = energia(vc)
    y = (vc / eng) ** 2
    mask = (y > 0)  # Máscara booleana para valores positivos de y
    ypos = y[mask]  # Valores positivos de y
    z = np.zeros_like(y)  # Arreglo de ceros del mismo tamaño que y
    z[mask] = np.log(ypos)  
    w = y * z
    sent = np.sum(w)
    H = sent / len(vc)
    return H

# Función para calcular los resultados de energía, zero crossings y entropía para cada archivo
def calcularresultados(files, folders, path):
    resultados = []
    for folder in folders:
        folderrt = []
        for file in files:
            archivo = folder + '/' + file
            vec = importaudio(path, archivo)
            rtenergia = energia(vec)
            rtzerocross = zero_cross(vec)
            rtentropia = entropia(vec)
            folderrt.append((rtenergia, rtzerocross, rtentropia))
        resultados.append(folderrt)
    return resultados

# Calcular los resultados para cada archivo
resultados = calcularresultados(files, folders, path)

# Agrupar los resultados por archivo
energia_por_archivo = [[] for i in range(len(files))]
zero_cross_por_archivo = [[] for i in range(len(files))]
entropia_por_archivo = [[] for i in range(len(files))]

for i, file in enumerate(files):
    
    energia_por_archivo[i].append(resultados[1][i][0])
    zero_cross_por_archivo[i].append(resultados[1][i][1])
    entropia_por_archivo[i].append(resultados[1][i][2])

# Definir una lista de colores para cada género
colors = {'Mujeres': 'red', 'Hombres': 'blue'}

for ii in (files):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') 
    ax.scatter(energia_por_archivo[0][ii], zero_cross_por_archivo[1][ii], entropia_por_archivo[1][ii])
    #ax.text(energia_por_archivo[ii], zero_cross_por_archivo[1][ii], entropia_por_archivo[1][ii], fontsize=8)
    
    

ax.set_xlabel('Energía')
ax.set_ylabel('Zero Crossings')
ax.set_zlabel('Entropía')
ax.set_title(file[1])
ax.legend()
plt.show()