<?xml version="1.0" encoding = "UFT-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
    <head>
      <link rel="stylesheet" href="style.css" type="text/css"/>
    </head>
  <body>
    
    <h2 align="center">PACIENTE</h2> <!--PACIENTE-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>num_expediente</th>
        <th>nombre</th>
        <th>apellido</th>
        <th>edad</th>
        <th>sexo</th>
        <th>fecha_ingreso</th>
        <th>hora_ingreso</th>
        <th>pais_origen</th>
        <th>fumador</th>
      </tr>
      <xsl:for-each select="note/HOSPITAL/PACIENTE">
        <tr>
          <td><xsl:value-of select="num_expediente"/></td>
          <td><xsl:value-of select="nombre"/></td>
          <td><xsl:value-of select="apellido"/></td>
          <td><xsl:value-of select="edad"/></td>
          <td><xsl:value-of select="sexo"/></td>
          <td><xsl:value-of select="fecha_ingreso"/></td>
          <td><xsl:value-of select="hora_ingreso"/></td>
          <td><xsl:value-of select="pais_origen"/></td>
          <td><xsl:value-of select="fumador"/></td>
        </tr>
      </xsl:for-each>
    </table>

    <h2 align="center">URGENCIA</h2> <!--URGENCIA-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>id_urgencia</th>
        <th>causa</th>
        <th>gravedad</th>
        <th>uso_ambulancia</th>
        <th>ingreso</th>
      </tr>
      <xsl:for-each select="note/HOSPITAL/PACIENTE/URGENCIA">
        <tr>
          <td><xsl:value-of select="id_urgencia"/></td>
          <td><xsl:value-of select="causa"/></td>
          <td><xsl:value-of select="gravedad"/></td>
          <td><xsl:value-of select="uso_ambulancia"/></td>
          <td><xsl:value-of select="ingreso"/></td>
        </tr>
      </xsl:for-each>
    </table>

    <h2 align="center">ESPECIALIDAD</h2> <!--ESPECIALIDAD-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>nombre_especialidad</th>
      </tr>
      <xsl:for-each select="note/HOSPITAL/PACIENTE/URGENCIA/ESPECIALIDAD">
        <tr>
          <td><xsl:value-of select="nombre_especialidad"/></td>
        </tr>
      </xsl:for-each>
    </table>

    <h2 align="center">MEDICO</h2> <!--MEDICO-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>id_medico</th>
        <th>nombre_medico</th>
      </tr>
      <xsl:for-each select="note/HOSPITAL/PACIENTE/URGENCIA/ESPECIALIDAD/MEDICO">
        <tr>
          <td><xsl:value-of select="id_medico"/></td>
          <td><xsl:value-of select="nombre_medico"/></td>
        </tr>
      </xsl:for-each>
    </table>

    <h2 align="center">OPERACION</h2> <!--OPERACION-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>id_operacion</th>
        <th>hora</th>
        <th>cirujano</th>
      </tr>
      <xsl:for-each select="note/HOSPITAL/PACIENTE/URGENCIA/OPERACION">
        <tr>
          <td><xsl:value-of select="id_operacion"/></td>
          <td><xsl:value-of select="hora"/></td>
          <td><xsl:value-of select="cirujano"/></td>
        </tr>
      </xsl:for-each>
    </table>


    <h2 align="center">QUIROFANO</h2> <!--QUIROFANO-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>id_quirofano</th>
        <th>planta</th>
        <th>puerta</th>
      </tr>
      <xsl:for-each select="note/HOSPITAL/PACIENTE/URGENCIA/OPERACION/QUIROFANO">
        <tr>
          <td><xsl:value-of select="id_quirofano"/></td>
          <td><xsl:value-of select="planta"/></td>
          <td><xsl:value-of select="puerta"/></td>
        </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
