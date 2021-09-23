from .utils import replace_random_int
from .soluciones import get_solution_from_anwser, python_is_answer, pablo_is_answer
from .check import default, check_python_is_answer, check_pablo_is_answer

QUESTIONS = [
    (0, "¿Cuál es la notación en python de $sqrt(random)$?"),
    (1, "¿Cuál es la notación en python de $random**random$?"),
    (2, "¿Cuál es la notación en python de $random*random$?"),
    (3, "¿Qué lenguaje de programación aprenderas en el curso"),
    (4, "¿Cual es el nombre del profesor que imparte este curso?"),
]

QUESTIONS_INFO = {
    0: {
        "question": "¿Cuál es la notación en python de $sqrt(random)$?",
        "create_question": replace_random_int,
        "question_type": "dymanic",
        "correct_answer": get_solution_from_anwser,
        "create_answers": None,
        "answer_type": "input",
        "check_answer": default,
    },
    1: {
        "question": "¿Cuál es la notación en python de $random**random$?",
        "create_question": replace_random_int,
        "question_type": "dymanic",
        "correct_answer": get_solution_from_anwser,
        "create_answers": None,
        "answer_type": "input",
        "check_answer": default,
    },
    2: {
        "question": "¿Cuál es la notación en python de $random*random$?",
        "create_question": replace_random_int,
        "question_type": "dymanic",
        "correct_answer": get_solution_from_anwser,
        "create_answers": None,
        "answer_type": "input",
        "check_answer": default,
    },
    3: {
        "question": "¿Qué lenguaje de programación aprenderas en el curso",
        "create_question": None,
        "question_type": "static",
        "correct_answer": python_is_answer,
        "create_answers": None,
        "answer_type": "input",
        "check_answer": check_python_is_answer,
    },
    4: {
        "question": "¿Cual es el nombre del profesor que imparte este curso?",
        "create_question": None,
        "question_type": "static",
        "correct_answer": pablo_is_answer,
        "create_answers": None,
        "answer_type": "input",
        "check_answer": check_pablo_is_answer,
    }
}
