# def get_response(user_input):
#     responses = {
#         "hola": "¡Hola! ¿Cómo estás?",
#         "bien": "Me alegra saberlo. ¿En qué puedo ayudarte?",
#         "adiós": "¡Hasta luego! Que tengas un buen día.",
#         "gracias": "¡De nada! Estoy aquí para ayudar.",
#     }
    

#     user_input = user_input.lower()

#     return responses.get(user_input, "Lo siento, no entiendo eso.")

# def main():
#     print("Chatbot: ¡Hola! Soy tu asistente virtual. Escribe 'adiós' para terminar la conversación.")
#     while True:
#         user_input = input("Tú: ")
#         response = get_response(user_input)
#         print(f"Chatbot: {response}")
        
#         if user_input.lower() == "adiós":
#             break

# if __name__ == "__main__":
#     main()

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear una instancia del chatbot
chatbot = ChatBot('Chatbot test')

# Entrenar el chatbot 
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")

# Conversación 
while True:
    user_input = input("Tú: ")
    response = chatbot.get_response(user_input)
    print(f"Chatbot: {response}")

    if user_input.lower() == "adiós":
        break