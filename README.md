# Projeto Desenvolvedor para a empresa Target Sistemas

Este projeto visa resolver uma série de problemas relacionados ao processamento e análise de dados, com o uso de Python. O projeto contém funcionalidades como cálculos financeiros, manipulação de dados e verificação de sequências matemáticas.

## Funcionalidades

1. **Cálculo da Soma de Números**  
   Um código simples que calcula a soma dos números de 1 até 13 utilizando uma estrutura de repetição.

2. **Verificação de Números na Sequência de Fibonacci**  
   O programa verifica se um número informado pelo usuário pertence ou não à sequência de Fibonacci.

3. **Análise de Faturamento Diário**  
   O projeto carrega dados de faturamento a partir de arquivos (em formato JSON ou XML), e realiza a análise dos seguintes pontos:
   - Menor valor de faturamento no mês.
   - Maior valor de faturamento no mês.
   - Número de dias com faturamento superior à média mensal, desconsiderando dias sem faturamento (finais de semana e feriados).

4. **Cálculo do Percentual de Faturamento por Estado**  
   O programa calcula o percentual de faturamento de diferentes estados de uma distribuidora, considerando valores predefinidos para cada estado.

5. **Inversão de String**  
   Um programa simples que inverte os caracteres de uma string fornecida, sem usar funções prontas como `reverse`.

## Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas:
  - `json`: Para manipulação de dados JSON.
  - `xml.etree.ElementTree`: Para leitura e manipulação de arquivos XML.

## Como Rodar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/TanigeDamasceno/Desenvolvedor.git
Navegue até o diretório do projeto:

bash
Copiar código
cd Desenvolvedor
Caso haja dependências externas, instale-as (se necessário):

bash
Copiar código
pip install -r requirements.txt
Execute o código desejado:

bash
Copiar código
python nome_do_arquivo.py
Exemplo para rodar o cálculo de soma:
bash
Copiar código
python Simulado.py
Estrutura do Projeto
plaintext
Copiar código
Desenvolvedor/

├── Simulado.py           # Script principal que contém a implementação de lógica de negócios

├── faturamento.xml       # Arquivo XML com dados de faturamento diário

├── dados.json            # Arquivo JSON com dados de faturamento


├── README.md             # Este arquivo

└── requirements.txt      # Arquivo de dependências (se necessário)
