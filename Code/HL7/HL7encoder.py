import base64
from hl7apy import core
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def generarHL7_ORU_R01():
    print("Se ha pedido mandar un mensaje HL7 del tipo ORU_R01")
    hl7 = core.Message("ORU_R01")
    hl7.msh.msh_3 = input("FileType: (text or img)")
    hl7.msh.msh_4 = "SendingFac"
    hl7.msh.msh_5 = "ReceivingApp"
    hl7.msh.msh_6 = "ReceivingFac"
    hl7.msh.msh_9 = "ORU^R01^ORU_R01"
    hl7.msh.msh_10 = "168715"
    hl7.msh.msh_11 = "P"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_3 = "15"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_5 = "JOSE"

    ## OBR Segment -- Patient details
    patients_detail = "10000"
    if patients_detail == "":
        patients_detail = "10000"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_4 = patients_detail


    if(hl7.msh.msh_3.value == "img"):
        with open(input("ENTER -> File name"), "rb") as image_file:
            mri = (base64.b64encode(image_file.read()))
            mri = StringIO(str(mri, 'utf-8')).getvalue()
    else:
        f = open(input("ENTER -> File name"), "r")
        mri = f.read()
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_1 = "1"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_2 = "ED"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_3 = "OWL"
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5 = mri
    hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_11 = "F"  # Observ Result Status -- "F" meaning 'Final result'
    hl7.validate()

    return(hl7)


