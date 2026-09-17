# Definición del Universo
estudiantes = {"Marcos", "Laura", "Carlos"}
profesores = {"Dr. Ruiz", "Dra. Salas"}
materias = {"Matemáticas", "Programación", "Física"}
aulas = {"A1", "Lab1"}
carreras = {"Ingeniería", "Diseño"}

rel_cursa = {("Marcos", "Matemáticas")}
rel_imparte = {("Dr. Ruiz", "Física")}
rel_asignada = {("Programación", "Lab1")}

# 1. Predicado: Estudiante(x)
def Estudiante(x):
    return x in estudiantes

# 2. Predicado: Profesor(x)
def Profesor(x):
    return x in profesores

# 3. Predicado: Materia(x)
def Materia(x):
    return x in materias

# 4. Predicado: Cursa(x, y)
def Cursa(x, y):
    return (x, y) in rel_cursa

# 5. Predicado: Imparte(x, y)
def Imparte(x, y):
    return (x, y) in rel_imparte

# 6. Predicado: Aula(x)
def Aula(x):
    return x in aulas

# 7. Predicado: Asignada(x, y)
def Asignada(x, y):
    return (x, y) in rel_asignada


print("--- 1. Estudiante(x) ---")
print(f"Positiva: Estudiante('Marcos') -> {Estudiante('Marcos')}")
print(f"Negativa: Estudiante('Dr. Ruiz') -> {Estudiante('Dr. Ruiz')}")

print("\n--- 2. Profesor(x) ---")
print(f"Positiva: Profesor('Dra. Salas') -> {Profesor('Dra. Salas')}")
print(f"Negativa: Profesor('Laura') -> {Profesor('Laura')}")

print("\n--- 3. Materia(x) ---")
print(f"Positiva: Materia('Programación') -> {Materia('Programación')}")
print(f"Negativa: Materia('Lab1') -> {Materia('Lab1')}")

print("\n--- 4. Cursa(x, y) ---")
print(f"Positiva: Cursa('Marcos', 'Matemáticas') -> {Cursa('Marcos', 'Matemáticas')}")
print(f"Negativa: Cursa('Dr. Ruiz', 'Matemáticas') -> {Cursa('Dr. Ruiz', 'Matemáticas')}")

print("\n--- 5. Imparte(x, y) ---")
print(f"Positiva: Imparte('Dr. Ruiz', 'Física') -> {Imparte('Dr. Ruiz', 'Física')}")
print(f"Negativa: Imparte('Carlos', 'Programación') -> {Imparte('Carlos', 'Programación')}")

print("\n--- 6. Aula(x) ---")
print(f"Positiva: Aula('A1') -> {Aula('A1')}")
print(f"Negativa: Aula('Matemáticas') -> {Aula('Matemáticas')}")

print("\n--- 7. Asignada(x, y) ---")
print(f"Positiva: Asignada('Programación', 'Lab1') -> {Asignada('Programación', 'Lab1')}")
print(f"Negativa: Asignada('Matemáticas', 'Laura') -> {Asignada('Matemáticas', 'Laura')}")