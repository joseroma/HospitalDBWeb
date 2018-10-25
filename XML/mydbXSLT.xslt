<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
    
    <h2>PACIENTE</h2> <!--PACIENTE-->
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
        <th>URGENCIA_id_urgencia</th>
      </tr>
      <xsl:for-each select="Paciente">
        <tr>
          <td><xsl:value-of select="num_expediente"/></td>
          <td><xsl:value-of select="nombre"/></td>
          <td><xsl:value-of select="apellido"/></td>
          <td><xsl:value-of select="edad"/></td>
          <td><xsl:value-of select="sexo"/></td>
          <td><xsl:value-of select="fecha_ingreso"/></td>
          <td><xsl:value-of select="hora_ingreso"/></td>
          <td><xsl:value-of select="fumador"/></td>
          <td><xsl:value-of select="URGENCIA_id_urgencia"/></td>
        </tr>
      </xsl:for-each>
    </table>

    <h2>URGENCIA</h2> <!--URGENCIA-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>id_urgencia</th>
        <th>causa</th>
        <th>gravedad</th>
        <th>uso_ambulancia</th>
        <th>necesita_operacion</th>
        <th>ingreso</th>
        <th>OPERACION_id_operacion</th>
        <th>ESPECIALIDAD_nombre_especialidad</th>
      </tr>
      <xsl:for-each select="Paciente/Urgencia">
        <tr>
          <td><xsl:value-of select="id_urgencia"/></td>
          <td><xsl:value-of select="causa"/></td>
          <td><xsl:value-of select="gravedad"/></td>
          <td><xsl:value-of select="uso_ambulancia"/></td>
          <td><xsl:value-of select="ingreso"/></td>
        </tr>
      </xsl:for-each>
    </table>

    <h2>ESPECIALIDAD</h2> <!--ESPECIALIDAD-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>nombre_especialidad</th>
      </tr>
      <xsl:for-each select="Paciente/Urgencia/Especialidad">
        <tr>
          <td><xsl:value-of select="nombre_especialidad"/></td>
        </tr>
      </xsl:for-each>
    </table>

    <h2>MEDICO</h2> <!--MEDICO-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>id_medico</th>
        <th>nombre_medico</th>
      </tr>
      <xsl:for-each select="Paciente/Urgencia/Especialidad/Medico">
        <tr>
          <td><xsl:value-of select="id_medico"/></td>
          <td><xsl:value-of select="nombre_medico"/></td>
        </tr>
      </xsl:for-each>
    </table>

    <h2>OPERACION</h2> <!--OPERACION-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>id_operacion</th>
        <th>hora</th>
        <th>cirujano</th>
      </tr>
      <xsl:for-each select="Paciente/Urgencia/Operacion">
        <tr>
          <td><xsl:value-of select="id_operacion"/></td>
          <td><xsl:value-of select="hora"/></td>
          <td><xsl:value-of select="cirujano"/></td>
        </tr>
      </xsl:for-each>
    </table>


    <h2>QUIROFANO</h2> <!--QUIROFANO-->
    <table border="1">
      <tr bgcolor="#2E9AFE">
        <th>id_quirofano</th>
        <th>planta</th>
        <th>puerta</th>
      </tr>
      <xsl:for-each select="Paciente/Urgencia/Operacion/Quirofano">
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
