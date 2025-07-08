# 📊 Gerador de Vídeo Contador

Este projeto gera vídeos animados que contam valores numéricos até marcos definidos, com animações suaves e efeitos visuais ao final.

## 📦 Requisitos

* Python 3.9+
* Windows (ou ajuste de fontes para Linux/Mac)

### 📅 Instalar dependências:

```bash
pip install moviepy pillow numpy
```

## 🚀 Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/your-username/gerador-video-contador.git
cd gerador-video-contador
```

2. Crie um arquivo `config_local.py` com suas configurações preferidas (veja exemplo abaixo). Se não existir, o sistema usará valores padrão internos.

3. Execute o script principal:

```bash
python main.py
```

4. O vídeo será exportado com o nome e pasta definidos em `arquivo_saida`.

## 🔧 Exemplo de `config_local.py`

```python
CONFIG = {
    "largura": 1280,                         # Largura do vídeo (px)
    "altura": 720,                           # Altura do vídeo (px)
    "fps": 30,                              # Frames por segundo

    "cor_fundo": (0, 0, 0),                 # RGB - Cor do fundo
    "cor_texto": (255, 255, 255),           # RGB - Cor dos números
    "cor_contorno": (255, 0, 0),            # RGB - Cor da borda do texto
    "espessura_contorno": 3,                # Espessura da borda (px)

    "caminho_fonte": "C:\\Windows\\Fonts\\arialbd.ttf",  # Caminho da fonte
    "tamanho_fonte": 120,                   # Tamanho da fonte (pt)

    "valores_marcos": [100, 250, 400],     # Lista de valores a serem mostrados
    "texto_unidade_monetaria": "R$",       # Prefixo para os números

    "tempo_animacao": 3.0,                  # Tempo padrão entre valores (s)
    "tempo_pausa": 1.0,                     # Pausa após cada valor (s)
    "tempo_final_extra": 4.0,               # Tempo extra após o valor final (s)

    "efeito_piscar_final": True,            # Ativar piscar no valor final?
    "cores_piscar": [(255,255,255), (255,215,0), (255,0,0)],  # Cores do piscar
    "piscar_por_segundo": 6,                # Frequência do piscar (vezes/segundo)

    "tempo_animacao_aleatorio": False,      # Tempo aleatório por valor?
    "intervalo_tempo_animacao": [3.0, 5.0], # Intervalo de tempo aleatório (s)

    "fator_inicio_suave": 1.0,              # Suavidade no início (maior = mais suave)
    "fator_fim_suave": 1.0,                 # Suavidade no fim (maior = mais suave)

    "arquivo_saida": "saida_video.mp4"      # Nome do arquivo final do vídeo
}
```

## 🗒️ Descrição dos Campos do CONFIG

| Campo                      | Tipo          | Unidade      | Descrição                                |
| -------------------------- | ------------- | ------------ | ---------------------------------------- |
| `largura` / `altura`       | `int`         | px           | Dimensões do vídeo                       |
| `fps`                      | `int`         | quadros/seg  | Frames por segundo                       |
| `cor_*`                    | `tuple[int]`  | RGB          | Cores do fundo, texto e contorno         |
| `espessura_contorno`       | `int`         | px           | Espessura da borda do texto              |
| `caminho_fonte`            | `str`         | caminho      | Caminho para arquivo .ttf                |
| `tamanho_fonte`            | `int`         | pt           | Tamanho da fonte                         |
| `valores_marcos`           | `list[int]`   | unidade      | Valores a serem contados                 |
| `texto_unidade_monetaria`  | `str`         | símbolo      | Ex: "R\$", "US\$"                        |
| `tempo_animacao`           | `float`       | segundos     | Duração padrão da animação               |
| `tempo_pausa`              | `float`       | segundos     | Pausa após cada valor                    |
| `tempo_final_extra`        | `float`       | segundos     | Tempo para efeito final                  |
| `efeito_piscar_final`      | `bool`        | -            | Ativa efeito de piscar final             |
| `cores_piscar`             | `list[tuple]` | RGB          | Cores usadas no piscar                   |
| `piscar_por_segundo`       | `int`         | vezes/seg    | Frequência do piscar                     |
| `tempo_animacao_aleatorio` | `bool`        | -            | Ativa variação do tempo                  |
| `intervalo_tempo_animacao` | `list[float]` | segundos     | Intervalo para tempo aleatório           |
| `fator_inicio_suave`       | `float`       | sem unidade  | Suavidade no início (maior = mais suave) |
| `fator_fim_suave`          | `float`       | sem unidade  | Suavidade no fim (maior = mais suave)    |
| `arquivo_saida`            | `str`         | nome arquivo | Nome do vídeo exportado                  |

## 📁 `.gitignore` sugerido

```bash
config_local.py
__pycache__/
*.pyc
*.mp4
```

## 🌐 Versões internacionais

* [`README.en.md`](README.en.md): Versão em inglês
* [`README.pt.md`](README.pt.md): Versão em português

---

Feito com 💻 por \[Daniwl] — contribuições são bem-vindas!