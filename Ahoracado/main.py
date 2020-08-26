import PySimpleGUI as sg 
import random
from ahorcado import main

intentos = 0
trucos = False
palabra = ''

layout = [[sg.Text("                                   Ahorcado")],
[sg.Text('Trucos')],
[sg.Radio('Si',group_id='trucos'),sg.Radio('No',group_id='trucos')],
[sg.Text('Caategoría')],
[sg.Radio('Deportes',group_id='categoria'),sg.Radio('Animales',group_id='categoria'),sg.Radio('Programación',group_id='categoria'),sg.Radio('Colegio',group_id='categoria')],
[sg.Button('Accept',key='play')]]

deportes = ['futbol','baloncesto','balonmano','atletismo','boxeo','pelota','raqueta','balon','porteria','canasta']
animales = ['perro','gato','hamster','rana','coballa','leopardo','leon','tigre','medusa','girafa','zebra','pajaro']
programacion = ['funcion','variable','string','int','boolean','lista','diccionario','api','print','clase']
colegio = ['silla','mesa','lapiz','boligrafo','libreta','aula','profesor','alumno','pizarra','patio']

window = sg.Window('Ahorcado').layout(layout)
try:
    while True:
        events, values = window.read()
        if events == sg.WIN_CLOSED:
            break
        if events == 'play':
            if values[0]: trucos = True
            if values[2]: palabra = random.choice(deportes)
            if values[3]: palabra = random.choice(animales)
            if values[4]: palabra = random.choice(programacion)
            if values[5]: palabra = random.choice(colegio)
            if palabra != '':
                window.close()
                main(palabra,trucos)
except: pass
