
import pandas as pd
from random import randrange, choice

#Vamos a empezar creando la tabla de pacientes
#Leemos todos los datos
df = pd.read_csv('../datasets/personas-extravidas-y-desaparecidas-datacivica-2018.csv')

#Comprobamos la cabecera de los datos
print(list(df))

df1 = pd.DataFrame()
df1['prim_nombre'] = df.prim_nombre
df1['seg_nombre'] = df.seg_nombre
df1['apellido_pat'] = df.apellido_pat
df1['apellido_mat'] = df.apellido_mat
df1['sexo_paceinte'] = df.fuerocomun_sexo
df1['altura_paciente'] = df.fuerocomun_estatura
df1['etnia_paceinte'] = df.fuerocomun_etnia
df1['edad_paciente'] = df.fuerocomun_edad
df1['complexion_paciente'] = df.fuerocomun_complexion
df1['fecha_ingreso'] = df.fuerocomun_desapfecha
df1['hora_ingreso'] = df.fuerocomun_desaphora
df1['nacionalidad_paceinte'] = df.fuerocomun_nacionalidad
df1['Descripcion'] = df.fuerocomun_descripcion
vector = []
urgencia = []
id_expediente = []
#Asegurar valores distintos
for i in range(0, len(df1.prim_nombre)):
    vector.insert(i,choice(["YES", "NO"]))
    id_expediente.insert(i, randrange(1111111, 9999999))
    num_urgencia = randrange(1111111, 9999999)
    urgencia.insert(i, choice(["NULL", num_urgencia]))

print(len(df.apellido_mat))
print(len(vector))
print(len(urgencia))
print(len(id_expediente))
df1['smoker'] = vector
df1['urgencia'] = urgencia
df1['num_expediente'] = id_expediente

print(list(df1))

df1.to_csv('../datasets/Tabla_Paciente.csv', sep='\t', encoding='utf-8')
print(list(df1))
#Join the values
#df = points.append(centroid)
#points_x = np.array(points.x, dtype=pd.Series)
#centroid_x = np.array(centroid.x, dtype=pd.Series)
#x_values = np.concatenate(points_x , centroid_x)



#Join both traces
#data = [points]

# Plot and embed in python offline!
#py.offline.plot(data, filename='basic-scatter.html')

# or plot with:
#plot_url = py.plot(data, filename='basic-line')