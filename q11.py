##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
import numpy as np
##
pd.set_option('display.notebook_repr_html', False)
df = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl2.tsv'), delimiter='\t')
##
##
dfsort = df.sort_values(by=['_c5a']).reset_index()
letras=sorted(set(dfsort._c0))
##
tabla=pd.DataFrame('',columns=['_c0','lista'],index=list(range(len(letras))))
z=0
for w in letras:
    tabla._c0[z]=w
    for i in list(range(len(df._c0))):
        if dfsort._c0[i] == w:
            tabla.lista[z] = tabla.lista[z] + str(dfsort._c5a[i]) + ':' + str(dfsort._c5b[i]) + ','
    tabla.lista[z]=tabla.lista[z][:-1]
    z = z+1
print(tabla)