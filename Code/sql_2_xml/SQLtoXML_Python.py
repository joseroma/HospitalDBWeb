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
cur.execute('SELECT `*` FROM PACIENTE;')

cur1 = db.cursor()
cur1.execute('SELECT `*` FROM URGENCIA;')

cur2 = db.cursor()
cur2.execute('SELECT `*` FROM OPERACION;')

cur3 = db.cursor()
cur3.execute('SELECT `*` FROM ESPECIALIDAD;')

cur4 = db.cursor()
cur4.execute('SELECT `*` FROM QUIROFANO;')

cur5 = db.cursor()
cur5.execute('SELECT `*` FROM MEDICO;')


# WRITING XML FILE

paciente = ET.Element('PACIENTE')
for row in cur.fetchall():
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
for row1 in cur1.fetchall():
    urgencia = ET.SubElement(paciente, "URGENCIA")
    ET.SubElement(urgencia, "id_urgencia").text = str(row1[0])
    ET.SubElement(urgencia, "causa").text = str(row1[1])
    ET.SubElement(urgencia, "gravedad").text = row1[2]
    ET.SubElement(urgencia, "uso_ambulancia").text = str(row1[3])
    ET.SubElement(urgencia, "necesita_operacion").text = row1[4]
    ET.SubElement(urgencia, "ingreso").text = str(row1[5])
    ET.SubElement(urgencia, "ESPECIALIDAD_nombre_especialidad").text = str(row1[6])
#    ET.SubElement(urgencia, "OPERACION_id_operacion").text = str(row1[7])
    # OPERACION.
for row2 in cur2.fetchall():
    operacion = ET.SubElement(urgencia, "OPERACION")
    ET.SubElement(operacion, "id_operacion").text = str(row2[0])
    ET.SubElement(operacion, "hora").text = str(row2[1])
    ET.SubElement(operacion, "cirujano").text = row2[2]
    ET.SubElement(operacion, "QUIROFANO_id_quirofano").text = str(row2[3])
    #ESPECIALIDAD
for row3 in cur3.fetchall():
    especialidad = ET.SubElement(urgencia, "ESPECIALIDAD")
    ET.SubElement(especialidad, "nombre_especialidad").text = str(row3[0])
    # quirofano
for row4 in cur4.fetchall():
    quirofano = ET.SubElement(operacion, "QUIROFANO")
    ET.SubElement(quirofano, "id_quirofano").text = str(row4[0])
    ET.SubElement(quirofano, "planta").text = str(row4[1])
    ET.SubElement(quirofano, "puerta").text = row4[2]
    #MEDICO
for row5 in cur5.fetchall():
    medico = ET.SubElement(especialidad, "MEDICO")
    ET.SubElement(medico, "id_medico").text = str(row5[0])
    ET.SubElement(medico, "nombre_medico").text = row5[1]
    ET.SubElement(medico, "ESPECIALIDAD_nombre_especialidad").text = row5[2]





# CLOSE CURSOR AND DATABASE
cur.close()
db.close()

tree_out = (ET.tostring(paciente, pretty_print=True))

xmlfile = open(os.path.join(cd, 'CLData_Output.xml'),'wb')
xmlfile.write(tree_out)
xmlfile.close()


# SUCCESS MESSAGE
print("Successfully migrated SQL to XML data!")
