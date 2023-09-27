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
bandera_sonido_on = None

variables_iniciales = inicializacion_de_variables()

listas_datos = guardado_en_sublistas(lista)

#tamaño pantalla (weight/height)
screen = pygame.display.set_mode([1200,800]) #se crea la ventana

#titulo ventana
pygame.display.set_caption("Preguntados")

#imágenes
imagenes = renderizar_imagenes()
imagen_sonido = imagenes["sound_img"]
barra_vida = imagenes["barra_vida_llena"]

#icono de preguntados en la ventana
pygame.display.set_icon(imagenes["icon"])

#inicialización de textos
textos = renderizar_textos()

#fuentes
fuentes = renderizar_fuentes()

#música de fondo
volumen = 0.2
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("Desafío preguntados/music/melodyloops-bright-shiny-morning.mp3")
sonido_fondo.set_volume(volumen)
sonido_fondo.play(-1)

#sonidos
sonido_respuesta_incorrecta = pygame.mixer.Sound("Desafío preguntados/music/roblox_death.mp3")
sonido_respuesta_correcta = pygame.mixer.Sound("Desafío preguntados/music/sonic_ring.mp3")
sonido_respuesta_incorrecta.set_volume(volumen)
sonido_respuesta_correcta.set_volume(volumen)
#sonido_respuesta_correcta.play()

#rectangulos
btn_opcion_a = pygame.Rect((70, 50), (60, 60))
btn_opcion_b = pygame.Rect((70, 50), (60, 60))
btn_opcion_c = pygame.Rect((70, 50), (60, 60))

while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #click del botón derecho del mouse
            posicion_click = list(event.pos)
            if btn_para_pregunta.collidepoint(posicion_click) and variables_iniciales["bandera_fin_del_juego"] is False:
                comenzar_juego(variables_iniciales)
                barra_vida = imagenes["barra_vida_llena"]
                if variables_iniciales["primer_inicio_indice"]:
                    variables_iniciales["indice_listas"] = 0
                    variables_iniciales["primer_inicio_indice"] = False
                else:
                    variables_iniciales["indice_listas"] += 1
            if btn_opcion_a.collidepoint(posicion_click) and variables_iniciales["bandera_opcion_a"]:
                variables_iniciales["opcion_elegida"] = "a"
                variables_iniciales["bandera_opcion_a"] = False
            elif btn_opcion_b.collidepoint(posicion_click) and variables_iniciales["bandera_opcion_b"]:
                variables_iniciales["opcion_elegida"] = "b"
                variables_iniciales["bandera_opcion_b"] = False
            elif btn_opcion_c.collidepoint(posicion_click) and variables_iniciales["bandera_opcion_c"]:
                variables_iniciales["opcion_elegida"] = "c"
                variables_iniciales["bandera_opcion_c"] = False

            if btn_para_reiniciar.collidepoint(posicion_click):
                reiniciar_variables(variables_iniciales)
            if btn_sonido.collidepoint(posicion_click):
                if bandera_sonido_on:
                    bandera_sonido_on = False
                else:
                    bandera_sonido_on = True
            if bandera_sonido_on:
                volumen = 0.3
                imagen_sonido = imagenes["sound_img"]
                sonido_fondo.set_volume(volumen)
                
            elif bandera_sonido_on is False:
                volumen = 0
                imagen_sonido = imagenes["sound_img_off"]
                sonido_fondo.set_volume(volumen)

            if variables_iniciales["indice_listas"] < len(listas_datos[0]) and variables_iniciales["bandera_fin_del_juego"] is False:
                text_pregunta = fuentes["fuente_text_pregunta"].render(listas_datos[0][variables_iniciales["indice_listas"]], True, COLOR_NEGRO)
                txt_opcion_a = fuentes["fuente_text_pregunta"].render(listas_datos[1][variables_iniciales["indice_listas"]], True, COLOR_NEGRO)
                txt_opcion_b = fuentes["fuente_text_pregunta"].render(listas_datos[2][variables_iniciales["indice_listas"]], True, COLOR_NEGRO)
                txt_opcion_c = fuentes["fuente_text_pregunta"].render(listas_datos[3][variables_iniciales["indice_listas"]], True, COLOR_NEGRO)
                variables_iniciales["respuesta_correcta"] = listas_datos[4][variables_iniciales["indice_listas"]]
            elif variables_iniciales["indice_listas"] == len(listas_datos[0]) and variables_iniciales["bandera_fin_del_juego"] is False:
                variables_iniciales["bandera_iniciar_preguntas"] = False
                variables_iniciales["bandera_fin_del_juego"] = True
                
            #respuesta correcta
            if variables_iniciales["bandera_iniciar_preguntas"]:
                if variables_iniciales["opcion_elegida"] == variables_iniciales["respuesta_correcta"] and (variables_iniciales["opcion_elegida"] in ("a", "b", "c")) and variables_iniciales["bandera_fin_del_juego"] is False and variables_iniciales["intentos"] != 0:
                    sonido_respuesta_correcta.play()
                    variables_iniciales["bandera_respuesta_correcta"] = True
                    variables_iniciales["bandera_opcion_a"] = False
                    variables_iniciales["bandera_opcion_b"] = False
                    variables_iniciales["bandera_opcion_c"] = False
                    if variables_iniciales["intentos"] == 1:
                        variables_iniciales["puntaje"] = 5
                    elif variables_iniciales["intentos"] == 2:
                        variables_iniciales["puntaje"] = 10
                        barra_vida = imagenes["barra_vida_llena"]
                    variables_iniciales["score"] += variables_iniciales["puntaje"]
                    variables_iniciales["opcion_elegida"] = ""

                #respuesta incorrecta
                elif variables_iniciales["opcion_elegida"] != variables_iniciales["respuesta_correcta"] and (variables_iniciales["opcion_elegida"] in ("a", "b", "c")) and variables_iniciales["bandera_fin_del_juego"] is False and (variables_iniciales["intentos"] in (1,2)):
                    if variables_iniciales["opcion_elegida"] not in variables_iniciales["opciones_seleccionadas"]:
                        variables_iniciales["intentos"] -= 1
                        sonido_respuesta_incorrecta.play()
                        variables_iniciales["opciones_seleccionadas"].append(variables_iniciales["opcion_elegida"])
                        barra_vida = imagenes["barra_vida_mitad"]
                
                #sin intentos
                if variables_iniciales["intentos"] == 0 and (variables_iniciales["opcion_elegida"] in ("a", "b", "c")) and variables_iniciales["bandera_fin_del_juego"] is False:
                    variables_iniciales["puntaje"] = 0
                    variables_iniciales["bandera_sin_intentos"] = True
                    variables_iniciales["bandera_opcion_a"] = False
                    variables_iniciales["bandera_opcion_b"] = False
                    variables_iniciales["bandera_opcion_c"] = False
                    barra_vida = imagenes["barra_vida_vacia"]

    #Renderización de elementos
    screen.blit(imagenes["background"],[0,0])

    img_btn_reiniciar = pygame.transform.scale(imagenes["btn_reiniciar_img"], (400, 75))
    btn_para_reiniciar = pygame.Rect(400, 700, 400, 60)
    screen.blit(img_btn_reiniciar, btn_para_reiniciar)

    img_btn_pregunta = pygame.transform.scale(imagenes["btn_pregunta_img"], (400, 60))
    btn_para_pregunta = pygame.Rect(400, 60, 326, 56)
    screen.blit(img_btn_pregunta, btn_para_pregunta)

    screen.blit(imagenes["logo"], [0,0])

    img_btn_sound = pygame.transform.scale(imagen_sonido, (70,80))
    btn_sonido = pygame.Rect(1095, 30, 100, 100)
    screen.blit(img_btn_sound, btn_sonido)

    if variables_iniciales["bandera_iniciar_preguntas"]:
        text_score = fuentes["fuente_text_score"].render(str(variables_iniciales["score"]),True, COLOR_NEGRO)
        img_barra_vida = pygame.transform.scale(barra_vida, (200,60))
        screen.blit(img_barra_vida, (980,720))
        screen.blit(textos["txt_titulo_score"], (530, 170))
        screen.blit(text_score, (577, 205))
        txt_coordinate_pregunta = text_pregunta.get_rect()
        txt_coordinate_pregunta.center = (screen.get_width() // 2, 300)
        screen.blit(text_pregunta, txt_coordinate_pregunta)
        y_txt_opcion = 460
        y_btn_opcion = 480

        if variables_iniciales["bandera_opcion_a"]:
            ancho_btn = calcular_ancho_btn(txt_opcion_a)
            alto_btn = calcular_alto_btn(txt_opcion_a)
            coordenada_btn = calcular_coordenada_btn(ancho_btn, alto_btn, 200, y_btn_opcion, screen)
            x_texto = coordenada_btn.left + (coordenada_btn.width - txt_opcion_a.get_width()) // 2
            btn_opcion_a = pygame.Rect(x_texto, y_txt_opcion, (ancho_btn), (ancho_btn))
            screen.blit(txt_opcion_a, (x_texto, y_txt_opcion))

        if variables_iniciales["bandera_opcion_b"]:
            ancho_btn = calcular_ancho_btn(txt_opcion_b)
            alto_btn = calcular_alto_btn(txt_opcion_b)
            coordenada_btn = calcular_coordenada_btn(ancho_btn, alto_btn, screen.get_width() // 2, y_btn_opcion, screen)
            x_texto = coordenada_btn.left + (coordenada_btn.width - txt_opcion_b.get_width()) // 2
            btn_opcion_b = pygame.Rect(x_texto, y_txt_opcion, ancho_btn, alto_btn)
            screen.blit(txt_opcion_b, (x_texto, y_txt_opcion))
            
        if variables_iniciales["bandera_opcion_c"]:
            ancho_btn = calcular_ancho_btn(txt_opcion_c)
            alto_btn = calcular_alto_btn(txt_opcion_c)
            coordenada_btn = calcular_coordenada_btn(ancho_btn, calcular_alto_btn(txt_opcion_b), 1000, y_btn_opcion, screen)
            x_texto = coordenada_btn.left + (coordenada_btn.width - txt_opcion_c.get_width()) // 2
            btn_opcion_c = pygame.Rect(x_texto, y_txt_opcion, ancho_btn, alto_btn)
            screen.blit(txt_opcion_c, (x_texto, y_txt_opcion))
        
        if variables_iniciales["bandera_respuesta_correcta"]:
            text_pregunta = textos["txt_respuesta_correcta"]
        elif variables_iniciales["bandera_sin_intentos"]:
            text_pregunta = textos["txt_respuesta_incorrecta"]
            
        
    elif variables_iniciales["bandera_fin_del_juego"]:
        text_pregunta = textos["text_fin_del_juego"]
        txt_coordinate_pregunta = text_pregunta.get_rect()
        txt_coordinate_pregunta.center = (screen.get_width() // 2, 300)
        screen.blit(text_pregunta, txt_coordinate_pregunta)
        screen.blit(textos["text_fin_del_juego2"], (240, 350))


    pygame.display.flip()#muestra cambios en pantalla 
        
    if event.type == pygame.QUIT:
        running = False
    

pygame.quit()


