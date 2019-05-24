##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
import numpy as np
##
pd.set_option('display.notebook_repr_html', False)
df = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl0.tsv'), delimiter='\t')
##
##
dfsort = df.sort_values(by=['_c2']).reset_index()
letras=sorted(set(dfsort._c1))
##
tabla=pd.DataFrame('',columns=['_c0','lista'],index=list(range(len(letras))))
z=0
for w in letras:
    tabla._c0[z]=w
    for i in list(range(len(df._c1))):
        if dfsort._c1[i] == w:
            tabla.lista[z] = tabla.lista[z] + str(dfsort._c2[i])+':'
    tabla.lista[z]=tabla.lista[z][:-1]
    z = z+1
print(tabla)