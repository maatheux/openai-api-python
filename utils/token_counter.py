import math

import tiktoken

model = "gpt-4"
coder = tiktoken.encoding_for_model(model)
token_list = coder.encode("Você é um categorizador de produtos.")

gpt4_cost = (len(token_list)/1000) * 0.03

print(model)
print(f"Lista de tokens: {token_list}")
print(f"Quantidade de tokens: {len(token_list)}")
print(f"Custo para o modelo {model} é de ${gpt4_cost}")

# Write the same code above but using gpt-3.5-turbo as model
model = "gpt-3.5-turbo"
coder = tiktoken.encoding_for_model(model)
token_list = coder.encode("Você é um categorizador de produtos.")

gpt3_cost = (len(token_list)/1000) * 0.0005

print(model)
print(f"Lista de tokens: {token_list}")
print(f"Quantidade de tokens: {len(token_list)}")
print(f"Custo para o modelo {model} é de ${gpt3_cost}")

print(f"\nO custo para o modelo gpt-4 é {math.floor(gpt4_cost/gpt3_cost)} vezes maior que o custo para o modelo gpt-3.5-turbo.")
