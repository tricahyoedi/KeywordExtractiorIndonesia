# -*- coding: utf-8 -*-
"""
Chunker pola dengan 2 atau 3 kata dalam frase
"""

def chunk(text,pattern,n_pattern):
    candidate = []
    pattern = pattern.split()
    n = len(pattern)
    for sub in text:
        end = len(sub) + 1 - n
        for ind, (a,b) in enumerate(sub):
            if(len(sub)<n): #berhenti kalau panjang kalimat < panjang pola
                break
            if ind == end:
                break
            x = True
            for num, i in enumerate(pattern):
                if i != sub[ind+num][1]:
                    x = False
            if x:
                s = ""
                for i in range(n):
                    s = s + sub[ind+i][0]
                    if i != len(pattern)-1:
                        s = s + " "
                candidate.append(s)
    candidate = [(candidate.count(i),n_pattern,i) for i in set(candidate)]
    return candidate

#from operator import itemgetter
import os
folder = "D:\Documents\Skripsi\Koding\Data\\testing\\"
os.chdir(folder)
n = len([name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))])

#baca pola
fo = open('D:\Documents\Skripsi\Koding\Data\\bobot.csv')
pola = fo.read()
fo.close()

pola = pola.split('\n')[1:]
pola = [i.split(',') for i in pola]
pola = [[i[0], int(i[1]), int(i[2])] for i in pola]

for i in range(n):
    fol_num = str(i+1)
    os.chdir(fol_num)
    fo = open("tagged_badanteks.txt","r+")
    badanteks = fo.read()
    fo.close()
    
    badanteks = badanteks.replace('\n','')
    badanteks = badanteks.split(' ./. ')[:-1] #sentence tokenize
    for i in badanteks:
        ind = badanteks.index(i)
        badanteks[ind]= i.split() #word tokenize
        for j in badanteks[ind]:
            ine = badanteks[ind].index(j)
            if badanteks[ind][ine] == '//GM':
                badanteks[ind][ine] = ('/','GM')
            else:
                temp = tuple(j.split('/'))
                badanteks[ind][ine] = tuple((temp[0].lower(),temp[1]))
            
    kandidat = []
    for i in pola:
        if 4>int(i[2])>1:
            kandidat = kandidat + chunk(badanteks,i[0],i[1])
    
    fo = open('generated_kandidat23_badan.txt','w+')
    fo.write('\n'.join([str(i[0]) +","+ str(i[1]) +","+ str(i[2]) for i in kandidat]))
    fo.close()
    
    os.chdir('..')
#    print fol_num