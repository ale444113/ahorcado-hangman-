import pygame, random
import PySimpleGUI as sg
def main(palabra,trampas):

    guess = []
    for x in palabra:
        guess.append("_ ")
    if trampas:
        the_letter = random.choice(palabra)
        the_index = palabra.index(the_letter)
        guess[the_index] = the_letter
    palabra = list(palabra)
    palabrasno = []

    pygame.init()
    playing = True

    WITDH, HEIGHT = 800, 400 
    screen = pygame.display.set_mode((WITDH, HEIGHT)) 
    pygame.display.set_caption("Hangman game")
    clock = pygame.time.Clock()

    images = []
    for i in range(7):
        image = pygame.image.load("images/hangman" + str(i) + ".png")
        images.append(image)

    hangman_status = 6
    def hangman(x,y,status):
        screen.blit(images[status], (x,y))
    def main(hangman_status):
        while playing:
            guess_in_str = ' '.join([str(elem) for elem in guess]) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    palabra_en_chr = 97
                    rango_para_esto = 260
                    
                    for x in range(13):
                        if mx in range(rango_para_esto,rango_para_esto+30) and my in range(190,220):
                            palabra_elegida = chr(palabra_en_chr)
                            if palabra_elegida not in palabrasno:
                                if palabra_elegida in palabra:
                                    index_list = [i for i, x in enumerate(palabra) if x == palabra_elegida]
                                    for n in range(len(index_list)):
                                        index = index_list[n]
                                        guess[index] = palabra_elegida+" "
                                    palabrasno.append(palabra_elegida)
                                    if '_ ' not in guess:
                                        return True

                                else:
                                    palabrasno.append(palabra_elegida)
                                    hangman_status-=1
                        palabra_en_chr += 1
                        rango_para_esto += 30

                    palabra_en_chr = 110
                    rango_para_esto = 260

                    for x in range(13):
                        if mx in range(rango_para_esto,rango_para_esto+30) and my in range(260,290):
                            palabra_elegida = chr(palabra_en_chr)
                            if palabra_elegida not in palabrasno:
                                if palabra_elegida in palabra:
                                    index_list = [i for i, x in enumerate(palabra) if x == palabra_elegida]
                                    for n in range(len(index_list)):
                                        index = index_list[n]
                                        guess[index] = palabra_elegida+" "
                                    palabrasno.append(palabra_elegida)
                                    if '_ ' not in guess:
                                        pygame.quit()
                                        return True
                                else:
                                    palabrasno.append(palabra_elegida)
                                    hangman_status-=1
                        palabra_en_chr += 1
                        rango_para_esto += 30

                    if hangman_status == 0:
                        pygame.quit()
                        return False
            screen.fill((255,255,255))
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render(guess_in_str, False, (0, 0, 0))
            screen.blit(textsurface,(372, 56))
            dibujarx, dibujary = 260, 190
            for x in range(97,110):
                if chr(x) not in palabrasno:
                    textsurface = myfont.render(chr(x), False, (0, 0, 0))
                    screen.blit(textsurface,(dibujarx, dibujary))
                    dibujarx += 30
                    
                else:
                    textsurface = myfont.render('', False, (0, 0, 0))
                    screen.blit(textsurface,(dibujarx, dibujary))
                    dibujarx += 30
            dibujarx, dibujary = 260, 260
            for x in range(110,123):
                if chr(x) not in palabrasno:
                    textsurface = myfont.render(chr(x), False, (0, 0, 0))
                    screen.blit(textsurface,(dibujarx, dibujary))
                    dibujarx += 30
                else:
                    textsurface = myfont.render('', False, (0, 0, 0))
                    screen.blit(textsurface,(dibujarx, dibujary))
                    dibujarx += 30
            hangman(40,30,hangman_status)
            pygame.display.update()
            clock.tick(60)
            


    try: 
        win = main(hangman_status)
        if win == False:
            palabra_in_str = ''.join([str(elem) for elem in palabra])
            layout = [[sg.Text('Perdiste :c')],
            [sg.Text(f'La palabra era: {palabra_in_str}')],
            [sg.Button('Aceptar',key='aceptar')]]
            ventanita = sg.Window('Perdiste :((').Layout(layout)
            while True:
                event, values = ventanita.read()
                if event == 'aceptar' or event == sg.WIN_CLOSED:
                    break
        elif win == True:
            layout = [[sg.Text('GANASTE!')],
            [sg.Button('Aceptar',key='aceptar')]]
            ventanita = sg.Window('Ganaste').Layout(layout)
            while True:
                event, values = ventanita.read()
                if event == 'aceptar' or event == sg.WIN_CLOSED:
                    break
            
    except: pass