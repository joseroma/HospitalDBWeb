
import pandas as pd
from random import randrange, choice


print("Leemos los datasets")

#BOTELLA NAIRA


#Leemos todos los datos
df = pd.read_csv('../datasets/personas-extravidas-y-desaparecidas-datacivica-2018.csv')
df_paises = pd.read_csv('../datasets/paises.txt')
especialidades = pd.read_csv('../datasets/especialidades.txt')
enfermedades = pd.read_csv('../datasets/enfermedades.txt')
doctor_names = pd.read_csv('../datasets/wc2018-players.csv')

print("Generamos los dataframes vacíos")

#Creamos las diferentes tablas
tabla_paciente = pd.DataFrame()
tabla_urgencia = pd.DataFrame()
tabla_operacion = pd.DataFrame()
tabla_enfermedad = pd.DataFrame()
tabla_especialidad = pd.DataFrame()
tabla_medico = pd.DataFrame()
tabla_quirofano = pd.DataFrame()

print("Creamos los vectores aleatorios para tabla_paciente")
#Generamos datos aleatorios para la tabla_paciente
bool_smoker = []
urgencia = []
id_expediente = []
num_urgencia_id = []
num_enfermedad_id = []
cont = 0
cont2 = 0
pacientes_ingresados = []
alea_Paises = []
enfermedad = []
vector_paises = df_paises['Albania'].tolist()
cont_urgencia = 0
lista_enfermedades= enfermedades['Nombres'].tolist()
#Asegurar valores distintos
#Añadir pais
print(len(df.prim_nombre))
for i in range(0, len(df.prim_nombre)):
    print(i)
    bool_smoker.insert(i,choice(["YES", "NO"]))
    id_expediente.insert(i, randrange(1111111, 9999999))
    num_pais_aleatorio = randrange(0, len(vector_paises))
    alea_Paises.insert(i, vector_paises[num_pais_aleatorio])
    choice_val = choice(["ENFERMEDAD", "URGENCIA"])
    num_urgencia = randrange(0, 200)
    num_enfermedad = randrange(0, len(lista_enfermedades))
    temp_urgencia = choice(["NULL", num_urgencia])
    temp_enfermedad = choice(["NULL", num_enfermedad])
    if choice_val == "URGENCIA":
        urgencia.insert(i, choice(["NULL", num_urgencia]))
        enfermedad.insert(i, "NULL")
        if temp_urgencia != "NULL":
            num_urgencia_id.insert(cont, num_urgencia)
            cont = cont + 1
    elif choice_val == "ENFERMEDAD":
        enfermedad.insert(i, choice(["NULL", num_enfermedad]))
        urgencia.insert(i, "NULL")
        if temp_enfermedad != "NULL":
            num_enfermedad_id.insert(cont2, num_enfermedad)
            cont2 = cont2 + 1
            pacientes_ingresados.insert(cont2, df.prim_nombre[i] + df.apellido_pat)


#Ahora elige toda la lista
print("Creamos los vectores aleatorios para tabla_urgencia")
enum_gravedad = []
boolean_ambulancia = []
id_operacion = []
lista_especialidades = especialidades['Especialidades'].tolist()
especialidad = []
id_toperacion = []
id_tespecialidad = []
tupla_ingreso = []
cont_operacion = 0
cont_especialidad = 0
for i in range(0, cont):
    enum_gravedad.insert(i, choice(["MUY ALTA", "ALTA", "MEDIA", "BAJA"]))
    boolean_ambulancia.insert(i, choice(["YES", "NO"]))
    tupla_ingreso.insert(i, choice(["YES", "NO"]))
    id_operacion_num = randrange(1111111, 9999999)
    num_especialidad = randrange(0, len(lista_especialidades))
    especialidad.insert(i, choice(["NULL", lista_especialidades[num_especialidad]]))
    id_operacion.insert(i, choice(["NULL", id_operacion_num]))
    if id_operacion[i] != "NULL":
        id_toperacion.insert(cont_operacion, int(id_operacion_num))
        cont_operacion = cont_operacion + 1

    if especialidad[i] != "NULL":
        id_tespecialidad.insert(cont_operacion, lista_especialidades[num_especialidad])
        cont_especialidad = cont_especialidad + 1


print("Creamos los vectores aleatorios para tabla_operacion")

id_quirofano1 = []
nombre_medico = []
for i in range(0, cont_operacion):
    id_quirof = randrange(0, 25)
    num_medico = randrange(0, len(doctor_names.Name))
    nombre_medico.insert(i,doctor_names.Name[num_medico])
    id_quirofano1.insert(i, id_quirofano1)


print("Creamos los vectores aleatorios para tabla_medico")
especialidad_tabla_medico = []
id_medico = []
for i in range(0, len(doctor_names.Name)):
    id_medico.insert(i, i)
    especialidad_aleatoria = randrange(0, len(lista_especialidades))
    especialidad_tabla_medico.insert(i, lista_especialidades[especialidad_aleatoria])


print("Creamos los vectores aleatorios para tabla_quirofano")
puerta_quirofano = ["A", "B", "C", "D", "E"]
planta_quirofano = []
puerta_quirofano_fin = []
id_quirofano= []
cont = 0
for i in range(0, 5):
    for p in range(0, 5):
        id_quirofano.insert(cont, cont)
        puerta_quirofano_fin.insert(cont, puerta_quirofano[p] )
        planta_quirofano.insert(cont, i)
        cont = cont + 1




###############################################################################3
#Falta poner para introducir la especialidad a la que se asocia una enfermedad
############################################################################3###


print("Creamos los vectores aleatorios para tabla_enfermedad")
cura_conocida = []
ingreso = []
contagiosa = []
hereditaria = []
tratamiento = []
especialidad_tenfermedad = []

for i in range(0, len(lista_enfermedades)):
    hereditaria.insert(i, choice(["YES", "NO"]))
    if hereditaria[i] == "YES":
        cura_conocida.insert(i, "NO")
    else:
        cura_conocida.insert(i, choice(["YES", "NO"]))
    if cura_conocida[i] == "YES":
        tratamiento.insert(i, choice(["YES", "NO"]))
    else:
        tratamiento.insert(i, "NO")

    if hereditaria[i] == "NO":
        contagiosa.insert(i, choice(["YES", "NO"]))
    else:
        contagiosa.insert(i, "NO")
    ingreso.insert(i, choice(["YES", "NO"]))

    especialidad_aleatoria = randrange(0, len(lista_especialidades))
    especialidad_tenfermedad.insert(i, lista_especialidades[especialidad_aleatoria])







# Comprobamos que los datos aleatorios se han generado correctamente





# Guardamos los datos generados aleatoriamente

#Paciente
tabla_paciente['num_expediente'] = id_expediente
tabla_paciente['prim_nombre'] = df.prim_nombre
tabla_paciente['apellido_pat'] = df.apellido_pat
tabla_paciente['fecha_ingreso'] = df.fuerocomun_desapfecha
tabla_paciente['hora_ingreso'] = df.fuerocomun_desaphora
tabla_paciente['sexo_paceinte'] = df.fuerocomun_sexo
tabla_paciente['edad_paciente'] = df.fuerocomun_edad
tabla_paciente['urgencia'] = urgencia
tabla_paciente['Enfermedad'] = enfermedad
tabla_paciente['Pais_origen'] = alea_Paises
tabla_paciente['smoker'] = bool_smoker
print(list(tabla_paciente))

cura_conocida = []
ingreso = []
contagiosa = []
hereditaria = []
tratamiento = []
#Enfermedad
tabla_enfermedad['Nombre_enfermedad'] = lista_enfermedades
tabla_enfermedad['Ingreso'] = ingreso
tabla_enfermedad['Cura_conocida'] = cura_conocida
tabla_enfermedad['Contagiosa'] = contagiosa
tabla_enfermedad['Hereditaria'] = hereditaria
tabla_enfermedad['Tratamiento'] = tratamiento
tabla_enfermedad['Especialidad'] = especialidad_tenfermedad

#Urgencia
num_urgencia_id = [int(x) for x in num_urgencia_id]
num_urgencia_id.sort()
tabla_urgencia['id_urgencia'] = num_urgencia_id
value_urgencia = [df.fuerocomun_descripcion[x] for x in num_urgencia_id]
tabla_urgencia['Causa'] = value_urgencia
tabla_urgencia['Gravedad'] = enum_gravedad
tabla_urgencia['Uso_ambulancia'] = boolean_ambulancia
tabla_urgencia['Necesita_operacion'] = id_operacion
tabla_urgencia['Especialidad'] = especialidad
print(list(tabla_urgencia))

#Operacion
id_toperacion.sort()
tabla_operacion['id_urgencia'] = id_toperacion
tabla_operacion['Quirofano'] = id_quirofano1
tabla_operacion['Cirujano'] = nombre_medico
tabla_operacion['Hora'] = df.fuerocomun_desaphora[300:len(nombre_medico)+300]
print(list(tabla_operacion))


# Medicos
tabla_medico['Medico'] = doctor_names.Name
tabla_medico['ID_Medico'] = id_medico
tabla_medico['Especialidad_medico'] = especialidad_tabla_medico

#Quirófano
tabla_quirofano['ID'] = id_quirofano
tabla_quirofano['Puerta'] = puerta_quirofano_fin
tabla_quirofano['Planta'] = planta_quirofano

#Especialidad
tabla_especialidad['Nombre_especialidad'] = lista_especialidades

print(len(doctor_names.Name))
print(len(lista_especialidades))
#Almacenamos los resultados en .csv
tabla_paciente.to_csv('../Result_datasets/tabla_paciente.csv', sep='\t', encoding='utf-8')
tabla_urgencia.to_csv('../Result_datasets/tabla_urgencia.csv', sep='\t', encoding='utf-8')
tabla_operacion.to_csv('../Result_datasets/tabla_operacion.csv', sep='\t', encoding='utf-8')
tabla_quirofano.to_csv('../Result_datasets/tabla_quirofano.csv', sep='\t', encoding='utf-8')
tabla_medico.to_csv('../Result_datasets/tabla_medico.csv', sep='\t', encoding='utf-8')