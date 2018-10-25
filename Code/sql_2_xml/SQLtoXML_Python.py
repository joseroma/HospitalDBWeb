#!/usr/bin/python
import sys, os, datetime
import pymysql
import lxml.etree as ET

cd = os.path.dirname(os.path.abspath(__file__))

# SET FILE NAME VALUES
i = datetime.datetime.today()
todaydate = i.strftime('%Y') + i.strftime('%m') + i.strftime('%d')


# DB CONNECTION AND QUERY
db = pymysql.connect(host='localhost', port=3306, user="root",
                      passwd="admin", db="mydb")
cur = db.cursor()
cur.execute('SELECT `*` FROM MEDICO, QUIROFANO')
print(cur.fetchall())
# WRITING XML FILE
root = ET.Element('HOSPITAL')

for row in cur.fetchall():
    paciente = ET.SubElement(root, "PACIENTES")
    ET.SubElement(paciente, "num_expediente").text = str(row[0])
    ET.SubElement(paciente, "nombre").text = str(row[1])
    ET.SubElement(paciente, "apellido").text = row[2]
    ET.SubElement(paciente, "edad").text = str(row[3])
    ET.SubElement(paciente, "sexo").text = row[4]
    ET.SubElement(paciente, "fecha_ingreso").text = str(row[5])
    ET.SubElement(paciente, "hora_ingreso").text = str(row[6])
    ET.SubElement(paciente, "pais_origen").text = row[7]
    ET.SubElement(paciente, "fumador").text = row[8]
    ET.SubElement(paciente, "URGENCIA_id_urgencia").text = str(row[9])
    #URGENCIA
    urgencia = ET.SubElement(paciente, "URGENCIA")
    ET.SubElement(urgencia, "id_urgencia").text = str(row[0])
    ET.SubElement(urgencia, "causa").text = str(row[1])
    ET.SubElement(urgencia, "gravedad").text = row[2]
    ET.SubElement(urgencia, "uso_ambulancia").text = str(row[3])
    ET.SubElement(urgencia, "necesita_operacion").text = row[4]
    ET.SubElement(urgencia, "ingreso").text = str(row[5])
    ET.SubElement(urgencia, "ESPECIALIDAD_nombre_especialidad").text = str(row[6])
    ET.SubElement(urgencia, "OPERACION_id_operacion").text = row[7]
    # OPERACION
    operacion = ET.SubElement(urgencia, "OPERACION")
    ET.SubElement(operacion, "id_operacion").text = str(row[0])
    ET.SubElement(operacion, "hora").text = str(row[1])
    ET.SubElement(operacion, "cirujano").text = row[2]
    ET.SubElement(operacion, "QUIROFANO_id_quirofano").text = str(row[3])
    #ESPECIALIDAD
    especialidad = ET.SubElement(urgencia, "ESPECIALIDAD")
    ET.SubElement(especialidad, "nombre_especialidad").text = str(row[0])
    # quirofano
    quirofano = ET.SubElement(operacion, "QUIROFANO")
    ET.SubElement(quirofano, "id_quirofano").text = str(row[0])
    ET.SubElement(quirofano, "planta").text = row[1]
    ET.SubElement(quirofano, "puerta").text = row[2]
    #MEDICO
    medico = ET.SubElement(especialidad, "MEDICO")
    ET.SubElement(medico, "id_medico").text = str(row[0])
    ET.SubElement(medico, "nombre_medico").text = row[1]
    ET.SubElement(medico, "ESPECIALIDAD_nombre_especialidad").text = row[2]





# CLOSE CURSOR AND DATABASE
cur.close()
db.close()

tree_out = (ET.tostring(root, pretty_print=True))

xmlfile = open(os.path.join(cd, 'CLData_Output.xml'),'wb')
xmlfile.write(tree_out)
xmlfile.close()


# SUCCESS MESSAGE
print("Successfully migrated SQL to XML data!")
