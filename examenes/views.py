import sympy
import random
import ast
import datetime
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Examen, ExamenResuelto
# News
from .questions_info import QUESTIONS_INFO
from .utils import obtener_formato_html, calificacion_final

def ExamenesListView(request):
    """"""
    examenes = Examen.objects.filter(activo=True)
    return render(request, 'examenes/list.html', {'examenes': examenes})

def RenderExamenView(request, examen_id):
    """"""
    examen = Examen.objects.get(id=examen_id)
    template = 'examenes/detail.html'
    render_examen = dict()
    render_examen.update({"tema": examen.tema, "id": examen.id, "preguntas": []})


    for i in range(1, 6):
        if i == 1:
            _p = examen.pregunta1
        if i == 2:
            _p = examen.pregunta2
        if i == 3:
            _p = examen.pregunta3
        if i == 4:
            _p = examen.pregunta4
        if i == 5:
            _p = examen.pregunta5

        p = QUESTIONS_INFO[_p]
        p_base = p["question"]
        question_type = p["question_type"]
        answer_type = p["answer_type"]

        if question_type == "dymanic":
            question = p["create_question"](_p, p_base)
            question_html = obtener_formato_html(question)
        if question_type == "static":
            question = p_base
            question_html = p_base

        if answer_type == "input":
            correct_answer = p["correct_answer"](question)
            answers = None

        render_examen["preguntas"].append([i, question, question_html, correct_answer, answers, answer_type])

    return render(request, template, {'examen': render_examen})


def CheckExamenView(request):
    """"""
    if request.method == "POST":
        _id = request.POST['_id']
        tema = request.POST['tema']
        tiempo = request.POST['tiempo']
        matricula = request.user.matricula
        curso = request.user.curso
        examen = Examen.objects.get(id=_id)

        # Check if student has a examen
        qs = ExamenResuelto.objects.filter(examen_id=_id, numero_cuenta=matricula)
        if qs.count() > 0:
            print("EXAMEN REPETIDO")
            context = {'numero_cuenta': matricula, 'calificacion': qs[0].calificacion}
            return render(request, 'examenes/noexiste.html', context)

        # Check Examen
        calificacion = []
        solucion = dict()
        solucion.update({"tema": tema, "tiempo": request.POST['tiempo'], "examen_result": []})
        for i in range(1, 6):
            pregunta = request.POST[f'pregunta{i}']
            respuesta_correcta = request.POST[f'respuesta{i}']
            alumno_respuesta = request.POST[f'alumno{i}']
            if i == 1:
                _p = examen.pregunta1
            if i == 2:
                _p = examen.pregunta2
            if i == 3:
                _p = examen.pregunta3
            if i == 4:
                _p = examen.pregunta4
            if i == 5:
                _p = examen.pregunta5

            p = QUESTIONS_INFO[_p]
            resultado = p["check_answer"](respuesta_correcta, alumno_respuesta)
            calificacion.append(resultado)
            solucion["examen_result"].append((pregunta, respuesta_correcta, alumno_respuesta, resultado))

        cal_final = calificacion_final(calificacion)
        save_examen, msg_save_examen = save_examen_resuelto(_id, curso, tema, matricula, cal_final, tiempo, solucion["examen_result"])
        print(msg_save_examen)

        context = {'solucion': solucion, "calificacion_final": cal_final,
                   'numero_cuenta': matricula}

    return render(request, 'examenes/solucion.html', context)


def save_examen_resuelto(examen_id, curso, tema, cuenta, calif, tiempo, preguntas):
    try:
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        Examen = ExamenResuelto()
        Examen.examen_id = str(examen_id)
        Examen.tema = tema
        Examen.curso = curso
        Examen.numero_cuenta = cuenta
        Examen.tiempo = date
        Examen.calificacion = str(calif)
        Examen.pregunta1 = str(preguntas[0][0])
        Examen.respuesta1_correcta = str(preguntas[0][1])
        Examen.respuesta1_alumno = str(preguntas[0][2])
        Examen.respuesta1_calif = str(preguntas[0][3])
        Examen.pregunta2 = str(preguntas[1][0])
        Examen.respuesta2_correcta = str(preguntas[1][1])
        Examen.respuesta2_alumno = str(preguntas[1][2])
        Examen.respuesta2_calif = str(preguntas[1][3])
        Examen.pregunta3 = str(preguntas[2][0])
        Examen.respuesta3_correcta = str(preguntas[2][1])
        Examen.respuesta3_alumno = str(preguntas[2][2])
        Examen.respuesta3_calif = str(preguntas[2][3])
        Examen.pregunta4 = str(preguntas[3][0])
        Examen.respuesta4_correcta = str(preguntas[3][1])
        Examen.respuesta4_alumno = str(preguntas[3][2])
        Examen.respuesta4_calif = str(preguntas[3][3])
        Examen.pregunta5 = str(preguntas[4][0])
        Examen.respuesta5_correcta = str(preguntas[4][1])
        Examen.respuesta5_alumno = str(preguntas[4][2])
        Examen.respuesta5_calif = str(preguntas[4][3])
        Examen.save()
        return (True, f'[INFO] Calificación guardada en la Base de Datos exitosamente a la cuenta {cuenta}')
    except Exception as e:
        return (False, f'[ERROR] Al guardar calificación en la Base de Datos a la cuenta {cuenta}, ERROR: {e}')
