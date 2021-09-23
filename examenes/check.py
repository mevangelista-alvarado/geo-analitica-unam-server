import sympy

def default(resp_correcta, alumno_respuesta):
    """"""
    return 1 if resp_correcta == alumno_respuesta else 0

def check_python_is_answer(resp_correcta, alumno_respuesta):
    return 1 if resp_correcta.lower() == alumno_respuesta.lower() else 0

def check_pablo_is_answer(resp_correcta, alumno_respuesta):
    return 1 if resp_correcta.lower() == alumno_respuesta.lower() else 0
