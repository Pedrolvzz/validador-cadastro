# ✅ Validador de Cadastro em Python

Projeto de estudo desenvolvido em Python para verificar o formato básico de e-mails e os dígitos verificadores de CPF, com interação pelo terminal.

## Funcionalidades

### 📧 E-mail

- Verifica se existe exatamente um `@`.
- Recusa espaços.
- Confere se o usuário e o domínio estão preenchidos.
- Verifica se o domínio contém um ponto.
- Recusa pontos consecutivos.
- Recusa pontos no início ou no final do usuário e do domínio.

### 🪪 CPF

- Aceita entradas com ou sem pontos e traço.
- Verifica se o CPF contém 11 dígitos.
- Recusa sequências com todos os dígitos iguais.
- Calcula e confere os dois dígitos verificadores.

## Como executar

É necessário ter o **Python 3** instalado.

1. Baixe os arquivos do repositório.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python main.py
```

Caso seu arquivo tenha outro nome, substitua `main.py` pelo nome correspondente.

## Menu

```text
=== VALIDADOR DE CADASTRO ===

1 - Validar Email
2 - Validar CPF
3 - Sair
```

Escolha uma opção e digite o dado solicitado para receber o resultado da verificação.

## Conceitos praticados

- Entrada e saída com `input()` e `print()`.
- Condições com `if`, `elif` e `else`.
- Repetições com `while`.
- Operadores lógicos e comparações.
- Manipulação e indexação de strings.
- Conversão de tipos com `int()`.
- Resto da divisão com `%`.

## Limitações

Este projeto tem finalidade educativa.

- A verificação de e-mail aplica regras básicas de formato; não cobre todas as possibilidades de endereços válidos nem confirma que a caixa de e-mail existe.
- A verificação de CPF confere a estrutura e os dígitos verificadores. Não consulta a Receita Federal nem confirma existência, titularidade ou situação cadastral.

Use dados fictícios em demonstrações e não publique informações pessoais no repositório.
