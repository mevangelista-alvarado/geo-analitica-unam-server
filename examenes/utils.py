import random
import sympy
import datetime
import ast
from sympy.parsing.latex import parse_latex


def replace_random_int(index, pregunta, str_to_change='random'):
    """"""
    numbers = range(1,10)
    if index == 0:
        numbers = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]

    count_random = pregunta.count(str_to_change)
    i = 0
    while i < count_random:
        pregunta = pregunta.replace(str_to_change, str(random.choice(numbers)), 1)
        i = i + 1
    return pregunta


def obtener_formato_html(pregunta, ):
    inicio = pregunta.find("$")
    final = pregunta.rfind("$")
    # sympy_str = ast.literal_eval(pregunta[inicio+1:final])
    sympy_str = f'{pregunta[inicio+1:final]}'

    sympy_obj = sympy.sympify(pregunta[inicio+1:final], evaluate=False)
    if isinstance(sympy_str, list):
        sympy_obj = sympy.Matrix(sympy_str)
    # TODO Poisson Geometry, i.e if isinstance(sympy_str, dict):
    sympy_latex = sympy.latex(sympy_obj)

    pregunta_html = f"{pregunta[0: inicio]} ${sympy_latex}$ {pregunta[final+1:]}"
    return pregunta_html


def calificacion_final(array):
    """"""
    sum_aux_calificacion = 0
    sum_calificacion = 0
    for index in range(0,5):
        sum_calificacion = sum_calificacion + array[index]
        if index != 4:
            sum_aux_calificacion = sum_aux_calificacion + array[index]

    partial_calificacion = regla_de_tres(sum_aux_calificacion)
    if partial_calificacion == "10":
        return partial_calificacion
    else:
        return regla_de_tres(sum_calificacion)


def regla_de_tres(partial_calificacion):
    """ 4                    --> 10
        partial_calificacion --> x
    """
    partial_calificacion = (partial_calificacion*10)/4
    if int(partial_calificacion) == 10:
        return "10"
    else:
        partial_calificacion = float(partial_calificacion)
        return f"{partial_calificacion:.2f}"
