import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))
model = "gpt-4"

def load_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"Erro: {e}")


def save_file(file_name, content):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")


def feeling_anlysis(product_name):
    system_feeling = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e 
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """

    user_prompt = load_file(f"./data/avaliacoes-{product_name}.txt")
    print(F"Analisando avaliações do produto {product_name}...")

    message_list = [
        {
            "role": "system",
            "content": system_feeling
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=message_list
        )
    except openai.AuthenticationError as e:
        print(f"Erro de autenticação: {e}")
    except openai.APIError as e:
        print(f"Erro ao chamar a API: {e}")

    response_text = response.choices[0].message.content
    save_file(f"./data/analise-{product_name}.txt", response_text)


if __name__ == "__main__":
    list_of_products = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados", "Maquiagem mineral"]
    for product in list_of_products:
        feeling_anlysis(product)
        print(f"Análise do produto {product} concluída.\n")
