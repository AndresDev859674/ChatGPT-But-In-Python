import random
from colorama import init, Fore, Style
import time

# Inicializar colorama
init()

# Mensaje de bienvenida en color rainbow
mensaje_bienvenida = "¡Hola! ¿En qué puedo ayudarte hoy?"
colores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

for letra, color in zip(mensaje_bienvenida, colores * (len(mensaje_bienvenida) // len(colores) + 1)):
    print(color + letra, end='', flush=True)
    time.sleep(0.1)  # Pausa breve para efecto de animación
print(Style.RESET_ALL)  # Reiniciar color después del mensaje

# Respuestas predeterminadas
RESPUESTAS = [
    "¡Hola!",
    "¡Hola! ¿Cómo estás?",
    "¡Estoy bien, gracias! ¿Y tú?",
    "¡Sí, sé Python! ¿En qué puedo ayudarte?",
    "¡Sí, conozco Minecraft!",
    "¡Sí, conozco Roblox!",
    "¡Sí, MrBeast es un famoso creador de contenido en YouTube!",
    "Transformers es una franquicia de medios que gira en torno a robots transformables.",
    "Harry Potter es una serie de novelas escritas por J.K. Rowling.",
    "Minecraft es un juego de construcción y aventuras muy popular.",
]

# Palabras clave y respuestas asociadas
PALABRAS_CLAVE = {
    "hola": ["¡Hola!"],
    "cómo estás": ["¡Hola! ¿Cómo estás?", "¡Estoy bien, gracias! ¿Y tú?"],
    "sabes python": ["¡Sí, sé Python! ¿En qué puedo ayudarte?"],
    "sabes minecraft": ["¡Sí, conozco Minecraft!"],
    "sabes roblox": ["¡Sí, conozco Roblox!"],
    "quién es mrbeast": ["¡Sí, MrBeast es un famoso creador de contenido en YouTube!"],
    "transformers": ["Transformers es una franquicia de medios que gira en torno a robots transformables."],
    "harry potter": ["Harry Potter es una serie de novelas escritas por J.K. Rowling."],
    "qué es minecraft": ["Minecraft es un juego de construcción y aventuras muy popular."]
}

# Nombre predeterminado del chatbot
nombre_chatbot = "ChatGPT"
nombre_usuario = "Usuario"  # Nombre de usuario predeterminado

# Función para generar respuesta basada en la entrada del usuario
def generar_respuesta(entrada_usuario):
    for palabra_clave, respuestas in PALABRAS_CLAVE.items():
        if palabra_clave in entrada_usuario.lower():
            return random.choice(respuestas)
    return "No entiendo lo que quieres decir. ¿Puedes repetirlo o hacer otra pregunta?"

# Función para imprimir la respuesta del chatbot con un color verde claro
def imprimir_respuesta_verde_claro(respuesta):
    print(Fore.LIGHTGREEN_EX + respuesta + Style.RESET_ALL)

# Función para manejar la entrada del usuario
def manejar_entrada(entrada_usuario):
    if entrada_usuario:
        respuesta = generar_respuesta(entrada_usuario)
        print(f"{nombre_chatbot}: ", end='')
        if nombre_chatbot in respuesta:
            imprimir_respuesta_verde_claro(respuesta)
        else:
            print(respuesta)

# Bucle principal para solicitar entrada del usuario
while True:
    entrada_usuario = input(f"{nombre_usuario}: ")
    manejar_entrada(entrada_usuario)
