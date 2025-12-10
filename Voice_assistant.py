import speech_recognition as sr
import pyttsx3
import webbrowser

# Inicializamos el reconocedor y el motor de texto a voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def hablar(texto):
    """Función para que el asistente hable"""
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    """Función para escuchar y reconocer voz en español"""
    microphone = sr.Microphone()
    
    with microphone as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)  # Elimina ruido de fondo
        audio = recognizer.listen(source)
    
    try:
        print("Procesando...")
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {text}")
        return text.lower()
    
    except sr.UnknownValueError:
        hablar("No pude entenderte, ¿puedes repetirlo?")
        print("No te entendí")
        return ""
    
    except sr.RequestError:
        hablar("Hay un problema con el servicio de reconocimiento")
        print("Error de conexión con Google")
        return ""

def talk():
    """Función principal del asistente"""
    comando = escuchar()
    
    if comando:
        if "hola" in comando:
            hablar("¡Hola! ¿En qué te puedo ayudar?")
        
        elif "youtube" in comando:
            hablar("Abriendo YouTube")
            webbrowser.open("https://www.youtube.com")
        
        elif "google" in comando:
            hablar("Abriendo Google")
            webbrowser.open("https://www.google.com")
        
        elif "adiós" in comando or "salir" in comando:
            hablar("¡Hasta luego!")
            return False  # Para salir del bucle
    
    return True

# Bucle principal
hablar("Asistente de voz activado. Di algo...")
while True:
    if not talk():
        break
    



