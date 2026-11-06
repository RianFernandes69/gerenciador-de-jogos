# 🎮 Gerenciador de Lista de Jogos em Python

Projeto desenvolvido durante meus estudos de programação em Python, com o objetivo de praticar lógica de programação e desenvolver um sistema interativo para gerenciamento de jogos.

O projeto foi evoluindo conforme novos conceitos foram aprendidos e aplicados.

## 📌 Versões do projeto

### Versão 2.0 — Menu interativo

Arquivo: `main.py`

Funcionalidades:
- Mostrar os jogos cadastrados.
- Pesquisar jogos.
- Cadastrar novos jogos.
- Consultar jogos por posição.
- Remover jogos.
- Exibir a lista e a quantidade de jogos ao encerrar.

Conceitos utilizados:
- Variáveis e tipos de dados.
- Listas.
- Estruturas condicionais (`if`, `elif` e `else`).
- Laços de repetição (`while` e `for`).
- Operadores lógicos.
- Métodos de listas (`append` e `remove`).
- Entrada de dados com `input()`.

### Versão 3.0 — Organização com funções

Arquivo: `gerenciador_v3.py`

A versão 3.0 mantém as funcionalidades da versão anterior, mas introduz funções para organizar melhor o código.

Novidades:
- Funções para mostrar, pesquisar, adicionar e remover jogos.
- Consulta de jogos por posição.
- Contagem de jogos por meio de uma função.
- Reutilização de código.
- Separação das responsabilidades de cada funcionalidade.

Novos conceitos utilizados:
- Definição de funções com `def`.
- Parâmetros e argumentos.
- Retorno de valores com `return`.
- Organização e reutilização de código.

### Versão 4.0 — Organização, validação e testes

Arquivo: `gerenciador_v4.py`

A versão 4.0 aprimora o sistema, adicionando validações e melhorando a organização dos arquivos.

Novidades:
- Normalização automática dos nomes com `strip()` e `lower()`.
- Bloqueio de jogos duplicados utilizando conjuntos (`set`).
- Pesquisa e remoção com comparação de nomes normalizados.
- Proteção da execução do menu com `if __name__ == "__main__":`.
- Separação dos testes em um arquivo independente.
- Importação de funções e variáveis entre arquivos.

Novos conceitos utilizados:
- Conjuntos (`set`).
- Métodos de strings (`strip()` e `lower()`).
- Importação de funções com `from` e `import`.
- Módulos Python.
- Testes de funções.
- `if __name__ == "__main__"`.

Testes realizados:
- Pesquisa de jogos.
- Adição de jogos.
- Bloqueio de duplicatas.
- Remoção de jogos.
- Consulta de posições.
- Contagem e exibição dos jogos.

Resultado: 6 de 6 testes aprovados.

## 📂 Estrutura dos arquivos

```text
gerenciador-de-jogos/
│
├── gerenciador_v3.py
├── gerenciador_v4.py
├── main.py
├── menu_jogos.py
├── README.md
├── teste_funcoes_v4.py
├── teste_funcoes.py
└── teste_importacao.py
```

## ▶️ Como executar

É necessário ter o Python 3 instalado.

Para executar a versão 2.0:

```bash
python main.py
```

Para executar a versão 3.0:

```bash
python gerenciador_v3.py
```

Para executar a versão 4.0:

```bash
python gerenciador_v4.py
```

Para executar os testes da versão 4.0:

```bash
python teste_funcoes_v4.py
```

## 🎯 Objetivo de aprendizagem

Este projeto faz parte da minha jornada de aprendizado em programação. O objetivo é desenvolver conhecimentos em lógica de programação, organização de código e construção de aplicações, evoluindo gradualmente para projetos mais completos.

As versões são mantidas separadamente para demonstrar a evolução do código e dos conhecimentos aplicados ao longo dos estudos.

---

Desenvolvido durante meus estudos de Python.