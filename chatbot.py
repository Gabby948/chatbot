def responder(user_input):
    user_input = user_input.lower()  # Asegúrate de que esta línea esté correctamente indentada

    if "hola" in user_input:
        return "¡Hola! ¿Cómo estás?"
    elif "adiós" in user_input or "adios" in user_input:
        return "¡Hasta luego! Cuídate."
    elif "cómo estás" in user_input or "cómo te va" in user_input:
        return "Estoy bien, gracias por preguntar. ¿Y tú?"
    elif "nombre" in user_input:
        return "Soy un chatbot simple creado en Python."
    else:
        return "Lo siento, no entiendo tu pregunta."

# conversación
print("Hola, soy un chatbot simple. ¿En qué puedo ayudarte? (Escribe 'adiós' para salir)")

while True:
    user_input = input("Tú: ")
    
    if "adiós" in user_input.lower() or "adios" in user_input.lower():
        print("Chatbot: ¡Hasta luego!")
        break

    response = responder(user_input)
    print(f"Chatbot: {response}")