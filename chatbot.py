def get_response(user_input):
    # Diccionario simple de preguntas y respuestas
    responses = {
        "hola": "¡Hola! ¿Cómo estás?",
        "bien": "Me alegra saberlo. ¿En qué puedo ayudarte?",
        "adiós": "¡Hasta luego! Que tengas un buen día.",
        "gracias": "¡De nada! Estoy aquí para ayudar.",
    }
    
    # Convierte la entrada del usuario a minúsculas
    user_input = user_input.lower()

    # Busca la respuesta en el diccionario
    return responses.get(user_input, "Lo siento, no entiendo eso.")

def main():
    print("Chatbot: ¡Hola! Soy tu asistente virtual. Escribe 'adiós' para terminar la conversación.")
    while True:
        user_input = input("Tú: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        
        if user_input.lower() == "adiós":
            break

if __name__ == "__main__":
    main()