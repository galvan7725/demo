print("Evaluacion de notas de alumnos")

def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Reprobado"
    return valoracion

nota1 = input()

print(evaluacion(int(nota1)))

print("Hola github")