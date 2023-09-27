import pygame
from constantes import *

def inicializacion_de_variables():
    variables_iniciales = {
    "score": 0,
    "bandera_iniciar_preguntas": False,
    "indice_listas": 0,
    "opcion_elegida": "",
    "respuesta_correcta": "",
    "puntaje": 2,
    "intentos": 2,
    "bandera_fin_del_juego": False,
    "bandera_opcion_a": True,
    "bandera_opcion_b": True,
    "bandera_opcion_c": True,
    "primer_inicio_indice": True,
    "bandera_respuesta_correcta": False,
    "bandera_sin_intentos": False,
    "opciones_seleccionadas": [] 
    }

    return variables_iniciales

def guardado_en_sublistas(lista: list):

    lista_preguntas = []
    lista_respuesta_a = []
    lista_respuesta_b = []
    lista_respuesta_c = []
    lista_respuesta_correcta = []
    lista_salida = []

    for e_lista in lista:
        lista_preguntas.append(e_lista["pregunta"])
        lista_respuesta_a.append(e_lista["a"])
        lista_respuesta_b.append(e_lista["b"])
        lista_respuesta_c.append(e_lista["c"])
        lista_respuesta_correcta.append(e_lista["correcta"])

    lista_salida = [lista_preguntas,lista_respuesta_a,lista_respuesta_b,lista_respuesta_c,lista_respuesta_correcta]
    
    return lista_salida

def comenzar_juego(diccionario_variables: dict):
    diccionario_variables["intentos"] = 2
    diccionario_variables["opcion_elegida"] = ""
    diccionario_variables["bandera_opcion_a"] = True
    diccionario_variables["bandera_opcion_b"] = True
    diccionario_variables["bandera_opcion_c"] = True
    diccionario_variables["bandera_iniciar_preguntas"] = True
    diccionario_variables["bandera_fin_del_juego"] = False
    diccionario_variables["bandera_respuesta_correcta"] = False
    diccionario_variables["bandera_sin_intentos"] = False
    diccionario_variables["opciones_seleccionadas"] = []

    return diccionario_variables

def reiniciar_variables(diccionario_variables:dict):
    diccionario_variables["score"] = 0
    diccionario_variables["bandera_iniciar_preguntas"] = False
    diccionario_variables["indice_listas"] = 0
    diccionario_variables["opcion_elegida"] = ""
    diccionario_variables["respuesta_correcta"] = ""
    diccionario_variables["puntaje"] = 0
    diccionario_variables["intentos"] = 2
    diccionario_variables["bandera_fin_del_juego"] = False
    diccionario_variables["bandera_opcion_a"] = True
    diccionario_variables["bandera_opcion_b"] = True
    diccionario_variables["bandera_opcion_c"] = True
    diccionario_variables["primer_inicio_indice"] = True
    diccionario_variables["bandera_respuesta_correcta"] = False
    diccionario_variables["bandera_sin_intentos"] = False
    diccionario_variables["opciones_seleccionadas"] = []

    return diccionario_variables


def renderizar_textos():
    fuentes = renderizar_fuentes()

    textos = {
        "txt_titulo_score": fuentes["fuente_txt_titulo_score"].render("SCORE:", True, COLOR_NEGRO),
        "text_score": fuentes["fuente_text_score"].render("0",True, COLOR_NEGRO),
        "text_pregunta": fuentes["fuente_text_pregunta"].render("", True, COLOR_NEGRO),
        "txt_opcion_a": fuentes["fuente_txt_opcion_a"].render("", True, COLOR_NEGRO),
        "txt_opcion_b": fuentes["fuente_txt_opcion_b"].render("", True, COLOR_NEGRO),
        "txt_opcion_c": fuentes["fuente_txt_opcion_c"].render("", True, COLOR_NEGRO),
        "txt_respuesta_correcta": fuentes["fuente_txt_respuesta_correcta"].render("¡Respuesta correcta!", True, COLOR_NEGRO),
        "txt_respuesta_incorrecta": fuentes["fuente_txt_respuesta_incorrecta"].render("Respuesta incorrecta, no tiene más intentos", True, COLOR_NEGRO),
        "text_fin_del_juego": fuentes["fuente_text_fin_del_juego"].render("¡FIN DEL JUEGO!", True, COLOR_NEGRO),
        "text_fin_del_juego2": fuentes["fuente_text_fin_del_juego2"].render("Si desea volver a jugar, presione 'reiniciar'", True, COLOR_NEGRO)
    }
    
    return textos

def renderizar_fuentes():
    fuente_importada = "Desafío preguntados/fonts/LuckiestGuy.ttf"

    fuentes = {
        "fuente_txt_titulo_score": pygame.font.Font(fuente_importada, 45),
        "fuente_text_score": pygame.font.Font(fuente_importada, 40),
        "fuente_text_pregunta": pygame.font.Font(fuente_importada, 38),
        "fuente_txt_opcion_a": pygame.font.Font(fuente_importada, 30),
        "fuente_txt_opcion_b": pygame.font.Font(fuente_importada, 30),
        "fuente_txt_opcion_c": pygame.font.Font(fuente_importada, 30),
        "fuente_txt_respuesta_incorrecta": pygame.font.Font(fuente_importada, 40),
        "fuente_txt_respuesta_correcta": pygame.font.Font(fuente_importada, 40),
        "fuente_text_fin_del_juego": pygame.font.Font(fuente_importada, 40),
        "fuente_text_fin_del_juego2": pygame.font.Font(fuente_importada, 40)
    }

    return fuentes


def renderizar_imagenes():
    imagenes = {
        "logo": pygame.image.load('Desafío preguntados/img/logo.png').convert(),
        "background": pygame.image.load('Desafío preguntados/img/fondo.png').convert(),
        "icon": pygame.image.load('Desafío preguntados/img/logo.png').convert(),
        "btn_opciones_background": pygame.image.load('Desafío preguntados/img/btn-3d.png').convert(),
        "btn_pregunta_img": pygame.image.load('Desafío preguntados/img/img_pregunta.png').convert(),
        "btn_reiniciar_img": pygame.image.load('Desafío preguntados/img/img_reiniciar.png').convert(),
        "sound_img": pygame.image.load('Desafío preguntados/img/img_sound.png').convert(),
        "sound_img_off": pygame.image.load('Desafío preguntados/img/img_sound_off.png').convert(),
        "barra_vida_llena": pygame.image.load('Desafío preguntados/img/barra_vida_llena.png').convert(),
        "barra_vida_mitad": pygame.image.load('Desafío preguntados/img/barra_vida_mitad.png').convert(),
        "barra_vida_vacia": pygame.image.load('Desafío preguntados/img/barra_vida_vacia.png').convert(),
    }

    #elimina el color de fondo de las imágenes
    imagenes["logo"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["icon"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["btn_opciones_background"].set_colorkey(COLOR_NEGRO)
    imagenes["btn_pregunta_img"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["btn_reiniciar_img"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["sound_img"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["sound_img_off"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["barra_vida_llena"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["barra_vida_mitad"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["barra_vida_vacia"].set_colorkey(COLOR_ROJO_PAINT)
    imagenes["icon"].set_colorkey(COLOR_ROJO_PAINT)

    return imagenes


def calcular_ancho_btn(texto:str):
    padding = 50
    ancho_btn = texto.get_width() + padding
    return ancho_btn
        
def calcular_alto_btn(texto:str):
    padding = 50
    alto_btn = texto.get_height() + padding
    return alto_btn

def calcular_coordenada_btn(ancho_btn, alto_btn, x, y, screen):
    imagen = renderizar_imagenes()
    btn_opcion_a_background = pygame.transform.scale(imagen["btn_opciones_background"], (ancho_btn, alto_btn))
    btn_opcion_a_background_coordinate = btn_opcion_a_background.get_rect()
    btn_opcion_a_background_coordinate.center = (x, y)
    screen.blit(btn_opcion_a_background, btn_opcion_a_background_coordinate)
    return btn_opcion_a_background_coordinate

