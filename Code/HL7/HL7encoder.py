from base64 import standard_b64encode
from hl7apy import core
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def generarHL7_ORU_R01():
    print("Se ha pedido mandar un mensaje HL7 del tipo ORU_R02.  Preparado para archivos OWL")
    hl7 = core.Message("ORU_R01")
    hl7.msh.msh_3 = "SendingApp"
    hl7.msh.msh_4 = "SendingFac"
    hl7.msh.msh_5 = "ReceivingApp"
    hl7.msh.msh_6 = "ReceivingFac"
    hl7.msh.msh_9 = "ORU^R01^ORU_R01"
    hl7.msh.msh_10 = "168715"
    hl7.msh.msh_11 = "P"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_3 = "15"  # input("ENTER -> Patients ID: ")
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_5 = "JOSE"  # "^".join([input("ENTER -> Patients Lastame: "), input("ENTER -> Patients Name: ")])

    ## OBR Segment -- Patient details
    patients_detail = "10000"  # input("ENTER -> Patients detail:")
    if patients_detail == "":
        patients_detail = "10000"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_4 = patients_detail

    f = open(input("ENTER -> File name"), "r")  # input("ENTER -> File name")
    # mri = StringIO(standard_b64encode(f.read()))
    mri = f.read()
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_1 = "1"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_2 = "ED"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_3 = "OWL"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5 = mri  # As per the StringIO API, we call getvalue() to dump the results
    # .getvalue()
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_11 = "F"  # Observ Result Status -- "F" meaning 'Final result'
    hl7.validate()
    return(hl7)


def generarHL7_ORU_R02():
    print("Se ha pedido mandar un mensaje HL7 del tipo ORU_R02. Preparado para imágenes")
    hl7 = core.Message("ORU_R02")
    hl7.msh.msh_3 = "SendingApp"
    hl7.msh.msh_4 = "SendingFac"
    hl7.msh.msh_5 = "ReceivingApp"
    hl7.msh.msh_6 = "ReceivingFac"
    hl7.msh.msh_9 = "ORU^R01^ORU_R01"
    hl7.msh.msh_10 = "168715"
    hl7.msh.msh_11 = "P"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_3 = "15"  # input("ENTER -> Patients ID: ")
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_5 = "JOSE"  # "^".join([input("ENTER -> Patients Lastame: "), input("ENTER -> Patients Name: ")])

    patients_detail = "10000"
    if patients_detail == "":
        patients_detail = "10000"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_4 = patients_detail

    f = open(input("ENTER -> File name"), "r")
    mri = StringIO(standard_b64encode(f.read()))
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_1 = "1"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_2 = "ED"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_3 = "OWL"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5 = mri.getvalue()  # As per the StringIO API, we call getvalue() to dump the results
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_11 = "F"  # Observ Result Status -- "F" meaning 'Final result'
    hl7.validate()
    return(hl7)