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
cur.execute('SELECT (`num_expediente`, `nombre`,`apellido`,`edad`,`sexo`,`fecha_ingreso`,`hora_ingreso`,`pais_origen`,`fumador`,`URGENCIA_id_urgencia`,`id_urgencia`,`causa`,`gravedad`,`uso_ambulancia`,`uso_ambulancia`,`ingreso`,`OPERACION_id_operacion`,`ESPECIALIDAD_nombre_especialidad`,`id_operacion`,`hora`,`cirujano`,`QUIROFANO_id_quirofano`,`nombre_especialidad`,`id_quirofano`,`planta`,`puerta`,`id_medico`,`nombre_medico`,`medico.ESPECIALIDAD_nombre_especialidad`) FROM (paciente, urgencia, operacion, especialidad, quirofano, medico) WHERE (`PACIENTE.URGENCIA_id_urgencia`=`URGENCIA.id_urgencia`) AND (`URGENCIA.OPERACION_id_operacion`=`OPERACION.id_operacion`) AND (`URGENCIA.ESPECIALIDAD_nombre_especialidad`=`ESPECIALIDAD.nombre_especialidad`) AND (`OPERACION.QUIROFANO_id_quirofano` =`QUIROFANO.id_quirofano`) AND (`MEDICO.ESPECIALIDAD_nombre_especialidad`=`ESPECIALIDAD.nombre_especialidad`);')
#cur.execute('SELECT `*` FROM (PACIENTE, URGENCIA, OPERACION, ESPECIALIDAD, QUIROFANO, MEDICO) WHERE (`PACIENTE.URGENCIA_id_urgencia`=`URGENCIA.id_urgencia`) AND (`URGENCIA.OPERACION_id_operacion`=`OPERACION.id_operacion`) AND (`URGENCIA.ESPECIALIDAD_nombre_especialidad`=`ESPECIALIDAD.nombre_especialidad`) AND (`OPERACION.QUIROFANO_id_quirofano` =`QUIROFANO.id_quirofano`) AND (`MEDICO.ESPECIALIDAD_nombre_especialidad`=`ESPECIALIDAD.nombre_especialidad`);')




# WRITING XML FILE


for row in cur.fetchall():
    paciente = ET.Element('PACIENTE')
    ET.SubElement(paciente, "num_expediente").text = str(row[0])
    ET.SubElement(paciente, "nombre").text = str(row[1])
    ET.SubElement(paciente, "apellido").text = row[2]
    ET.SubElement(paciente, "edad").text = str(row[3])
    ET.SubElement(paciente, "sexo").text = row[4]
    ET.SubElement(paciente, "fecha_ingreso").text = str(row[5])
    ET.SubElement(paciente, "hora_ingreso").text = str(row[6])
    ET.SubElement(paciente, "pais_origen").text = str(row[7])
    ET.SubElement(paciente, "fumador").text = row[8]
    ET.SubElement(paciente, "URGENCIA_id_urgencia").text = str(row[9])
    urgencia = ET.SubElement(paciente, "URGENCIA")
    ET.SubElement(urgencia, "id_urgencia").text = str(row[10])
    ET.SubElement(urgencia, "causa").text = str(row[11])
    ET.SubElement(urgencia, "gravedad").text = row[12]
    ET.SubElement(urgencia, "uso_ambulancia").text = str(row[13])
    ET.SubElement(urgencia, "ingreso").text = str(row[14])
    ET.SubElement(urgencia, "ESPECIALIDAD_nombre_especialidad").text = str(row[15])
    ET.SubElement(urgencia, "OPERACION_id_operacion").text = str(row[16])
    operacion = ET.SubElement(urgencia, "OPERACION")
    ET.SubElement(operacion, "id_operacion").text = str(row[17])
    ET.SubElement(operacion, "hora").text = str(row[18])
    ET.SubElement(operacion, "cirujano").text = row[19]
    ET.SubElement(operacion, "QUIROFANO_id_quirofano").text = str(row[20])
    #ESPECIALIDAD
    especialidad = ET.SubElement(urgencia, "ESPECIALIDAD")
    ET.SubElement(especialidad, "nombre_especialidad").text = str(row[21])
    # quirofano
    quirofano = ET.SubElement(operacion, "QUIROFANO")
    ET.SubElement(quirofano, "id_quirofano").text = str(row[22])
    ET.SubElement(quirofano, "planta").text = str(row[23])
    ET.SubElement(quirofano, "puerta").text = row[24]
    #MEDICO
    medico = ET.SubElement(especialidad, "MEDICO")
    ET.SubElement(medico, "id_medico").text = str(row[25])
    ET.SubElement(medico, "nombre_medico").text = str(row[26])
    ET.SubElement(medico, "ESPECIALIDAD_nombre_especialidad").text = str(row[27])





# CLOSE CURSOR AND DATABASE
cur.close()
db.close()

tree_out = (ET.tostring(paciente, pretty_print=True))

xmlfile = open(os.path.join(cd, 'CLData_Output.xml'),'wb')
xmlfile.write(tree_out)
xmlfile.close()


# SUCCESS MESSAGE
print("Successfully migrated SQL to XML data!")
