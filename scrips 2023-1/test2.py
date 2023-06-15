import numpy as np
import matplotlib.pyplot as plt

files = ["hid.0", "hId.0", "hEd.0", "hAd.0", "had.0", "hYd.0", "hOd.0", "hod.0", "hUd.0", "hud.0", "hed.0", "heid.0", "haid.0", "haud.0", "hoid.0", "houd.0", "hied.0", "heed.0"]

folders = ["andrew", "andy", "bill", "david", "geoff", "jo", "kate", "mike", "nick", "penny", "rich", "rose", "sarah", "sue", "tim", "wendy"]

path = "C:/Poyecto PG1/hVd Database-F/"

def import_audio(path, file_name):
    with open(path + '/' + file_name, 'rb') as fid:
        data_array = np.fromfile(fid, np.int16)
        data_array = data_array / max(data_array)
    return data_array

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

    # Aplicar las operaciones vectorizadas solo a los valores positivos de y
    mask = (y > 0)  # Máscara booleana para valores positivos de y
    y_pos = y[mask]  # Valores positivos de y
    z = np.zeros_like(y)  # Arreglo de ceros del mismo tamaño que y
    z[mask] = np.log(y_pos)  # Calcular el logaritmo solo para los valores positivos de y
    w = y * z

    sent = np.sum(w)  
    H = sent / len(vc)
    return H

def calcular_resultados(files, folders, path):
    energia_list = []
    zero_cross_list = []
    entropia_list = []
    for folder in folders:
        energia_folder = []
        zero_cross_folder = []
        entropia_folder = []
        for file in files:
            archivo = folder + '/' + file
            vec = import_audio(path, archivo)

            rt_zero_cross = zero_cross(vec)
            rt_entropia = entropia(vec)
            rt_energia = energia(vec)

            energia_folder.append(rt_energia)
            zero_cross_folder.append(rt_zero_cross)
            entropia_folder.append(rt_entropia)

        energia_list.append(energia_folder)
        zero_cross_list.append(zero_cross_folder)
        entropia_list.append(entropia_folder)

    return energia_list, zero_cross_list, entropia_list

energia_list, zero_cross_list, entropia_list = calcular_resultados(files, folders, path)

# Graficar los resultados de la energía
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i, energia_folder in enumerate(energia_list):
    for j, energia_file in enumerate(energia_folder):
        ax.scatter(i, j, energia_file, c='r', marker='o')
ax.set_xlabel('Carpeta')
ax.set_ylabel('Archivo')
ax.set_zlabel('Energía')
plt.show()

# Graficar los resultados del zero-crossing rate
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i, zero_cross_folder in enumerate(zero_cross_list):
    for j, zero_cross_file in enumerate(zero_cross_folder):
        ax.scatter(i, j, zero_cross_file, c='g', marker='o')
ax.set_xlabel('Carpeta')
ax.set_ylabel('Archivo')
ax.set_zlabel('Zero-crossing rate')
plt.show()

# Graficar los resultados de la entropía
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i, entropia_folder in enumerate(entropia_list):
    for j, entropia_file in enumerate(entropia_folder):
        ax.scatter(i, j, entropia_file, c='b', marker='o')
ax.set_xlabel('Carpeta')
ax.set_ylabel('Archivo')
ax.set_zlabel('Entropía')
plt.show()