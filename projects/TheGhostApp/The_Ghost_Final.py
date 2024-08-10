import random
import turtle
import time

def bienvenida():
    #Esta función da la bienvenida al programa y
        #muestra los nombres de los autores.
    turtle.color('white')
    turtle.sety(0)
    style = ('Courier', 40, 'italic')
    turtle.write('The Ghost', move = False, font = style, align = 'center')
    turtle.sety(-70)
    style = ('Courier', 20, 'italic')
    turtle.write('A01383088 Juan Luis Flores Sánchez', move = False,
                 font = style, align = 'center')
    turtle.sety(-90)
    style = ('Courier', 20, 'italic')
    turtle.write('A01383479 Francisco Javier Macías Segura', move = False,
                 font = style, align = 'center')
    time.sleep(5)
    turtle.clear()
    
def intro():
    #Esta función es una animación que recibe al usuario con colores,
              #figuras y mensajes haciendolo más llamativo
    j1 = turtle.Turtle()
    turtle.bgcolor('black')
    j1.hideturtle()
    j1.setpos(-70,-270)
    j1.color('white')
    style = ('Times New Roman',30)
    j1.write('Cargando...', font = style)
    turtle.penup()
    turtle.setpos(0,0)
    turtle.hideturtle()
    turtle.bgcolor('black')
    turtle.pensize(3)
    turtle.speed(0)
    turtle.pendown()
    for i in range(6):
        for colours in ('red','magenta','blue','cyan',
                        'green','yellow','white'):
            turtle.color(colours)
            turtle.circle(100)
            turtle.left(10)
    turtle.penup()        
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    j1.clear()
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    j2 = turtle.Turtle()
    j2.hideturtle()
    j2.penup()
    j2.setpos(-290,250)
    j2.color('red')
    style = ('Times New Roman',40)
    j2.pendown()
    j2.write('ERROR, INTRUSO DETECTADO', font = style)
    j2.penup()
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    j2.clear()
    turtle.setpos(-125,250)
    turtle.color('white')
    style = ('Times New Roman',30)
    turtle.write('Por fin te encuentro...', font = style)
    turtle.penup()
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.penup()
    turtle.setpos(-170,-270)
    turtle.color('white')
    style = ('Times New Roman',30)
    turtle.write('¿Estás listo para desafiarme?', font = style)
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.clear()
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('red')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('blue')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.bgcolor('black')
    turtle.setpos(100,100)
    turtle.hideturtle()
    turtle.color('white')
    turtle.pensize(3)
    turtle.speed(0)
    turtle.left(120)
    turtle.pendown()
    for i in range(100):
        if 1 % 2 is 0:
            turtle.color('silver')
        else:
            turtle.color('gray')
        turtle.forward(200)
        turtle.left(91)
    turtle.penup
    turtle.down
    turtle.setpos(-100,0)
    turtle.color('yellow')
    style = ('Times New Roman',50)
    turtle.write('THE GHOST', font = style)
    time.sleep(3)
    
def menu():
    #Esta función imprime el menú y dirige al usuario a otras funciones
                        #dependiendo de su elección.
    turtle.clear()
    turtle.color('white')
    turtle.sety(0)
    style = ('Courier', 40, 'italic')
    turtle.write('Menú', move = False, font = style, align = 'center')
    turtle.sety(-30)
    style = ('Courier', 20, 'italic')
    turtle.write('1. Inicio de sesión', move = False, font = style,
                 align = 'center')
    turtle.sety(-60)
    style = ('Courier', 20, 'italic')
    turtle.write('2. Registro', move = False, font = style, align = 'center')
    turtle.sety(-90)
    style = ('Courier', 20, 'italic')
    turtle.write('3. Acerca de The Ghost', move = False, font = style,
                 align = 'center')
    turtle.sety(-120)
    style = ('Courier', 20, 'italic')
    turtle.write('4. Salir', move = False, font = style, align = 'center')
    time.sleep(2)
    ans = turtle.textinput('¿Qué desea hacer?',
                           'Ingrese su respuesta (1/2/3/4)')
    if ans == '1':
        turtle.clear()
        inicio_sesion()
    if ans == '2':
        turtle.clear()
        registro()
    if ans == '3':
        acerca()
    if ans == '4':
        salir()

def inicio_sesion():
    #Esta función lleva a cabo el inicio de sesión de los usuarios
       #independientemente de si son alumnos o profesores, después
    #según lo respondido los guiará a otras funciones dependiendo de
                             #sus elecciones.
    global user_name, grado, nombre, q, lista_alumnos, contrasena, grupo, \
           usuario_profesor, usuario
    turtle.color('white')
    turtle.sety(0)
    style = ('Courier', 40, 'italic')
    turtle.write('Inicio de sesión', move = False, font = style,
                 align = 'center')
    turtle.sety(-30)
    style = ('Courier', 20, 'italic')
    turtle.write('Sigue las instrucciones y contesta lo que se te indica',
                 move = False, font = style, align = 'center')
    time.sleep(2)
    ans = turtle.textinput('¿Eres alumno o profesor',
                           'Ingrese su respuesta (Alumno/Profesor)')
    ans = ans.lower()
    if ans == 'alumno':
        try:
            archivo_alumnos = open('Alumnos.txt', 'r')
            lista_alumnos = archivo_alumnos.readlines()
            archivo_alumnos.close()
            ans = turtle.textinput('Usuario Alumno',
                                   'Ingrese su usuario (Por ejemplo: @abdce)')
            q = 0
            for p in lista_alumnos:
                nombre_alumno, usuario_alumno, contrasena, usuario_profesor, \
                               grado, grupo, calificacion = p.split(',')
                if ans == usuario_alumno.strip():
                    while True:
                        ans = turtle.textinput('Contraseña Alumno',
                                               'Ingrese su contraseña')
                        if ans == contrasena.strip():
                            nombre = nombre_alumno.strip()
                            user_name = usuario_alumno.strip()
                            grado = grado.strip()
                            turtle.clear()
                            turtle.color('white')
                            turtle.sety(0)
                            style = ('Courier', 40, 'italic')
                            turtle.write('Bienvenido de nuevo,',
                                         move = False, font = style,
                                         align = 'center')
                            turtle.sety(-30)
                            style = ('Courier', 20, 'italic')
                            turtle.write(nombre_alumno, move = False,
                                         font = style, align = 'center')
                            turtle.sety(-60)
                            style = ('Courier', 20, 'italic')
                            turtle.write('Tu examen comenzará pronto.',
                                         move = False, font = style,
                                         align = 'center')
                            time.sleep(5)
                            leer_preguntas()
                            hacer_preguntas()
                            ans = turtle.textinput('Cerrar sesión',
                            'Escribe da Enter cuando desees regresar a menú')
                            menu()
                    menu()
                q = q + 1
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('Hubo un problema: No se ha encontrado el usuario.',
                         move = False, font = style, align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('Regresando a menú.', move = False, font = style,
                         align = 'center')
            time.sleep(3)
            menu()
        except:
            turtle.clear()
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('Hubo un error.', move = False, font = style,
                         align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('Regresando a menú.', move = False, font = style,
                         align = 'center')
            time.sleep(3)
            menu()
    elif ans == 'profesor':
        try:
            archivo_profesor = open('Profesores.txt', 'r')
            lista_profesores = archivo_profesor.readlines()
            archivo_profesor.close()
            ans = turtle.textinput('Usuario Profesor',
                                   'Ingrese su usuario (Por ejemplo: @abdce)')
            for i in lista_profesores:
                nombre, usuario, contraseña = i.split(',')
                if ans == usuario.strip():
                    while True:
                        ans = turtle.textinput('Contraseña Profesor',
                                               'Ingrese su contraseña')
                        if ans == contraseña.strip():
                            user = usuario.strip()
                            usuario = usuario
                            turtle.clear()
                            turtle.color('white')
                            turtle.sety(0)
                            style = ('Courier', 40, 'italic')
                            turtle.write('Bienvenido de nuevo,',
                                         move = False, font = style,
                                         align = 'center')
                            turtle.sety(-30)
                            style = ('Courier', 20, 'italic')
                            turtle.write(nombre.strip(), move = False,
                                         font = style, align = 'center')
                            turtle.sety(-60)
                            style = ('Courier', 20, 'italic')
                            turtle.write('La herramienta comenzará.',
                                         move = False, font = style,
                                         align = 'center')
                            profesor()
                            break
                    menu()
            turtle.clear()
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('Hubo un problema: No se ha encontrado el usuario.',
                         move = False, font = style, align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('Regresando a menú.', move = False, font = style,
                         align = 'center')
            time.sleep(3)
            menu()
        except:
            turtle.clear()
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('Hubo un error.', move = False, font = style,
                         align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('Regresando a menú.', move = False, font = style,
                         align = 'center')
            time.sleep(3)
            menu()
    else:
        turtle.clear()
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write('Hubo un problema: No se ha seleecionado una opción.',
                     move = False, font = style, align = 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write('Regresando a menú.', move = False, font = style,
                     align = 'center')
        time.sleep(3)
        menu()

def leer_preguntas():
    #Esta función esta enfocada en la lectura de el archivo que contiene las
          #preguntas y con la información de sus líneas se crea una lista.
    global preguntas
    try:
        archivo_preguntas = open('TheGhostPreguntas.txt', 'r')
        preguntas = archivo_preguntas.readlines()
        archivo_preguntas.close()
    except IOError as mensaje:
        turtle.clear()
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write('Hubo un error: ' + str(mensaje), move = False,
                     font = style, align = 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write('Regresando a menú.', move = False, font = style,
                     align = 'center')
        time.sleep(3)
        menu()
    
def hacer_preguntas():
    #Esta función procesa la lista creada en leer_preguntas() y con ella
    #escribe la pregunta, y genera posiciones al azar de las respuestas para
       #que no aparezcan en el mismo lugar siempre. También califica cada
        #respuesta a las preguntas, para después de eso dar un puntaje y
                                #calificación
    global preguntas, score, nombre, grado, user_name, q, lista_alumnos, \
           contrasena, grupo, usuario_profesor
    turtle.clear()
    score = 0
    b = 0
    for x in preguntas:
        pregunta, res1, res2, res3 = x.split(',')
        pos1 = random.randint(1, 3)
        pos2 = pos1
        pos3 = pos1
        res3 = res3.strip()
        while pos1 == pos2:
            pos2 = random.randint(1, 3)
        while pos3 == pos1 or pos3 == pos2:
            pos3 = random.randint (1, 3)
        turtle.sety(0)
        turtle.color('white')
        style = ('Courier', 20, 'italic')
        turtle.write(pregunta, move = False, font = style, align = 'center')
        if pos1 == 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('a) ' + res1, move = False, font = style,
                         align = 'center')
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('b) ' + res2, move = False, font = style,
                         align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('c) ' + res3, move = False, font = style,
                         align = 'center')
        if pos2 == 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('a) ' + res2, move = False, font = style,
                         align = 'center')
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('b) ' + res1, move = False, font = style,
                         align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('c) ' + res3, move = False, font = style,
                         align = 'center')
        if pos3 == 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('a) ' + res3, move = False, font = style,
                         align = 'center')
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('b) ' + res2, move = False, font = style,
                         align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('c) ' + res1, move = False, font = style,
                         align = 'center')
        time.sleep(2)
        ans = turtle.textinput('Respuesta', 'Ingrese su respuesta (a/b/c)')
        if pos1 == 1 and ans == 'a':
            score = score + 1
        if pos2 == 1 and ans == 'b':
            score = score + 1
        if pos3 == 1 and ans == 'c':
            score = score + 1
        turtle.clear()
        b = b + 1
        if grado == '1' and b == 10:
            break
        if grado == '2' and b == 20:
            break
        if grado == '3' and b == 30:
            break
    turtle.sety(0)
    style = ('Courier', 20, 'italic')
    turtle.write('Resultados de ' + nombre, move = False, font = style,
                 align = 'center')
    if grado == '1':
        puntaje = score / 10
        if puntaje < 0.7:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('No has sido competencia para mi. ', move = False,
                         font = style, align = 'center')
            turtle.color('white')
        if puntaje >= 0.7 and puntaje < 0.9:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado pero, ¡¡¡VOLVERÉ!!!...',
                         move = False, font = style, align = 'center')
            turtle.color('white')
        if puntaje >= 0.9 and puntaje < 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado...', move = False, font = style,
                         align = 'center')
            turtle.color('white')
        if puntaje >= 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es 100', move = False, font = style,
                         align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado, ha sido un honor perder ante ti.',
                         move = False, font = style, align = 'center')
            turtle.color('white')
    if grado == '2':
        puntaje = score / 20
        if puntaje < 0.7:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('No has sido competencia para mi. ', move = False,
                         font = style, align = 'center')
            turtle.color('white')
        if puntaje >= 0.7 and puntaje < 0.9:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado pero, ¡¡¡VOLVERÉ!!!...',
                         move = False, font = style, align = 'center')
            turtle.color('white')
        if puntaje >= 0.9 and puntaje < 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado...', move = False, font = style,
                         align = 'center')
            turtle.color('white')
        if puntaje >= 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es 100', move = False, font = style,
                         align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado, ha sido un honor perder ante ti.',
                         move = False, font = style, align = 'center')
            turtle.color('white')
    if grado == '3':
        puntaje = score / 30
        if puntaje < 0.7:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('No has sido competencia para mi. ', move = False,
                         font = style, align = 'center')
            turtle.color('white')
        if puntaje >= 0.7 and puntaje < 0.9:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado pero, ¡¡¡VOLVERÉ!!!...',
                         move = False, font = style, align = 'center')
            turtle.color('white')
        if puntaje >= 0.9 and puntaje < 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es ' + str(puntaje * 100), move = False,
                         font = style, align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado...', move = False, font = style,
                         align = 'center')
            turtle.color('white')
        if puntaje >= 1:
            turtle.sety(-30)
            style = ('Courier', 20, 'italic')
            turtle.write('Tu puntaje es 100', move = False, font = style,
                         align = 'center')
            turtle.sety(-60)
            turtle.color('red')
            style = ('Courier', 20, 'italic')
            turtle.write('Me has derrotado, ha sido un honor perder ante ti.',
                         move = False, font = style, align = 'center')
            turtle.color('white')
    puntaje = puntaje * 100
    if puntaje > 100:
        puntaje = 100
    puntaje = str(puntaje)
    try:
        arch_write = open('Alumnos.txt', 'w')
        r = 0
        for x in lista_alumnos:
            if q == r:
                arch_write.write(nombre + ',' + user_name + ',' + contrasena +
                ',' + usuario_profesor + ',' + grado + ',' + grupo + ','
                + puntaje + '\n')
            else:
                arch_write.write(x)
            r = r + 1
        arch_write.close()
        score = 0
    except:
        turtle.clear()
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write('Hubo un error. ', move = False, font = style,
                     align = 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write('Regresando a menú.', move = False, font = style,
                     align = 'center')
        time.sleep(3)
        menu()
        
def profesor():
    #Esta función se utiliza como menú de el profesor al iniciar sesión
              #y en el se dirige a donde el usuario elija.
    turtle.clear()
    turtle.color('white')
    turtle.sety(0)
    style = ('Courier', 40, 'italic')
    turtle.write('Profesor', move = False, font = style, align = 'center')
    turtle.sety(-30)
    style = ('Courier', 20, 'italic')
    turtle.write('1. Calificación por Alumno', move = False, font = style,
                 align = 'center')
    turtle.sety(-60)
    style = ('Courier', 20, 'italic')
    turtle.write('2. Califiación por Grupo', move = False, font = style,
                 align = 'center')
    turtle.sety(-90)
    style = ('Courier', 20, 'italic')
    turtle.write('3. Calificación general alumnos', move = False,
                 font = style, align = 'center')
    turtle.sety(-120)
    style = ('Courier', 20, 'italic')
    turtle.write('4. Cerrar sesión y salir', move = False, font = style,
                 align = 'center')
    time.sleep(2)
    ans = turtle.textinput('¿Qué desea hacer?',
                           'Ingrese su respuesta (1/2/3/4)')
    if ans == '1':
        calificacion_alumno()
    if ans == '2':
        calificacion_grupo()
    if ans == '3':
        calificacion_general()
    if ans == '4':
        menu()
    
def calificacion_alumno():
    #Esta función se especializa en obtener la calificación de un alumno
               #en particular seleccionado por un profesor.
    global user, usuario
    turtle.clear()
    try:
        arch_leer = open('Alumnos.txt','r')
        lista = arch_leer.readlines()
        arch_leer.close()
        ans = turtle.textinput('Nombre alumno',
                               'Escriba el nombre de su alumno')
        for x in lista:
            nombre_alumno, usuario_alumno, contrasena_alumno, \
                usuario_profesor, grado, grupo, calificacion = x.split(',')
            if ans.strip() == nombre_alumno.strip():
                turtle.clear()
                turtle.color('white')
                turtle.sety(0)
                style = ('Courier', 40, 'italic')
                turtle.write('Profesor', move = False, font = style,
                             align = 'center')
                turtle.sety(-30)
                style = ('Courier', 20, 'italic')
                turtle.write('El alumno', move = False, font = style,
                             align = 'center')
                turtle.sety(-60)
                style = ('Courier', 20, 'italic')
                turtle.write(nombre_alumno, move = False, font = style,
                             align = 'center')
                turtle.sety(-90)
                style = ('Courier', 20, 'italic')
                turtle.write('tiene una calificación de', move = False,
                             font = style, align = 'center')
                turtle.sety(-120)
                style = ('Courier', 20, 'italic')
                turtle.write(str(calificacion.strip()), move = False,
                             font = style, align = 'center')
                time.sleep(2)
                ans = turtle.textinput('Presione Enter',
                            'Presione Enter para regresar a menú de profesor')
                profesor()
        profesor()
    except:
        turtle.clear()
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write('Hubo un error.', move = False, font = style,
                     align = 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write('Regresando a menú del profesor.', move = False,
                     font = style, align = 'center')
        time.sleep(3)
        profesor()
        
def calificacion_grupo():
    #Esta función se especializa en obtener la calificación promedio
         #de un grupo en particular seleccionado por un profesor.
    global usuario
    turtle.clear()
    try:
        arch_leer = open('Alumnos.txt','r')
        lista = arch_leer.readlines()
        arch_leer.close()
        ans = turtle.textinput('Grupo','Escriba el grupo')
        group = 0
        elementos = 0
        for x in lista:
            nombre_alumno, usuario_alumno, contrasena_alumno, \
            usuario_profesor, grado, grupo, calificacion = x.split(',')
            if usuario.strip() == usuario_profesor.strip():
                if ans.strip() == grupo.strip():
                    group = group + float(calificacion.strip())
                    elementos = elementos + 1
        group = group / elementos
        turtle.clear()
        turtle.color('white')
        turtle.sety(0)
        style = ('Courier', 40, 'italic')
        turtle.write('Profesor', move = False, font = style,
                     align = 'center')
        turtle.sety(-30)
        style = ('Courier', 20, 'italic')
        turtle.write('El grupo', move = False, font = style,
                     align = 'center')
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write(ans, move = False, font = style, align = 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write('tiene una calificación promedio de', move = False,
                     font = style, align = 'center')
        turtle.sety(-120)
        style = ('Courier', 20, 'italic')
        turtle.write(group, move = False, font = style, align = 'center')
        time.sleep(2)
        ans = turtle.textinput('Presione Enter',
                        'Presione Enter para regresar a menú de profesor')
        profesor()
    except:
        turtle.clear()
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write('Hubo un error.', move = False, font = style,
                     align = 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write('Regresando a menú del profesor.', move = False,
                     font = style, align = 'center')
        time.sleep(3)
        profesor()
        
def calificacion_general():
    #Esta función se especializa en obtener la calificación promedio de 
       #todos los alumnos seleccionado por el usuario de un profesor.
    global usuario
    turtle.clear()
    try:
        arch_leer = open('Alumnos.txt','r')
        lista = arch_leer.readlines()
        arch_leer.close()
        group = 0
        elemento = 0
        for x in lista:
            nombre_alumno, usuario_alumno, contrasena_alumno, \
            usuario_profesor, grado, grupo, calificacion = x.split(',')
            if usuario.strip() == usuario_profesor.strip():
                group = group + float(calificacion.strip())
                elemento = elemento + 1
        group = group / elemento
        turtle.clear()
        turtle.color('white')
        turtle.sety(0)
        style = ('Courier', 40, 'italic')
        turtle.write('Profesor', move = False, font = style, align = 'center')
        turtle.sety(-30)
        style = ('Courier', 20, 'italic')
        turtle.write('La calificación general para su usuario', move = False,
                     font = style, align = 'center')
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write(usuario, move = False, font = style, align = 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write(group, move = False, font = style, align = 'center')
        time.sleep(2)
        ans = turtle.textinput('Presione Enter',
                        'Presione Enter para regresar a menú de profesor')
        profesor()
    except:
        turtle.clear()
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write('Hubo un error.', move = False, font = style,
                     align= 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write('Regresando a menú del profesor.', move = False,
                     font = style, align = 'center')
        time.sleep(3)
        profesor()
        
def registro():
    #Esta función se especializa en el registro de un alumno o profesor en
     #los archivos de la aplicación para disfrutar de sus características.
    global userName
    usuarioTomado = 0
    usuarioTomadoP = 0
    turtle.color('white')
    turtle.sety(0)
    style = ('Courier', 40, 'italic')
    turtle.write('Registro', move = False, font = style, align = 'center')
    turtle.sety(-30)
    style = ('Courier', 20, 'italic')
    turtle.write('Sigue las instrucciones y contesta lo que se te indica',
                 move = False, font = style, align = 'center')
    time.sleep(2)
    ans = turtle.textinput('¿Eres alumno o profesor',
                           'Ingrese su respuesta (Alumno/Profesor)')
    ans = ans.lower()
    if ans == 'alumno':
        try:
            profesor = 0
            ans = turtle.textinput('Usuario Profesor',
            'Ingrese el usuario de su profesor (Por ejemplo: @abcdef)')
            archUP = open('Profesores.txt', 'r')
            lista = archUP.readlines()
            archUP.close()
            for x in lista:
                nombreProfesor, usuarioProfesor, \
                                contraseñaProfesor = x.split(',')
                if ans == usuarioProfesor.strip():
                    profesor = 1
                    userProf = ans
            if profesor == 1:
                ans = turtle.textinput('Nombre Alumno',
                'Ingrese su nombre completo respetando mayúsculas y tildes')
                nombreAlumno = ans
                while True:
                    ans = turtle.textinput('Usuario Alumno',
                        'Ingrese su nuevo usuario (Por ejemplo: @abcdef)')
                    archUA = open('Alumnos.txt', 'r')
                    lista2 = archUA.readlines()
                    archUA.close()
                    for c in lista2:
                        na, ua, c, up, grado, grupo, \
                            calificacion = c.split(',')
                        if ua.strip() == ans:
                            usuarioTomado = 1
                    if usuarioTomado == 0:
                        usuarioA = ans
                        break
                    usuarioTomado = 0
                ans = turtle.textinput('Contraseña',
                                       'Ingrese su nueva contraseña')
                contraseña = ans
                ans = turtle.textinput('Grado', 'Ingrese su grado')
                grado = ans
                ans = turtle.textinput('Grupo', 'Ingrese su grupo')
                grupo = ans
                calificacion = '0'
                archAA = open('Alumnos.txt', 'a')
                archAA.write(nombreAlumno + ',' + usuarioA + ',' +
                contraseña + ',' + userProf + ',' + grado + ',' + grupo +
                             ',' + calificacion + '\n')
                archAA.close()
                turtle.sety(-60)
                style = ('Courier', 20, 'italic')
                turtle.write('Cuenta creada satisfactoriamente.',
                             move = False, font = style, align = 'center')
                turtle.sety(-90)
                style = ('Courier', 20, 'italic')
                turtle.write('Regresando a menú.', move = False,
                             font = style, align = 'center')
                time.sleep(3)
                menu()
            else:
                turtle.sety(-60)
                style = ('Courier', 20, 'italic')
                turtle.write('Usuario de profesor no encontrado.',
                             move = False, font = style, align = 'center')
                turtle.sety(-90)
                style = ('Courier', 20, 'italic')
                turtle.write('Regresando a menú.', move = False,
                             font = style, align = 'center')
                time.sleep(3)
                menu()
        except:
            turtle.clear()
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('Hubo un error.', move = False, font = style,
                         align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('Regresando a menú.', move = False, font = style,
                         align = 'center')
            time.sleep(3)
            menu()
    elif ans == 'profesor':
        try:
            ans = turtle.textinput('Nombre Profesor',
                'Ingrese su nombre completo respetando mayúsculas y tildes')
            nombreProfesor = ans
            while True:
                ans = turtle.textinput('Usuario Profesor',
                        'Ingrese su nuevo usuario (Por ejemplo: @abcdef)')
                archUP = open('Profesores.txt', 'r')
                lista4 = archUP.readlines()
                archUP.close()
                for q in lista4:
                    np, up, contra = q.split(',')
                    if up.strip() == ans:
                        usuarioTomado = 1
                if usuarioTomadoP == 0:
                    usuarioP = ans
                    break
                usuarioTomadoP = 0
            ans = turtle.textinput('Contraseña',
                                   'Ingrese su nueva contraseña')
            contraseñaP = ans
            archAP = open('Profesores.txt', 'a')
            archAP.write(nombreProfesor + ',' + usuarioP + ','
                         + contraseñaP + '\n')
            archAP.close()
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('Cuenta creada satisfactoriamente.', move = False,
                         font = style, align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('Regresando a menú.', move = False, font = style,
                         align = 'center')
            time.sleep(3)
            menu()
        except:
            turtle.clear()
            turtle.sety(-60)
            style = ('Courier', 20, 'italic')
            turtle.write('Hubo un error.', move = False, font = style,
                         align = 'center')
            turtle.sety(-90)
            style = ('Courier', 20, 'italic')
            turtle.write('Regresando a menú.', move = False, font = style,
                         align = 'center')
            time.sleep(3)
            menu()
    else:
        turtle.clear()
        turtle.sety(-60)
        style = ('Courier', 20, 'italic')
        turtle.write('Hubo un problema: No se ha seleecionado una \
opción válida.', move = False, font = style, align = 'center')
        turtle.sety(-90)
        style = ('Courier', 20, 'italic')
        turtle.write('Regresando a menú.', move = False, font = style,
                     align = 'center')
        time.sleep(3)
        menu()
        
def acerca():
    #Esta función imprime información de la aplicación si es seleccionada
                         #por el usuario en el menú.
    turtle.clear()
    turtle.color('white')
    turtle.sety(0)
    style = ('Courier', 40, 'italic')
    turtle.write('A cerca de...', move = False, font = style,
                 align = 'center')
    turtle.sety(-30)
    style = ('Courier', 20, 'italic')
    turtle.write('The Ghost es un programa desarrollado por', move = False,
                 font = style, align = 'center')
    turtle.sety(-60)
    style = ('Courier', 20, 'italic')
    turtle.write('Francisco Javier Macías Segura y Juan Luis Flores Sánchez',
                 move = False, font = style, align = 'center')
    turtle.sety(-90)
    style = ('Courier', 20, 'italic')
    turtle.write('con el propósito de fomentar e impulsar la educación, y el \
mejoramiento', move = False, font = style, align = 'center')
    turtle.sety(-120)
    style = ('Courier', 20, 'italic')
    turtle.write('académico mexicano en la prueba PISA.', move = False,
                 font = style, align = 'center')
    time.sleep(5)
    turtle.textinput('Presiona Enter',
            'Presiona Enter para salir de A cerca de... y volver al menú')
    menu()
    
def salir():
    #Esta función presenta una animación para despedir el programa de el
                                    #usuario
    turtle.clear()
    color = ['purple', 'purple', 'purple', 'purple','blue', 'blue', 'blue',
             'blue', 'green', 'green', 'green', 'yellow', 'yellow', 'yellow',
             'orange', 'orange', 'orange', 'red', 'red', 'red']
    turtle.color('white')
    turtle.sety(-130)
    style = ('Courier', 30, 'italic')
    turtle.write('Saliendo...', move = False, font = style, align = 'center')
    indice_color = 0
    turtle.speed(8)
    turtle.home()
    turtle.sety(-40)
    turtle.pendown()
    for a in range (10, 110, 5):
        turtle.pencolor(color[indice_color])
        indice_color = indice_color + 1 
        for i in range (1, 4):
            turtle.forward(a)
            turtle.right(120)
        turtle.right(17)
    time.sleep(2)
    turtle.penup()
    turtle.clear()
    turtle.color('white')
    turtle.sety(-90)
    style = ('Courier', 40, 'italic')
    turtle.write('Vuelva pronto :)', move = False, font = style,
                 align = 'center')
    time.sleep(2)
    turtle.clear()
    turtle.done()
    exit

turtle.title('The Ghost')
turtle.penup()
turtle.hideturtle()
turtle.bgcolor('black')
score = 0
bienvenida()
intro()
turtle.penup()
turtle.setpos(0,0)
turtle.bgpic('TheGhostbg.png')
menu()
turtle.done()
turtle.bye()