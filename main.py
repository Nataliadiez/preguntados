from constantes import *
import pygame
from functions import *
from data import lista

#inicia pygame
pygame.init()

#Inicialización de variables y banderas
running = True
score = 0
bandera_iniciar_preguntas = False
recorrido = 0
opcion_elegida = ""
respuesta_correcta = ""
puntaje = 0
intentos = 2
bandera_fin_del_juego = False

#guardo en listas la data
lista_preguntas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []
lista_respuesta_correcta = []

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

#logo preguntados
logo = pygame.image.load("Desafío preguntados/img/logo.png").convert()
#elimina el color negro de la imagen
logo.set_colorkey([0, 0, 0])

#función que devuelve el diseño de la fuente
def font_desing(font:str, size:int):
    """
    Recibe como parámetro el str de la fuente(tiene que ser importada) y el int del tamaño de fuente(50).
    """
    font_directory = "Desafío preguntados/fonts/"
    font = pygame.font.Font(font_directory+font, size)
    return font


#función que devuelve el diseño del texto
def text_desing(design, text:str, color:tuple):
    text = design.render(text, True,(color))
    return text

text_btn_pregunta = text_desing(font_desing("outline_pixel-7.ttf", 50), "Pregunta", COLOR_BLANCO)
text_btn_reiniciar = text_desing(font_desing("outline_pixel-7.ttf", 40), "Reiniciar", COLOR_BLANCO)
text_title_score = text_desing(font_desing("outline_pixel-7.ttf", 40), "SCORE:", COLOR_BLANCO)
text_score = text_desing(font_desing("outline_pixel-7.ttf", 40), str(score), COLOR_BLANCO)
text_empty = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), "", COLOR_BLANCO)
text_pregunta = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "", COLOR_BLANCO)
text_opcion1 = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), "", COLOR_BLANCO)
text_opcion2 = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), "", COLOR_BLANCO)
text_opcion3 = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), "", COLOR_BLANCO)
text_respuesta_correcta = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "¡Respuesta correcta!", COLOR_BLANCO)
text_respuesta_incorrecta = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "Respuesta incorrecta, no tiene más intentos", COLOR_BLANCO)
text_fin_del_juego = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), "¡FIN DEL JUEGO!\nSi desea volver a jugar, presione 'reiniciar'", COLOR_BLANCO)


#música de fondo
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("Desafío preguntados/music/melodyloops-bright-shiny-morning.mp3")
sonido_fondo.set_volume(0.0)
sonido_fondo.play()

#rectangulos
fondo_ojos_logo = pygame.Rect((70, 50), (60, 60))
btn_reiniciar = pygame.Rect((490, 696),(250, 50))
btn_pregunta = pygame.Rect((475, 78),(270, 50))



while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#click del botón derecho del mouse
            posicion_click = list(event.pos)
            boton_pregunta = (posicion_click[0] > 479 and posicion_click[0] < 743) and (posicion_click[1] > 79 and posicion_click[1] < 125)
            boton_reiniciar = (posicion_click[0] > 491 and posicion_click[0] < 738) and (posicion_click[1] > 697 and posicion_click[1] < 744)
            boton_opcion_a = (posicion_click[0] > 156 and posicion_click[0] < 343) and (posicion_click[1] > 422 and posicion_click[1] < 485)
            boton_opcion_b = (posicion_click[0] > 516 and posicion_click[0] < 697) and (posicion_click[1] > 422 and posicion_click[1] < 485)
            boton_opcion_c = (posicion_click[0] > 867 and posicion_click[0] < 1076) and (posicion_click[1] > 417 and posicion_click[1] < 485)
            print(posicion_click)
            if boton_pregunta:
                bandera_iniciar_preguntas = True
                bandera_fin_del_juego = False
                intentos = 2
                if recorrido < len(lista_preguntas):
                    print(intentos)
                    text_pregunta = text_desing(font_desing("TitilliumWeb-Light.ttf", 40), lista_preguntas[recorrido], COLOR_BLANCO)
                    text_opcion1 = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), lista_respuesta_a[recorrido], COLOR_BLANCO)
                    text_opcion2 = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), lista_respuesta_b[recorrido], COLOR_BLANCO)
                    text_opcion3 = text_desing(font_desing("TitilliumWeb-Light.ttf", 30), lista_respuesta_c[recorrido], COLOR_BLANCO)
                    respuesta_correcta = lista_respuesta_correcta[recorrido]
                    text_coordinates = text_pregunta.get_rect()
                    text_coordinates.center = (screen.get_width() // 2, 650 // 2)

                    text_coordinate_opciona = text_opcion1.get_rect()
                    text_coordinate_opciona.center = (500 // 2, 900 // 2)

                    text_coordinate_opcionb = text_opcion2.get_rect()
                    text_coordinate_opcionb.center = (screen.get_width() // 2, 900 // 2)

                    text_coordinate_opcionc = text_opcion3.get_rect()
                    text_coordinate_opcionc.center = (1950 // 2, 900 // 2)

                    score += puntaje
                    text_score = text_desing(font_desing("outline_pixel-7.ttf", 40), str(score), COLOR_BLANCO)
                if recorrido < len(lista_preguntas) and bandera_iniciar_preguntas:
                    recorrido += 1

                elif recorrido == len(lista_preguntas) and bandera_fin_del_juego is False:
                    text_opcion1 = text_empty
                    text_opcion2 = text_empty
                    text_opcion3 = text_empty
                    bandera_fin_del_juego = True
                else:
                    pass


            if boton_opcion_a:
                opcion_elegida = "a"
            elif boton_opcion_b:
                opcion_elegida = "b"
            elif boton_opcion_c:
                opcion_elegida = "c"
                
            if opcion_elegida == respuesta_correcta and (boton_opcion_a or boton_opcion_b or boton_opcion_c) and bandera_fin_del_juego is False:
                print("respuesta correcta")
                text_opcion1 = text_empty
                text_opcion2 = text_empty
                text_opcion3 = text_empty
                text_pregunta = text_respuesta_correcta
                text_coordinates = text_pregunta.get_rect()
                text_coordinates.center = (screen.get_width() // 2, 650 // 2)
                if intentos == 1:
                    puntaje = 5
                elif intentos == 2:
                    puntaje = 10

            elif opcion_elegida != respuesta_correcta and (boton_opcion_a or boton_opcion_b or boton_opcion_c) and bandera_fin_del_juego is False:
                if boton_opcion_a:
                    text_opcion1 = text_empty
                elif boton_opcion_b:
                    text_opcion2 = text_empty
                elif boton_opcion_c:  
                    text_opcion3 = text_empty
                intentos -= 1
                puntaje = 5
                print("respuesta incorrecta")
                
            if intentos == 0 and (boton_opcion_a or boton_opcion_b or boton_opcion_c):
                print("respuesta incorrecta, sin intentos")
                puntaje = 0
                text_opcion1 = text_empty
                text_opcion2 = text_empty
                text_opcion3 = text_empty
                text_pregunta = text_respuesta_incorrecta
                text_coordinates = text_pregunta.get_rect()
                text_coordinates.center = (screen.get_width() // 2, 650 // 2)
            
            if boton_reiniciar:
                text_opcion1 = text_empty
                text_opcion2 = text_empty
                text_opcion3 = text_empty
                text_pregunta = text_empty
                recorrido = 0
                score = 0
                text_score = text_desing(font_desing("outline_pixel-7.ttf", 40), str(score), COLOR_BLANCO)
                opcion_elegida = ""
                respuesta_correcta = ""
                puntaje = 0
                intentos = 2
                bandera_fin_del_juego = False
            

    screen.fill(COLOR_AZUL)
    pygame.draw.rect(screen, (COLOR_AZUL_REAL), btn_reiniciar, 0)
    pygame.draw.rect(screen, (COLOR_AZUL_REAL), btn_pregunta, 0)
    pygame.draw.rect(screen, (COLOR_NEGRO), fondo_ojos_logo, 0)
    screen.blit(text_btn_reiniciar, (500, 700))
    screen.blit(logo,[0,0])
    screen.blit(text_btn_pregunta, (480, 80))
    screen.blit(text_title_score, (540, 170))
    screen.blit(text_score, (595, 200))
        
    if bandera_iniciar_preguntas:
        screen.blit(text_pregunta, text_coordinates)
        screen.blit(text_opcion1, text_coordinate_opciona)
        screen.blit(text_opcion2, text_coordinate_opcionb)
        screen.blit(text_opcion3, text_coordinate_opcionc)
    if bandera_fin_del_juego:
        text_pregunta = text_fin_del_juego
        text_coordinates = text_pregunta.get_rect()
        text_coordinates.center = (screen.get_width() // 2, 650 // 2)
        screen.blit(text_pregunta, text_coordinates)
        screen.blit(text_opcion1, (0, 0))
        screen.blit(text_opcion2, (0, 0))
        screen.blit(text_opcion3, (0, 0))

    pygame.display.flip()#muestra cambios en pantalla 
        
    if event.type == pygame.QUIT:
        running = False
    

pygame.quit()


