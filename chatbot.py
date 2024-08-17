from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear una instancia del chatbot con configuración personalizada
chatbot = ChatBot(
    'Chatbot Mejorado',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
    ]
)

# Entrenar el chatbot usando el corpus en español
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")

# Función principal de conversación con manejo de excepciones y mejor flujo
def iniciar_conversacion():
    print("Hola! Soy tu asistente virtual. Escribe 'adiós' para finalizar la conversación.")
    
    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() in ["adiós", "adios", "salir", "exit", "bye"]:
                print("Chatbot: ¡Hasta luego! Que tengas un buen día.")
                break

            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        
        except(KeyboardInterrupt, EOFError, SystemExit):
            print("\nChatbot: ¡Hasta luego! Que tengas un buen día.")
            break

if __name__ == "__main__":
    iniciar_conversacion()