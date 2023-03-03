import openai

openai.api_key = "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"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,     #comando de entrada 
        max_tokens = 2024,    #quantidade de palavras 
        temperature = 0.5,    #conhecimentos solidos 
        n=1,
        stop=None 
    )
    message = completions.choices[0].text
    return message.strip()

quantperg= int(input("Quantas perguntas deseja fazer ?\n"))

for n in range(0,quantperg):
    prompt = input (f'Faça a {n+1}º pergunta: \n')
    print(generate_text(prompt))
        
