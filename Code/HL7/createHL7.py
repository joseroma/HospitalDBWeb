from hl7apy import core

hl7 = core.Message("ORU_R01")
hl7.msh.msh_3 = "SendingApp"
hl7.msh.msh_4 = "SendingFac"
hl7.msh.msh_5 = "ReceivingApp"
hl7.msh.msh_6 = "ReceivingFac"
hl7.msh.msh_9 = "ORU^R01^ORU_R01"
hl7.msh.msh_10 = "168715"
hl7.msh.msh_11 = "P"

# PID - Patient Identification
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_3 = "1"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_5 = "SARFATI^MICHAEL"

## OBR Segment -- Patient details
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_4 = "10000"

from base64 import standard_b64encode
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

f = open("bones.owl", "r")
#mri = StringIO(standard_b64encode(f.read()))
mri = f.read()

hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_1 = "1"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_2 = "ED"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_3 = "PDF"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5 = mri  # As per the StringIO API, we call getvalue() to dump the results
#.getvalue()
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_11 = "F"  # Observ Result Status -- "F" meaning 'Final result'


hl7.validate()

print(hl7.msh.value)