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
btn_pregunta_img = pygame.image.load("Desafío preguntados/img/pregunta fuente img.png").convert()

#elimina el color negro de la imagen PNG
logo.set_colorkey([0, 0, 0])
icon.set_colorkey([0, 0, 0])
btn_opciones_background.set_colorkey([0, 0, 0])
btn_pregunta_img.set_colorkey((237, 28, 36))

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

text_btn_reiniciar = text_desing(font_desing("ka1.ttf", 50), "Reiniciar", COLOR_NEGRO)
text_title_score = text_desing(font_desing("ka1.ttf", 40), "SCORE:", COLOR_NEGRO)
text_score = text_desing(font_desing("ka1.ttf", 40), str(score), COLOR_NEGRO)
text_empty = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), "", COLOR_NEGRO)
text_pregunta = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "", COLOR_NEGRO)
txt_opcion_a = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), "", COLOR_NEGRO)
txt_opcion_b = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), "", COLOR_NEGRO)
txt_opcion_c = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), "", COLOR_NEGRO)
text_respuesta_correcta = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "¡Respuesta correcta!", COLOR_NEGRO)
text_respuesta_incorrecta = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "Respuesta incorrecta, no tiene más intentos", COLOR_NEGRO)
text_fin_del_juego = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "¡FIN DEL JUEGO!", COLOR_NEGRO)
text_fin_del_juego2 = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "Si desea volver a jugar, presione 'reiniciar'", COLOR_NEGRO)


#música de fondo
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("Desafío preguntados/music/melodyloops-bright-shiny-morning.mp3")
sonido_fondo.set_volume(0.0)
sonido_fondo.play()


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
            print("no entró a preguntas")
            if btn_para_pregunta.collidepoint(posicion_click):
                print("Entró a pregunta")
                intentos = 2
                opcion_elegida = ""
                bandera_opcion_a = True
                bandera_opcion_b = True
                bandera_opcion_c = True
                bandera_iniciar_preguntas = True
                bandera_fin_del_juego = False
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
                
            if indice_listas < len(lista_preguntas):
                text_pregunta = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), lista_preguntas[indice_listas], COLOR_NEGRO)
                txt_opcion_a = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), lista_respuesta_a[indice_listas], COLOR_NEGRO)
                txt_opcion_b = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), lista_respuesta_b[indice_listas], COLOR_NEGRO)
                txt_opcion_c = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), lista_respuesta_c[indice_listas], COLOR_NEGRO)
                respuesta_correcta = lista_respuesta_correcta[indice_listas]

            if indice_listas == len(lista_preguntas) and bandera_fin_del_juego is False:
                bandera_iniciar_preguntas = False
                bandera_fin_del_juego = True
                
            #respuesta correcta
            if bandera_iniciar_preguntas:
                if opcion_elegida == respuesta_correcta and (opcion_elegida in ("a", "b", "c")) and bandera_fin_del_juego is False and intentos != 0:
                    text_pregunta = text_respuesta_correcta
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
                    intentos -= 1

                #sin intentos
                if intentos == 0 and (opcion_elegida in ("a", "b", "c")) and bandera_fin_del_juego is False:
                    puntaje = 0
                    text_pregunta = text_respuesta_incorrecta
                    bandera_opcion_a = False
                    bandera_opcion_b = False
                    bandera_opcion_c = False

    #Renderización de elementos
    screen.blit(background,[0,0])
    btn_para_reiniciar = pygame.Rect(500, 700, 400, 60)
    img_btn_pregunta = pygame.transform.scale(btn_pregunta_img, (400, 60))
    btn_para_pregunta = pygame.Rect(400, 60, 326, 56)
    screen.blit(img_btn_pregunta, btn_para_pregunta)

    pygame.draw.rect(screen, (COLOR_NEGRO), fondo_ojos_logo, 0)
    screen.blit(logo, [0,0])
    btn_para_reiniciar = screen.blit(text_btn_reiniciar, btn_para_reiniciar)

    if bandera_iniciar_preguntas:
        text_score = text_desing(font_desing("ka1.ttf", 40), str(score), COLOR_NEGRO)
        screen.blit(text_title_score, (540, 170))
        screen.blit(text_score, (595, 205))
        txt_coordinate_pregunta = text_pregunta.get_rect()
        txt_coordinate_pregunta.center = (screen.get_width() // 2, 300)
        screen.blit(text_pregunta, txt_coordinate_pregunta)
        coordenadas_x_opcion_b = screen.get_width() // 2
        coordenadas_x_opcion_a = (screen.get_width() - coordenadas_x_opcion_b) // 2
        coordenadas_x_opcion_c = (screen.get_width() + coordenadas_x_opcion_b) // 2
        coordenadas_y_opciones = 450

        if bandera_opcion_a:
            btn_opcion_a = pygame.Rect(coordenadas_x_opcion_a, coordenadas_y_opciones, (txt_opcion_a.get_width()+50), (txt_opcion_a.get_height()+15))
            btn_opcion_a_background = pygame.transform.scale(btn_opciones_background, (txt_opcion_a.get_width()+50, txt_opcion_a.get_height()+15))
            screen.blit(btn_opcion_a_background, btn_opcion_a)
            x_texto = btn_opcion_a.left + (btn_opcion_a.width - txt_opcion_a.get_width()) // 2
            y_texto = btn_opcion_a.top + (btn_opcion_a.height - txt_opcion_a.get_height()) // 2
            screen.blit(txt_opcion_a, (x_texto, y_texto))

        if bandera_opcion_b:
            btn_opcion_b = pygame.Rect(coordenadas_x_opcion_b, coordenadas_y_opciones, (txt_opcion_b.get_width()+50), (txt_opcion_b.get_height()+15))
            btn_opcion_b_background = pygame.transform.scale(btn_opciones_background, (txt_opcion_b.get_width()+50, txt_opcion_b.get_height()+15))
            screen.blit(btn_opcion_b_background, btn_opcion_b)
            x_texto = btn_opcion_b.left + (btn_opcion_b.width - txt_opcion_b.get_width()) // 2
            y_texto = btn_opcion_b.top + (btn_opcion_b.height - txt_opcion_b.get_height()) // 2
            screen.blit(txt_opcion_b, (x_texto, y_texto))
            
        if bandera_opcion_c:
            btn_opcion_c = pygame.Rect(coordenadas_x_opcion_c, coordenadas_y_opciones, (txt_opcion_c.get_width()+50), (txt_opcion_c.get_height()+15))
            btn_opcion_c_background = pygame.transform.scale(btn_opciones_background, (txt_opcion_c.get_width()+50, txt_opcion_c.get_height()+15))
            screen.blit(btn_opcion_c_background, btn_opcion_c)
            x_texto = btn_opcion_c.left + (btn_opcion_c.width - txt_opcion_c.get_width()) // 2
            y_texto = btn_opcion_c.top + (btn_opcion_c.height - txt_opcion_c.get_height()) // 2
            screen.blit(txt_opcion_c, (x_texto, y_texto))
        
    if bandera_fin_del_juego:
        text_pregunta = text_fin_del_juego
        txt_coordinate_pregunta = text_pregunta.get_rect()
        txt_coordinate_pregunta.center = (screen.get_width() // 2, 300)
        screen.blit(text_pregunta, txt_coordinate_pregunta)
        screen.blit(text_fin_del_juego2, (300, 350))


    pygame.display.flip()#muestra cambios en pantalla 
        
    if event.type == pygame.QUIT:
        running = False
    

pygame.quit()


