from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
client = OpenAI(api_key=os.getenv("API_KEY"))

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Listar apenas os nomes dos produtos, sem a considerar a descrição"
        },
        {
            "role": "user",
            "content": "Liste 3 produtos sustentáveis"
        }
    ],
    model= "gpt-4"
)

print(response)
