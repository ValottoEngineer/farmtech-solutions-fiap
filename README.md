# FarmTech Solutions - Agricultura Digital (Fase 1)

Projeto da FarmTech Solutions para apoiar a fazenda cliente na migração para
Agricultura Digital. Culturas suportadas: **Café** e **Cana-de-açúcar**.

## Estrutura do projeto

```
farmtech-solutions-fiap/
  farm-tech_app.py            # App Python: menu, cadastro, área de plantio e manejo de insumos
  dados_talhoes.csv           # Dados exportados pelo Python (exemplo já incluso)
  estatisticas.R              # App R: média e desvio padrão dos dados do CSV
  clima.R                     # App R (ir além): clima em tempo real via API pública
  resumo_artigo_cap8_vant.txt # Resumo do artigo da disciplina de Formação Social
  video_youtube.txt           # Link do vídeo demonstrativo (preencher)
  empacotar.py                # Gera o ZIP final da entrega
```

## 1. App Python (`farm-tech_app.py`)

Requer apenas Python 3 (nenhuma biblioteca externa).

```bash
python farm-tech_app.py
```

Menu:
1. Cadastrar talhão (entrada de dados: cultura, dimensões e insumo)
2. Listar talhões (saída de dados)
3. Atualizar talhão (por posição do vetor)
4. Deletar talhão (por posição do vetor)
5. Sair

Cada talhão é um registro do vetor `talhoes` (lista de dicionários) com:
- **Área de plantio**: cálculo de retângulo (`largura_m x comprimento_m`).
- **Manejo de insumos**: taxa de aplicação (mL/metro) x comprimento da rua x
  número de ruas, convertido para litros.

Toda vez que você cadastra, atualiza ou deleta um talhão, o app **exporta
automaticamente** os dados para `dados_talhoes.csv` — é esse arquivo que os
scripts em R leem depois. O CSV já vem com 6 talhões de exemplo (3 de café,
3 de cana) para você não depender de digitar dados na hora de testar o R.

## 2. Estatísticas em R (`estatisticas.R`)

Usa apenas R base (sem pacotes extras). Lê `dados_talhoes.csv` e calcula
média e desvio padrão de largura, comprimento, área, nº de ruas, taxa de
aplicação e volume de insumo — no geral e separado por cultura.

```bash
Rscript estatisticas.R
```

## 3. Clima em R (item "ir além") (`clima.R`)

Conecta à API pública e gratuita **Open-Meteo** (sem necessidade de chave/API
key) para buscar o clima atual de uma cidade digitada pelo usuário, e imprime
os dados em texto simples no terminal, com uma recomendação sobre pulverizar
insumos ou não.

Requer o pacote `jsonlite` (instale uma única vez, se ainda não tiver):

```r
install.packages("jsonlite")
```

Depois rode:

```bash
Rscript clima.R
```

## 4. Resumo do artigo (Formação Social)

O arquivo `resumo_artigo_cap8_vant.txt` contém o resumo do capítulo "Uso de
Veículos Aéreos Não Tripulados (VANT) em Agricultura de Precisão" (Embrapa).
**Formatação exigida pelo enunciado (até 1 folha A4)**: copie o texto para o
Word/Google Docs e aplique fonte **Arial 11**, espaçamento **simples (1)**
entre linhas e margens **esquerda/direita de 2 cm**. Exporte como PDF/DOCX
para incluir no ZIP final.

## 5. Vídeo demonstrativo

`video_youtube.txt` é só um placeholder — depois de gravar (até 5 min,
mostrando o Python e o R funcionando) e postar no YouTube como **não
listado**, cole o link real nesse arquivo.

## 6. Gerando o ZIP final da entrega

```bash
python empacotar.py
```

Isso cria `farmtech-solutions-entrega.zip` na pasta do projeto, já com
Python, R, o resumo do artigo e o `video_youtube.txt`.

## Observação sobre o Git

Há um revert de commit parado no meio (`git status` deve mostrar isso) de
antes desta sessão. Antes de commitar as novidades acima, decida se quer
concluir ou abortar esse revert:

```bash
git status
git revert --abort   # ou: git revert --continue, dependendo do que quiser manter
```

Depois disso, adicione e commite os arquivos normalmente para versionar no
GitHub, conforme pedido no enunciado.
