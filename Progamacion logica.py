# UNIVERSO DE DISCURSO

estudiantes = {"Marcos", "Laura", "Carlos", "David", "Fabián", "Erick"}
profesores = {"Dr. Ruiz", "Dra. Salas"}
materias = {"Matemáticas", "Programación", "Física"}
aulas = {"A1", "Lab1"}
carreras = {"Ingeniería", "Diseño"}


# BASE DE CONOCIMIENTOS (Hechos relacionales)

rel_cursa = {
    ("Marcos", "Matemáticas"),
    ("David", "Programación"),
    ("Fabián", "Programación"),
    ("Erick", "Programación"),
    ("Marcos", "Programación")
}

rel_imparte = {
    ("Dr. Ruiz", "Física")
}

rel_asignada = {
    ("Programación", "Lab1")
}

rel_aprobado = {
    ("Laura", "Matemáticas")
}

rel_becado = {
    "Laura"
}

rel_tutor = {
    ("Dra. Salas", "Marcos")
}

rel_requisito = {
    ("Matemáticas", "Física")
}

rel_egresado = {
    "Carlos"
}

rel_inscrito = {
    ("Marcos", "Ingeniería"),
    ("David", "Programación"),
    ("Fabián", "Programación"),
    ("Erick", "Programación")
}

rel_jefedegrupo = {
    "Laura"
}

# PREDICADOS BASE (15 Predicados)
def Estudiante(x):
    return x in estudiantes

def Profesor(x):
    return x in profesores

def Materia(x):
    return x in materias

def Cursa(x, y):
    return (x, y) in rel_cursa

def Imparte(x, y):
    return (x, y) in rel_imparte

def Aula(x):
    return x in aulas

def Asignada(x, y):
    return (x, y) in rel_asignada

def Aprobado(x, y):
    return (x, y) in rel_aprobado

def Becado(x):
    return x in rel_becado

def Tutor(x, y):
    return (x, y) in rel_tutor

def Requisito(x, y):
    return (x, y) in rel_requisito

def Egresado(x):
    return x in rel_egresado

def Carrera(x):
    return x in carreras

def Inscrito(x, y):
    return (x, y) in rel_inscrito

def EsJefeDeGrupo(x):
    return x in rel_jefedegrupo

# LEYES Y REGLAS DE INFERENCIA

# Ley 1: Derecho a Inscribir Materia
# Puede_Inscribir(x, y) :- Aprobado(x, z) ∧ Requisito(z, y)
def Puede_Inscribir(estudiante, materia_destino):
    for materia_z in materias:
        if Aprobado(estudiante, materia_z) and Requisito(materia_z, materia_destino):
            return True
    return False

# Ley 2: Materia Activa (Ejemplo del pizarrón/clase)
# Materia_Activa(y) :- Inscrito(a, y) ∧ Inscrito(b, y) ∧ Inscrito(c, y) con a != b != c
def Materia_Activa(materia):
    alumnos_inscritos = {e for e in estudiantes if Cursa(e, materia) or Inscrito(e, materia)}
    return len(alumnos_inscritos) >= 3

# Ley 3: Estudiante de Excelencia
# Estudiante_Excelencia(x) :- Becado(x) ∧ EsJefeDeGrupo(x)
def Estudiante_Excelencia(estudiante):
    return Becado(estudiante) and EsJefeDeGrupo(estudiante)

# Ley 4: Materia en Carrera
# Materia_En_Carrera(m, c) :- Cursa(e, m) ∧ Inscrito(e, c)
def Materia_En_Carrera(materia, carrera):
    for e in estudiantes:
        if Cursa(e, materia) and Inscrito(e, carrera):
            return True
    return False

# Ley 5: Estudiante Matriculado Activo
# Estudiante_Activo(e) :- Inscrito(e, c) ∧ Cursa(e, m)
def Estudiante_Activo(estudiante):
    for c in carreras:
        for m in materias:
            if Inscrito(estudiante, c) and Cursa(estudiante, m):
                return True
    return False

# VERIFICACIÓN Y CONSULTAS
if __name__ == "__main__":
    print("         VERIFICACIÓN DE LOS 15 PREDICADOS BASE                   ")
   
    print(f"1.  Estudiante('Marcos')            [Positiva] -> {Estudiante('Marcos')}")
    print(f"    Estudiante('Dr. Ruiz')          [Negativa] -> {Estudiante('Dr. Ruiz')}")
    print(f"2.  Profesor('Dra. Salas')          [Positiva] -> {Profesor('Dra. Salas')}")
    print(f"    Profesor('Laura')               [Negativa] -> {Profesor('Laura')}")
    print(f"3.  Materia('Programación')         [Positiva] -> {Materia('Programación')}")
    print(f"    Materia('Lab1')                 [Negativa] -> {Materia('Lab1')}")
    print(f"4.  Cursa('Marcos', 'Matemáticas')  [Positiva] -> {Cursa('Marcos', 'Matemáticas')}")
    print(f"    Cursa('Dr. Ruiz', 'Matemáticas')[Negativa] -> {Cursa('Dr. Ruiz', 'Matemáticas')}")
    print(f"5.  Imparte('Dr. Ruiz', 'Física')   [Positiva] -> {Imparte('Dr. Ruiz', 'Física')}")
    print(f"    Imparte('Carlos', 'Programación')[Negativa]-> {Imparte('Carlos', 'Programación')}")
    print(f"6.  Aula('A1')                      [Positiva] -> {Aula('A1')}")
    print(f"    Aula('Matemáticas')             [Negativa] -> {Aula('Matemáticas')}")
    print(f"7.  Asignada('Programación', 'Lab1')[Positiva] -> {Asignada('Programación', 'Lab1')}")
    print(f"    Asignada('Matemáticas', 'Laura')[Negativa] -> {Asignada('Matemáticas', 'Laura')}")
    print(f"8.  Aprobado('Laura', 'Matemáticas')[Positiva] -> {Aprobado('Laura', 'Matemáticas')}")
    print(f"    Aprobado('Carlos', 'Programación')[Negativa]->{Aprobado('Carlos', 'Programación')}")
    print(f"9.  Becado('Laura')                 [Positiva] -> {Becado('Laura')}")
    print(f"    Becado('Carlos')                [Negativa] -> {Becado('Carlos')}")
    print(f"10. Tutor('Dra. Salas', 'Marcos')   [Positiva] -> {Tutor('Dra. Salas', 'Marcos')}")
    print(f"    Tutor('Marcos', 'Laura')        [Negativa] -> {Tutor('Marcos', 'Laura')}")
    print(f"11. Requisito('Matemáticas', 'Física')[Positiva]-> {Requisito('Matemáticas', 'Física')}")
    print(f"    Requisito('Física', 'Matemáticas')[Negativa]-> {Requisito('Física', 'Matemáticas')}")
    print(f"12. Egresado('Carlos')              [Positiva] -> {Egresado('Carlos')}")
    print(f"    Egresado('Marcos')              [Negativa] -> {Egresado('Marcos')}")
    print(f"13. Carrera('Ingeniería')           [Positiva] -> {Carrera('Ingeniería')}")
    print(f"    Carrera('Beca')                 [Negativa] -> {Carrera('Beca')}")
    print(f"14. Inscrito('Marcos', 'Ingeniería')[Positiva] -> {Inscrito('Marcos', 'Ingeniería')}")
    print(f"    Inscrito('Dra. Salas', 'Diseño')[Negativa] -> {Inscrito('Dra. Salas', 'Diseño')}")
    print(f"15. EsJefeDeGrupo('Laura')          [Positiva] -> {EsJefeDeGrupo('Laura')}")
    print(f"    EsJefeDeGrupo('Marcos')         [Negativa] -> {EsJefeDeGrupo('Marcos')}")

    print("             VERIFICACIÓN DE LEYES O REGLAS                       ")
   
    print(f"Ley 1: Puede_Inscribir('Laura', 'Física')     -> {Puede_Inscribir('Laura', 'Física')}")
    print(f"Ley 2: Materia_Activa('Programación')        -> {Materia_Activa('Programación')}")
    print(f"Ley 3: Estudiante_Excelencia('Laura')         -> {Estudiante_Excelencia('Laura')}")
    print(f"Ley 4: Materia_En_Carrera('Matemáticas', 'Ingeniería') -> {Materia_En_Carrera('Matemáticas', 'Ingeniería')}")
    print(f"Ley 5: Estudiante_Activo('Marcos')            -> {Estudiante_Activo('Marcos')}")