from constantes import *
import pygame
from functions import *
from data import lista
from colores import *

""" Añadir música cuando la opción es correcta e incorrecta """

#inicia pygame
pygame.init()

#Inicialización de variables y banderas
running = True
score = 0
bandera_iniciar_preguntas = False
indice_listas = 0
opcion_elegida = ""
respuesta_correcta = ""
puntaje = 0
intentos = 0
bandera_fin_del_juego = False
bandera_opcion_a = True
bandera_opcion_b = True
bandera_opcion_c = True
primer_inicio_indice = True
bandera_sonido_on = ""
bandera_respuesta_correcta = False
bandera_respuesta_incorrecta = False
bandera_sin_intentos = False
opciones_seleccionadas = []


#Listas vacías para recibir los datos de la data
lista_preguntas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []
lista_respuesta_correcta = []

#guardado de datos en las sub-listas
for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])
    lista_respuesta_correcta.append(e_lista["correcta"])


#tamaño pantalla (weight/height)
screen = pygame.display.set_mode([1200,800]) #se crea la ventana

#titulo ventana
pygame.display.set_caption("Preguntados")

#imágenes
logo = pygame.image.load("Desafío preguntados/img/logo.png").convert()
background = pygame.image.load("Desafío preguntados/img/fondo.png").convert()
icon = pygame.image.load("Desafío preguntados/img/logo.png").convert()
btn_opciones_background = pygame.image.load("Desafío preguntados/img/btn-3d.png").convert()
btn_pregunta_img = pygame.image.load("Desafío preguntados/img/img_pregunta.png").convert()
btn_reiniciar_img = pygame.image.load("Desafío preguntados/img/img_reiniciar.png").convert()
sound_img = pygame.image.load("Desafío preguntados/img/img_sound.png").convert()
sound_img_off = pygame.image.load("Desafío preguntados/img/img_sound_off.png").convert()
imagen_sonido = sound_img
#elimina el color de fondo de las imágenes
logo.set_colorkey(COLOR_NEGRO)
icon.set_colorkey(COLOR_NEGRO)
btn_opciones_background.set_colorkey(COLOR_NEGRO)
btn_pregunta_img.set_colorkey((237, 28, 36))
btn_reiniciar_img.set_colorkey((237, 28, 36))
sound_img.set_colorkey((237, 28, 36))
sound_img_off.set_colorkey((237, 28, 36))

#icono de preguntados en la ventana
pygame.display.set_icon(icon)

#función que devuelve el diseño de la fuente
def font_desing(font:str, size:int):
    """
    Recibe como parámetro el str de la fuente(tiene que ser importada) y el int del tamaño de fuente(50).
    """
    font_directory = "Desafío preguntados/fonts/"
    font = pygame.font.Font(font_directory + font, size)
    return font


#función que devuelve el diseño del texto
def text_desing(design, text:str, color:tuple):
    text = design.render(text, True,(color))
    return text

text_title_score = text_desing(font_desing("LuckiestGuy.ttf", 45), "SCORE:", COLOR_NEGRO)
text_score = text_desing(font_desing("LuckiestGuy.ttf", 40), str(score), COLOR_NEGRO)
text_empty = text_desing(font_desing("LuckiestGuy.ttf", 30), "", COLOR_NEGRO)
text_pregunta = text_desing(font_desing("LuckiestGuy.ttf", 40), "", COLOR_NEGRO)
txt_opcion_a = text_desing(font_desing("LuckiestGuy.ttf", 50), "", COLOR_NEGRO)
txt_opcion_b = text_desing(font_desing("LuckiestGuy.ttf", 30), "", COLOR_NEGRO)
txt_opcion_c = text_desing(font_desing("LuckiestGuy.ttf", 30), "", COLOR_NEGRO)
text_respuesta_correcta = text_desing(font_desing("LuckiestGuy.ttf", 40), "¡Respuesta correcta!", COLOR_NEGRO)
text_respuesta_incorrecta = text_desing(font_desing("LuckiestGuy.ttf", 40), "Respuesta incorrecta, no tiene más intentos", COLOR_NEGRO)
text_fin_del_juego = text_desing(font_desing("LuckiestGuy.ttf", 40), "¡FIN DEL JUEGO!", COLOR_NEGRO)
text_fin_del_juego2 = text_desing(font_desing("LuckiestGuy.ttf", 40), "Si desea volver a jugar, presione 'reiniciar'", COLOR_NEGRO)


#música de fondo
volumen = 0.2
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("Desafío preguntados/music/melodyloops-bright-shiny-morning.mp3")
sonido_fondo.set_volume(volumen)
sonido_fondo.play()

#sonidos
sonido_respuesta_incorrecta = pygame.mixer.Sound("Desafío preguntados/music/roblox_death.mp3")
sonido_respuesta_correcta = pygame.mixer.Sound("Desafío preguntados/music/sonic_ring.mp3")
sonido_respuesta_incorrecta.set_volume(volumen)
sonido_respuesta_correcta.set_volume(volumen)
#sonido_respuesta_correcta.play()


#rectangulos
fondo_ojos_logo = pygame.Rect((70, 50), (60, 60))
btn_opcion_a = pygame.Rect((70, 50), (60, 60))
btn_opcion_b = pygame.Rect((70, 50), (60, 60))
btn_opcion_c = pygame.Rect((70, 50), (60, 60))


while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #click del botón derecho del mouse
            posicion_click = list(event.pos)
            print(intentos)
            print(opcion_elegida)
            if btn_para_pregunta.collidepoint(posicion_click) and bandera_fin_del_juego is False:
                intentos = 2
                opcion_elegida = ""
                bandera_opcion_a = True
                bandera_opcion_b = True
                bandera_opcion_c = True
                bandera_iniciar_preguntas = True
                bandera_fin_del_juego = False
                bandera_respuesta_correcta = False
                bandera_sin_intentos = False
                opciones_seleccionadas.clear()
                if primer_inicio_indice:
                    indice_listas = 0
                    primer_inicio_indice = False
                else:
                    indice_listas += 1
            if btn_opcion_a.collidepoint(posicion_click) and bandera_opcion_a:
                opcion_elegida = "a"
                bandera_opcion_a = False
            if btn_opcion_b.collidepoint(posicion_click) and bandera_opcion_b:
                opcion_elegida = "b"
                bandera_opcion_b = False
            if btn_opcion_c.collidepoint(posicion_click) and bandera_opcion_c:
                opcion_elegida = "c"
                bandera_opcion_c = False

            if btn_para_reiniciar.collidepoint(posicion_click):
                score = 0
                bandera_iniciar_preguntas = False
                indice_listas = 0
                opcion_elegida = ""
                respuesta_correcta = ""
                puntaje = 0
                intentos = 0
                bandera_fin_del_juego = False
                bandera_opcion_a = True
                bandera_opcion_b = True
                bandera_opcion_c = True
                primer_inicio_indice = True
            if btn_sonido.collidepoint(posicion_click):
                if bandera_sonido_on:
                    bandera_sonido_on = False
                else:
                    bandera_sonido_on = True
            if bandera_sonido_on:
                volumen = 0.3
                imagen_sonido = sound_img
                sonido_fondo.set_volume(volumen)
                
            elif bandera_sonido_on is False:
                volumen = 0
                imagen_sonido = sound_img_off
                sonido_fondo.set_volume(volumen)

            if indice_listas < len(lista_preguntas) and bandera_fin_del_juego is False:
                text_pregunta = text_desing(font_desing("LuckiestGuy.ttf", 38), lista_preguntas[indice_listas], COLOR_NEGRO)
                txt_opcion_a = text_desing(font_desing("LuckiestGuy.ttf", 30), lista_respuesta_a[indice_listas], COLOR_NEGRO)
                txt_opcion_b = text_desing(font_desing("LuckiestGuy.ttf", 30), lista_respuesta_b[indice_listas], COLOR_NEGRO)
                txt_opcion_c = text_desing(font_desing("LuckiestGuy.ttf", 30), lista_respuesta_c[indice_listas], COLOR_NEGRO)
                respuesta_correcta = lista_respuesta_correcta[indice_listas]
            elif indice_listas == len(lista_preguntas) and bandera_fin_del_juego is False:
                bandera_iniciar_preguntas = False
                bandera_fin_del_juego = True
                
            #respuesta correcta
            if bandera_iniciar_preguntas:
                if opcion_elegida == respuesta_correcta and (opcion_elegida in ("a", "b", "c")) and bandera_fin_del_juego is False and intentos != 0:
                    sonido_respuesta_correcta.play()
                    bandera_respuesta_correcta = True
                    bandera_opcion_a = False
                    bandera_opcion_b = False
                    bandera_opcion_c = False
                    if intentos == 1:
                        puntaje = 5
                    elif intentos == 2:
                        puntaje = 10
                    score += puntaje
                    opcion_elegida = ""

                #respuesta incorrecta
                elif opcion_elegida != respuesta_correcta and (opcion_elegida in ("a", "b", "c")) and bandera_fin_del_juego is False and (intentos in (1,2)):
                    if opcion_elegida not in opciones_seleccionadas:
                        intentos -= 1
                        sonido_respuesta_incorrecta.play()
                        opciones_seleccionadas.append(opcion_elegida)
                

                #sin intentos
                if intentos == 0 and (opcion_elegida in ("a", "b", "c")) and bandera_fin_del_juego is False:
                    puntaje = 0
                    bandera_sin_intentos = True
                    bandera_opcion_a = False
                    bandera_opcion_b = False
                    bandera_opcion_c = False

    #Renderización de elementos
    screen.blit(background,[0,0])

    img_btn_reiniciar = pygame.transform.scale(btn_reiniciar_img, (400, 75))
    btn_para_reiniciar = pygame.Rect(400, 700, 400, 60)
    screen.blit(img_btn_reiniciar, btn_para_reiniciar)

    img_btn_pregunta = pygame.transform.scale(btn_pregunta_img, (400, 60))
    btn_para_pregunta = pygame.Rect(400, 60, 326, 56)
    screen.blit(img_btn_pregunta, btn_para_pregunta)

    pygame.draw.rect(screen, (COLOR_NEGRO), fondo_ojos_logo, 0)
    screen.blit(logo, [0,0])

    img_btn_sound = pygame.transform.scale(imagen_sonido, (70,80))
    btn_sonido = pygame.Rect(1095, 30, 100, 100)
    screen.blit(img_btn_sound, btn_sonido)

    if bandera_iniciar_preguntas:
        text_score = text_desing(font_desing("LuckiestGuy.ttf", 40), str(score), COLOR_NEGRO)
        screen.blit(text_title_score, (530, 170))
        screen.blit(text_score, (577, 205))
        txt_coordinate_pregunta = text_pregunta.get_rect()
        txt_coordinate_pregunta.center = (screen.get_width() // 2, 300)
        screen.blit(text_pregunta, txt_coordinate_pregunta)
        y_texto = 460

        if bandera_opcion_a:
            btn_opcion_a_background = pygame.transform.scale(btn_opciones_background, (txt_opcion_a.get_width()+50, txt_opcion_a.get_height()+50))
            btn_opcion_a_background_coordinate = btn_opcion_a_background.get_rect()
            btn_opcion_a_background_coordinate.center = (200, 480)
            screen.blit(btn_opcion_a_background, btn_opcion_a_background_coordinate)
            x_texto = btn_opcion_a_background_coordinate.left + (btn_opcion_a_background_coordinate.width - txt_opcion_a.get_width()) // 2
            btn_opcion_a = pygame.Rect( x_texto, y_texto, (txt_opcion_a.get_width()+50), (txt_opcion_a.get_height()+15))
            screen.blit(txt_opcion_a, (x_texto, y_texto))

        if bandera_opcion_b:
            btn_opcion_b_background = pygame.transform.scale(btn_opciones_background, (txt_opcion_b.get_width()+50, txt_opcion_b.get_height()+50))
            btn_opcion_b_background_coordinate = btn_opcion_b_background.get_rect()
            btn_opcion_b_background_coordinate.center = (screen.get_width() // 2, 480)
            screen.blit(btn_opcion_b_background, btn_opcion_b_background_coordinate)
            x_texto = btn_opcion_b_background_coordinate.left + (btn_opcion_b_background_coordinate.width - txt_opcion_b.get_width()) // 2
            btn_opcion_b = pygame.Rect(x_texto, y_texto, (txt_opcion_b.get_width()+50), (txt_opcion_b.get_height()+15))
            screen.blit(txt_opcion_b, (x_texto, y_texto))
            
        if bandera_opcion_c:
            btn_opcion_c_background = pygame.transform.scale(btn_opciones_background, (txt_opcion_c.get_width()+50, txt_opcion_c.get_height()+50))
            btn_opcion_c_background_coordinate = btn_opcion_c_background.get_rect()
            btn_opcion_c_background_coordinate.center = (1000, 480)
            screen.blit(btn_opcion_c_background, btn_opcion_c_background_coordinate)
            x_texto = btn_opcion_c_background_coordinate.left + (btn_opcion_c_background_coordinate.width - txt_opcion_c.get_width()) // 2
            btn_opcion_c = pygame.Rect(x_texto, y_texto, (txt_opcion_c.get_width()+50), (txt_opcion_c.get_height()+15))
            screen.blit(txt_opcion_c, (x_texto, y_texto))
        
        if bandera_respuesta_correcta:
            text_pregunta = text_respuesta_correcta
        elif bandera_sin_intentos:
            text_pregunta = text_respuesta_incorrecta
            
        
    elif bandera_fin_del_juego:
        text_pregunta = text_fin_del_juego
        txt_coordinate_pregunta = text_pregunta.get_rect()
        txt_coordinate_pregunta.center = (screen.get_width() // 2, 300)
        screen.blit(text_pregunta, txt_coordinate_pregunta)
        screen.blit(text_fin_del_juego2, (240, 350))


    pygame.display.flip()#muestra cambios en pantalla 
        
    if event.type == pygame.QUIT:
        running = False
    

pygame.quit()


