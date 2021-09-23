import sympy
import ast
from sympy.parsing.latex import parse_latex


# Custom create Questions Methods
# Custom Answers Methods
def get_solution_from_anwser(pregunta, html=False):
    """"""
    inicio = pregunta.find("$")
    final = pregunta.rfind("$")
    return f'{pregunta[inicio+1:final]}'

def python_is_answer(pregunta, html=False):
    return "python"

def pablo_is_answer(pregunta, html=False):
    return "pablo"
