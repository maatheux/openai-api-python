from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
client = OpenAI(api_key=os.getenv("API_KEY"))
model = "gpt-3.5-turbo"

qt_responses = 3

def categorize_product(product_name, product_name_list):
    system_prompt = f"""
            Você é um categorizador de produtos.
            Você deve assumir as categorias presentes na lista abaixo.
    
            # Lista de Categorias Válidas
            {product_name_list.split(", ")}
    
            # Formato da Saída
            Produto: Nome do Produto
            Categoria: apresente a categoria do produto
    
            # Exemplo de Saída
            Produto: Escova elétrica com recarga solar
            Categoria: Eletrônicos Verdes
        """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": product_name
            }
        ],
        model=model,
        temperature=1,
        max_tokens=400,
        # n=qt_responses
    )

    return response.choices[0].message.content

    #print(response.choices[0].message.content)

    # for counter in range(0, qt_responses):
    #     print(response.choices[counter].message.content)
    #     print("--------------------")


def main():
    categories_list = input("Apresente a lista de categorias separadas por vírgula: ")
    while True:
        product_name = input("Apresente o nome do produto: ")
        response_text = categorize_product(product_name, categories_list)
        print(response_text)


if __name__ == "__main__":
    main()
