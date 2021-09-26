# Óra jegyzet

## Gépi tanulás alapjai - Hitelbírálati feladat megoldása osztályozó algoritmussal

Érintett témák: Hitelbírálati feladat, Osztályozás, Döntési fák bemutatása, K legközelebbi szomszéd módszere, Profit görbe, Kiértékelés

## Importok
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

## Adatok betöltése
df = pd.read_csv("FILENEAME.csv") ## adatok betöltése

# Data understanding


## Megoszlás ábrázolása
a = plt.hist(df[OSZLOPNEV], bins=50) 


## DataFlow megbontása feltétel szerint
egyik = df[df['OSZLOPNEV'] == "ERTEK_1"]
masik = df[df['OSZLOPNEV'] == "ERTEK_2"]

### Példa
Mult = df[df['past_or_future'] == "past"]
jovo = df[df['past_or_future'] == "future"]


### Ábrázolás példa
a = plt.hist(mult['PERSONAL_NET_INCOME'], bins =100)
b = plt.hist(jovo['PERSONAL_NET_INCOME'], bins =100, alpha= 0.50)


## Értékek megszámolása
df['OSZLOPNEV'].value_counts()

### Példa
mult['TARGET_NOT_DEFAULT'].value_counts()
*
1.0    17901
0.0     4249
Name: TARGET_NOT_DEFAULT, dtype: int64

#### Kitöletetlen értékek esetén
jovo['TARGET_NOT_DEFAULT'].value_counts()
*
Series([], Name: TARGET_NOT_DEFAULT, dtype: int64)


## Új oszlop létrehozása fügvénnyel - oszlop alapján

def fuggvenynev(x):
    if x == "F":
        return 1
    else:
        return 0
-
df['UjOSZLOPNEV'] = df['OSZLOPNEV'].apply(fuggvenynev)


## Új oszlop létrehozása fügvénnyel - sor alapján

def fuggvenynev1(x):
    if x['Age']>67:
        return x['PERSONAL_NET_INCOME']
    else:
        return 0
-
df['UjOSZLOPNEV'] = df.apply(fuggvenynev1, axis=1)

