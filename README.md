# Sudoku Validator
![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

Bem-vindo ao **Sudoku Validator**, um projeto em Python que valida tabuleiros de Sudoku 9x9 conforme as regras clássicas do jogo.

## Sobre o Projeto
O objetivo é criar uma ferramenta eficiente para verificar a validade de tabuleiros de Sudoku, com foco em lógica e boas práticas de programação.

### Regras Validadas
- Cada linha deve conter números de 1 a 9 sem repetição.
- Cada coluna deve seguir a mesma regra.
- Cada subgrade 3x3 deve ser válida.

## Instalação
1. Certifique-se de ter Python 3.8 ou superior instalado.
2. Clone o repositório:
   
   ```git clone https://github.com/fxlipe124/sudoku-validator.git```
4. Navegue até o diretório:
   
   ```cd sudoku-validator```
5. Execute:
   
   ```python sudoku_validator.py```

Estrutura do Código

```is_valid_sudoku``` ```is_valid_unit``` são funções que contém a lógica principal de validação.

```board``` exemplo de tabuleiro no código (editável).

## Como Funciona

O programa usa uma abordagem modular:

Verifica linhas, colunas e subgrades separadamente.

Usa conjuntos (set) para detectar duplicatas em O(n).

Ignora células vazias (representadas por 0).

## Exemplo de Uso 
Basta editar ou inserir novos números na varíavel "board" para validar o seu tabuleiro.

## Próximos Passos
Adicionar interface para entrada de tabuleiros.

Implementar um gerador de Sudoku.

## Contribuições
Sugestões são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

Desenvolvido por Felipe - mar, 2025.
