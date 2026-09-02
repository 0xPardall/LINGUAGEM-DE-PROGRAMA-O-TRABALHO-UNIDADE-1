# 📚 Sistema de Gestão de Notas de Alunos

Sistema simples desenvolvido em **Python** para cadastro de notas,
cálculo da média e determinação da situação final de um aluno.

Este projeto foi desenvolvido como atividade prática da unidade
**Introdução à Linguagem Python**, com foco no uso de **funções,
listas, estruturas condicionais e estruturas de repetição**.

---

## 🎯 Objetivo

O objetivo do projeto é desenvolver um sistema capaz de:

- Cadastrar notas de um aluno;
- Armazenar as notas em uma lista;
- Calcular a média das notas;
- Determinar a situação do aluno;
- Exibir um relatório final.

A regra utilizada para determinar a situação é:

| Média | Situação |
|------:|----------|
| ≥ 7,0 | Aprovado |
| < 7,0 | Reprovado |

---

## 🛠️ Tecnologias

- **Python 3**
- **Nix** para gerenciamento do ambiente de desenvolvimento
- **Git** para controle de versão
- **GitHub** para hospedagem do projeto

O projeto não utiliza bibliotecas externas.

---

## 📁 Estrutura do projeto

```text
sistema-notas/
├── flake.nix
├── main.py
├── notas.py
├── relatorio.py
└── README.md
````

### `main.py`

Arquivo principal da aplicação.

Responsável por:

* iniciar o programa;
* solicitar a quantidade de notas;
* receber as notas do usuário;
* utilizar as funções dos demais módulos;
* gerar o relatório final.

### `notas.py`

Módulo responsável pela lógica relacionada às notas.

Contém as funções:

* `adicionar_nota()`
* `calcular_media()`
* `verificar_situacao()`

### `relatorio.py`

Módulo responsável pela apresentação do resultado final.

Contém a função:

* `gerar_relatorio()`

### `flake.nix`

Define o ambiente de desenvolvimento utilizando Nix,
permitindo executar o projeto com uma versão controlada do Python.

---

## 🚀 Executando o projeto

### Pré-requisitos

É necessário ter:

* Python 3 instalado; ou
* Nix instalado para utilizar o ambiente definido no `flake.nix`.

---

### Utilizando Python diretamente

Execute:

```bash
python main.py
```

---

### Utilizando Nix

Entre no ambiente de desenvolvimento:

```bash
nix develop
```

Depois execute:

```bash
python main.py
```

Também é possível executar diretamente através do pacote definido
no Flake:

```bash
nix run
```

---

## 💻 Exemplo de execução

```text
========================================
   SISTEMA DE GESTÃO DE NOTAS
========================================

Quantas notas deseja cadastrar? 4
Digite a 1ª nota (0 a 10): 8
Digite a 2ª nota (0 a 10): 7
Digite a 3ª nota (0 a 10): 9
Digite a 4ª nota (0 a 10): 6

========================================
          RELATÓRIO FINAL
========================================

Notas cadastradas:
  Nota 1: 8.00
  Nota 2: 7.00
  Nota 3: 9.00
  Nota 4: 6.00

Média final: 7.50
Situação: Aprovado
========================================
```

---

## 🧠 Conceitos utilizados

O projeto aplica conceitos fundamentais da linguagem Python.

### Listas

As notas são armazenadas em uma lista:

```python
notas = []
```

Cada nova nota é adicionada à lista durante a execução.

### Funções

As funcionalidades foram divididas em funções para facilitar a
organização e reutilização do código.

Exemplo:

```python
def calcular_media(notas):
    return sum(notas) / len(notas)
```

### Estruturas de repetição

A estrutura `for` é utilizada para permitir o cadastro de várias notas:

```python
for numero in range(1, quantidade + 1):
    nota = solicitar_nota(numero)
    adicionar_nota(notas, nota)
```

### Estruturas condicionais

A situação do aluno é determinada através de uma estrutura condicional:

```python
if media >= 7:
    return "Aprovado"

return "Reprovado"
```

---

## 🧪 Validação de entradas

O programa também realiza validações básicas.

A quantidade de notas deve ser maior que zero.

As notas devem:

* ser valores numéricos;
* estar entre `0` e `10`.

Exemplo:

```text
Digite a 1ª nota (0 a 10): 15
A nota deve estar entre 0 e 10.
```

---

## 📋 Requisitos da atividade

O projeto contempla os requisitos definidos na atividade prática:

* [x] Cadastro de notas;
* [x] Armazenamento das notas em uma lista;
* [x] Cálculo da média;
* [x] Determinação da situação;
* [x] Relatório final;
* [x] Utilização de funções;
* [x] Utilização de estruturas condicionais;
* [x] Utilização de estruturas de repetição;
* [x] Testes com diferentes entradas;
* [x] Código organizado e comentado.

---

## 📖 Contexto acadêmico

Projeto desenvolvido para a atividade prática:

**Linguagem de Programação**

**Unidade:** U1 — Introdução à Linguagem Python

**Aula:** A4 — Funções em Python

**Experimento:** Sistemas de Gestão de Notas de Alunos

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos e de aprendizagem
da linguagem Python.
