import unittest
from unittest.mock import patch
import openai
import os

# Importer le script principal
from src.chatbot import obtenir_reponse

class TestOpenAIBot(unittest.TestCase):
    @patch('openai.ChatCompletion.create')
    def test_obtenir_reponse(self, mock_create):
        # Définir la réponse fictive de l'API
        mock_create.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Hello!"
                    }
                }
            ]
        }

        # Appeler la fonction avec un exemple de prompt
        prompt = "Salut"
        response = obtenir_reponse(prompt)

        # Vérifier que la réponse est correcte
        self.assertEqual(response, "Hello!")

    @patch('openai.ChatCompletion.create')
    def test_obtenir_reponse_erreur(self, mock_create):
        # Simuler une exception
        mock_create.side_effect = Exception("API error")

        # Appeler la fonction avec un exemple de prompt
        prompt = "Salut"
        response = obtenir_reponse(prompt)

        # Vérifier que l'erreur est gérée correctement
        self.assertTrue(response.startswith("Une erreur s'est produite"))

if __name__ == '__main__':
    unittest.main()
