import json   # Importa el módulo para trabajar con archivos JSON
import os     # Importa el módulo para interactuar con el sistema operativo

# =========================
# Módulo de adquisición de conocimiento
# =========================

ARCHIVO_BASE = "Conocimiento.json"  # Nombre del archivo donde se guarda el conocimiento

# Si no existe la base, crearla con preguntas y respuestas iniciales
if not os.path.exists(ARCHIVO_BASE):  # Verifica si el archivo de conocimiento existe
    conocimiento_inicial = {          # Diccionario con preguntas y respuestas por defecto
        "hola": "Hola, ¿cómo estás?",
        "como estas?": "Estoy bien, gracias. ¿Y tú?",
        "de que te gustaria hablar?": "Podemos hablar de tecnología, ciencia o lo que quieras."
    }
    # Crea el archivo y guarda el conocimiento inicial en formato JSON
    with open(ARCHIVO_BASE, "w", encoding="utf-8") as f:
        json.dump(conocimiento_inicial, f, ensure_ascii=False, indent=2)

# Función para cargar conocimiento desde el archivo JSON
def cargar_conocimiento():
    with open(ARCHIVO_BASE, "r", encoding="utf-8") as f:
        return json.load(f)  # Devuelve el diccionario cargado

# Función para guardar el conocimiento actualizado en el archivo JSON
def guardar_conocimiento(base):
    with open(ARCHIVO_BASE, "w", encoding="utf-8") as f:
        json.dump(base, f, ensure_ascii=False, indent=2)

# =========================
# Chatbot
# =========================

print("ChatBot Aprendiz (escribe 'salir' para terminar)")  # Mensaje de bienvenida
base_conocimiento = cargar_conocimiento()  # Carga el conocimiento existente

while True:  # Bucle principal del chatbot
    pregunta = input("Tú: ").strip().lower()  # Lee la pregunta del usuario, quita espacios y pone en minúsculas
    if pregunta == "salir":                   # Si el usuario escribe 'salir', termina el chat
        print("ChatBot: ¡Hasta luego!")
        break

    if pregunta in base_conocimiento:         # Si la pregunta está en la base de conocimiento
        print("ChatBot:", base_conocimiento[pregunta])  # Responde con la respuesta guardada
    else:
        print("ChatBot: No sé qué responder a eso.")    # Si no sabe la respuesta
        nueva_respuesta = input("💡 ¿Qué debería responder cuando me digas eso?: ").strip()  # Pide al usuario la respuesta correcta
        base_conocimiento[pregunta] = nueva_respuesta   # Añade la nueva pregunta y respuesta a la base
        guardar_conocimiento(base_conocimiento)         # Guarda la base actualizada en el archivo
        print("Conocimiento aprendido.")                # Informa que ha aprendido