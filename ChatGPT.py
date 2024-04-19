import tkinter as tk
from tkinter import ttk, scrolledtext
import random

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

# Función para manejar la entrada del usuario
def manejar_entrada():
    entrada_usuario = entrada.get("1.0", tk.END).strip()
    if entrada_usuario:
        respuesta = generar_respuesta(entrada_usuario)
        salida.config(state=tk.NORMAL)  # Permitir la edición de la salida
        salida.insert(tk.END, f"{nombre_usuario}: {entrada_usuario}\n")
        salida.insert(tk.END, f"{nombre_chatbot}: " + respuesta + "\n\n")
        salida.see(tk.END)  # Desplazar hacia abajo para mostrar el mensaje más reciente
        salida.config(state=tk.DISABLED)  # Deshabilitar la edición de la salida
        entrada.delete("1.0", tk.END)

# Función para cambiar el nombre del chatbot
def cambiar_nombre_chatbot():
    global nombre_chatbot
    nuevo_nombre = entrada_nombre_chatbot.get()
    if nuevo_nombre:
        nombre_chatbot = nuevo_nombre
        etiqueta_nombre_chatbot.config(text=f"Nombre del Chatbot: {nombre_chatbot}")

# Función para cambiar el nombre de usuario
def cambiar_nombre_usuario():
    global nombre_usuario
    nuevo_nombre_usuario = entrada_nombre_usuario.get()
    if nuevo_nombre_usuario:
        nombre_usuario = nuevo_nombre_usuario
        etiqueta_nombre_usuario.config(text=f"Nombre de Usuario: {nombre_usuario}")

# Crear la ventana principal
raiz = tk.Tk()
raiz.title("Aplicación de ChatGPT")
raiz.resizable(False, False)  # Deshabilitar redimensionamiento de la ventana

# Colores
color_fondo = "#f0f0f0"  # Color de fondo similar al de la página de ChatGPT
color_texto = "#333333"  # Color de texto oscuro

# Configurar estilo
raiz.configure(bg=color_fondo)
raiz.option_add("*Font", "Helvetica 11")
raiz.option_add("*Background", color_fondo)
raiz.option_add("*Foreground", color_texto)

# Etiqueta para mostrar el nombre del chatbot
etiqueta_nombre_chatbot = tk.Label(raiz, text=f"Nombre del Chatbot: {nombre_chatbot}", bg=color_fondo, fg=color_texto)
etiqueta_nombre_chatbot.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")  # Alinear a la izquierda y arriba

# Caja de entrada para cambiar el nombre del chatbot
entrada_nombre_chatbot = ttk.Entry(raiz)
entrada_nombre_chatbot.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="w")  # Alinear a la izquierda y arriba

# Botón para cambiar el nombre del chatbot
boton_cambiar_nombre_chatbot = ttk.Button(raiz, text="Cambiar Nombre", command=cambiar_nombre_chatbot, style='TButton')
boton_cambiar_nombre_chatbot.grid(row=0, column=2, padx=10, pady=(10, 5), sticky="w")

# Etiqueta para mostrar el nombre de usuario
etiqueta_nombre_usuario = tk.Label(raiz, text=f"Nombre de Usuario: {nombre_usuario}", bg=color_fondo, fg=color_texto)
etiqueta_nombre_usuario.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="w")  # Alinear a la izquierda y arriba

# Caja de entrada para cambiar el nombre de usuario
entrada_nombre_usuario = ttk.Entry(raiz)
entrada_nombre_usuario.grid(row=1, column=1, padx=10, pady=(0, 5), sticky="w")  # Alinear a la izquierda y arriba

# Botón para cambiar el nombre de usuario
boton_cambiar_nombre_usuario = ttk.Button(raiz, text="Cambiar Nombre de Usuario", command=cambiar_nombre_usuario, style='TButton')
boton_cambiar_nombre_usuario.grid(row=1, column=2, padx=10, pady=(0, 5), sticky="w")

# Crear la caja de texto de salida
salida = scrolledtext.ScrolledText(raiz, width=50, height=20, state='disabled')
salida.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # Alinear en el centro

# Crear la caja de entrada de texto
entrada = tk.Text(raiz, width=50, height=1)
entrada.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")  # Alinear a la izquierda y abajo

# Crear el botón de enviar con estilo Windows
style = ttk.Style()
style.configure('TButton', padding=4, relief="flat", background=color_fondo, foreground=color_texto, borderwidth=0)
boton_enviar = ttk.Button(raiz, text="Enviar", command=manejar_entrada, style='TButton')
boton_enviar.grid(row=3, column=1, padx=10, pady=(0, 10), sticky="e")  # Alinear a la derecha y abajo

# Ejecutar el bucle principal de la aplicación
raiz.mainloop()
