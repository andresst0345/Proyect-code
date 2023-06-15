import scipy 
import matplotlib as mp
import numpy as np

path = "C:/Poyecto PG1/hVd Database-F/bill"
folders = ["folder1", "folder2", "folder3", "folder4", "folder5", "folder6", "folder7", "folder8", "folder9", "folder10", "folder11", "folder12", "folder13", "folder14" "folder16"]
files = ["hAd.0","haid.0", "haud.0", "hEd.0"]
results = {}

def import_audio(path: str, file_name: str) -> np.array:
    with open(path + '/' + file_name, 'rb') as fid:
        data_array = np.fromfile(fid, np.int16)
        data_array = data_array / max(data_array)
    return data_array

def energia(v: list) -> float:
    ope = []
    for i in range(len(v)):
        c = v[i] **2
        ope.append(c)
    se = sum(ope)
    eng = se / len(v)
    return eng

def zero_cross(vec) -> float:
    opz = []
    for ii in range(len(vec)):
        b = np.sign(vec[ii]) 
        a = np.sign(vec[ii]-1)
        d = b - a
        opz.append(d)
    szc = sum(opz)
    zcr = szc / 2*len(vec)
    return zcr

def entropia(vc: list) -> float:
    opent = []
    for iii in range(len(vc)):
        y = ((vc[iii]) / energia(vc))**2
        z = np.log(y)
        w = y * z
        opent.append(w)
        sent = sum(opent)
        H = sent / len(vc)
    return H

# test
for folder in folders:
    folder_results = {}
    for file_name in files:
        k = import_audio(path+'/'+folder, file_name)
        folder_results[file_name] = [energia(k), zero_cross(k), entropia(k)]
    results[folder] = folder_results

print(results)