import json

# 1. Valor da variável SOMA
INDICE = 13
SOMA = 0
K = 0

# Laço 'while' para somar os números de 1 até INDICE
while K < INDICE:
    K += 1  # Aumenta K em 1 a cada iteração
    SOMA += K  # Soma o valor de K à variável SOMA

# Imprime o valor final de SOMA
print(f"O valor final de SOMA é: {SOMA}")


# 2. Verificar número na sequência de Fibonacci
def pertence_fibonacci(numero):
    a, b = 0, 1  # Primeiros dois valores da sequência de Fibonacci
    while a <= numero:  # Enquanto o valor de 'a' for menor ou igual ao número informado
        if a == numero:  # Se o número 'a' for igual ao número informado
            return True  # O número pertence à sequência
        a, b = b, a + b  # Atualiza os valores de 'a' e 'b' para o próximo número da sequência
    return False  # Se o número não for encontrado na sequência, retorna False

# Solicita ao usuário que informe um número
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci e exibe a mensagem correspondente
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")


# 3. Análise do faturamento diário (usando dados JSON)
# Função para carregar os dados JSON a partir de um arquivo
def carregar_dados_json(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)  # Carrega os dados do arquivo JSON
    return dados

# Função para calcular o menor, maior e a média de faturamento
def calcular_faturamento(faturamento_diario):
    # Filtra os valores de faturamento, desconsiderando os dias com faturamento 0
    faturamento = [x['valor'] for x in faturamento_diario if x['valor'] > 0]
    
    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    
    # Calcula a média de faturamento diário, ignorando os dias sem faturamento
    media_mensal = sum(faturamento) / len(faturamento)
    
    # Conta o número de dias em que o faturamento foi superior à média mensal
    dias_acima_da_media = len([x for x in faturamento if x > media_mensal])

    # Exibe os resultados
    print(f"Menor faturamento: {menor_faturamento:.2f}")
    print(f"Maior faturamento: {maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# Carrega os dados JSON de um arquivo
arquivo_json = 'dados.json'  # Caminho para o arquivo JSON
faturamento_diario = carregar_dados_json(arquivo_json)

# Realiza os cálculos e exibe os resultados
calcular_faturamento(faturamento_diario)


# 4. Percentual de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calculando o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calculando o percentual de cada estado
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

# Exibe o percentual de cada estado
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")


# 5. Inverter uma string
def inverter_string(s):
    invertida = ""  # Inicializa uma string vazia para armazenar a string invertida
    for char in s:  # Para cada caractere na string original
        invertida = char + invertida  # Coloca o caractere na frente da string invertida
    return invertida  # Retorna a string invertida

# Solicita ao usuário que informe uma string
string = input("Informe uma string: ")

# Exibe a string invertida
print(f"String invertida: {inverter_string(string)}")
