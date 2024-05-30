import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv(dotenv_path='data/.env')

# Récupérer la clé API depuis les variables d'environnement
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Vérifier si la clé API est définie
if not OPENAI_API_KEY:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

# Définir la clé API pour le client OpenAI
openai.api_key = OPENAI_API_KEY

def obtenir_reponse(prompt):
    try:
        # Appel à l'API OpenAI pour obtenir une réponse
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"

def main():
    print("Bienvenue au bot console OpenAI. Tapez 'exit' pour quitter.")
    while True:
        prompt = input("Vous : ")
        if prompt.lower() == 'exit':
            print("Au revoir!")
            break
        response = obtenir_reponse(prompt)
        print(f"Bot : {response}")

if __name__ == "__main__":
    main()
