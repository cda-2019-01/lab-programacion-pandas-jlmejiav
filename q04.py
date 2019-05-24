##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
##
pd.set_option('display.notebook_repr_html', False)
df = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl1.tsv'), delimiter='\t')
##
letrasmin=sorted(set(df._c4))
letrasmay=[]
for w in letrasmin:
    letrasmay.append(w.upper())
print(letrasmay)