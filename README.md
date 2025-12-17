# LeetCodePY

Repositório de soluções de problemas do LeetCode implementadas em Python.

## Sobre o Projeto

Este repositório contém minhas soluções para problemas de algoritmos do LeetCode, desenvolvidas como parte do meu aprendizado em Python e estruturas de dados.

## Estrutura do Projeto

```
leetCode/
├── lc1.py          # LeetCode #1 - Two Sum
├── lc9.py          # LeetCode #9 - Palindrome Number
├── lc13.py         # LeetCode #13 - Roman to Integer
├── arrayI.py       # LeetCode #1929 - Concatenation of Array
├── arrayII.py      # LeetCode #1470 - Shuffle the Array
└── arrayIII.py     # LeetCode #485 - Max Consecutive Ones
```

## Problemas Resolvidos

### Problemas Numéricos

| # | Problema | Dificuldade | Arquivo | Solução |
|---|----------|-------------|---------|---------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | `lc1.py` | Força bruta com loops aninhados |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | `lc9.py` | Conversão para string e comparação |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | `lc13.py` | Dicionário com lógica de subtração |

### Problemas de Arrays

| # | Problema | Dificuldade | Arquivo | Solução |
|---|----------|-------------|---------|---------|
| 1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | `arrayI.py` | Método `.extend()` |
| 1470 | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) | Easy | `arrayII.py` | `insert()` e `pop()` |
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Easy | `arrayIII.py` | Iteração com contador |

## Como Executar

Cada arquivo contém uma solução independente que pode ser executada diretamente:

```bash
python lc1.py
python lc9.py
python lc13.py
python arrayI.py
python arrayII.py
python arrayIII.py
```

## Tecnologias

- Python 3
- Type hints (em alguns arquivos)

## Padrões de Código

- Cada problema segue o padrão de classe `Solution` do LeetCode
- Casos de teste incluídos no final de cada arquivo
- Soluções funcionais com foco em legibilidade

## Progresso

Total de problemas resolvidos: **6**

- Easy: 6
- Medium: 0
- Hard: 0

## Autor

Gabriel

## Licença

Este projeto é de código aberto e está disponível para fins educacionais.
