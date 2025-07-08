# Gerador de Video Contador / Counter Video Generator

Sistema em Python para gerar vídeos que exibem contadores numéricos com animações e efeitos visuais. Ideal para criar vídeos de metas, arrecadação ou contagens regressivas/positivas.

---

## 🌐 Idiomas

* [Leia em Português](#uso-em-português)
* [Read in English](#usage-in-english)

---

## Uso em Português

### Instalação

1. Certifique-se de ter o Python 3.9 ou superior instalado.

2. Instale as dependências obrigatórias:

```bash
pip install moviepy pillow numpy
```

### Execução

1. Crie o arquivo `config_local.py` com as configurações desejadas (veja abaixo um exemplo).
2. Execute o script principal:

```bash
python vContador.py
```

### Exemplo de `config_local.py`

```python
CONFIG = {
    "largura": 1920,
    "altura": 1080,
    "fps": 30,
    "cor_fundo": (30, 30, 30),
    "cor_texto": (255, 255, 255),
    "cor_contorno": (0, 0, 0),
    "espessura_contorno": 3,
    "caminho_fonte": "C:\\Windows\\Fonts\\arialbd.ttf",
    "tamanho_fonte": 180,
    "tempo_animacao": 3.0,
    "tempo_pausa": 1.5,
    "tempo_final_extra": 5.0,
    "valores_marcos": [100, 500, 1000],
    "efeito_piscar_final": True,
    "cores_piscar": [(255, 255, 255), (255, 215, 0)],
    "piscar_por_segundo": 5,
    "arquivo_saida": "meu_video.mp4",
    "texto_unidade_monetaria": "R$"
}
```

> ✅ **Nota:** Se algum campo for omitido, o sistema usará os valores padrão.

### Campos do CONFIG explicados

| Campo                     | Descrição                                    |
| ------------------------- | -------------------------------------------- |
| `largura`, `altura`       | Dimensões do vídeo                           |
| `fps`                     | Frames por segundo                           |
| `cor_fundo`               | Cor de fundo do vídeo (RGB)                  |
| `cor_texto`               | Cor principal do texto                       |
| `cor_contorno`            | Cor da borda do texto                        |
| `espessura_contorno`      | Espessura da borda do texto                  |
| `caminho_fonte`           | Caminho da fonte TTF                         |
| `tamanho_fonte`           | Tamanho da fonte                             |
| `tempo_animacao`          | Tempo de contagem entre marcos               |
| `tempo_pausa`             | Pausa após cada marco                        |
| `tempo_final_extra`       | Tempo extra ao final (para efeito de piscar) |
| `valores_marcos`          | Lista dos valores a serem contados           |
| `efeito_piscar_final`     | Se verdadeiro, o número final piscará        |
| `cores_piscar`            | Lista de cores para o efeito de piscar       |
| `piscar_por_segundo`      | Quantas vezes por segundo o número pisca     |
| `arquivo_saida`           | Nome do arquivo MP4 gerado                   |
| `texto_unidade_monetaria` | Prefixo como "R\$" ou "\$"                   |

### Evitar subir config\_local.py para o GitHub

Adicione no `.gitignore`:

```
config_local.py
```

---

## Usage in English

### Installation

1. Make sure Python 3.9 or newer is installed.

2. Install dependencies:

```bash
pip install moviepy pillow numpy
```

### Running

1. Create a file `config_local.py` with your preferred settings (see example below).
2. Run the script:

```bash
python vContador.py
```

### Example `config_local.py`

```python
CONFIG = {
    "largura": 1920,
    "altura": 1080,
    "fps": 30,
    "cor_fundo": (30, 30, 30),
    "cor_texto": (255, 255, 255),
    "cor_contorno": (0, 0, 0),
    "espessura_contorno": 3,
    "caminho_fonte": "C:\\Windows\\Fonts\\arialbd.ttf",
    "tamanho_fonte": 180,
    "tempo_animacao": 3.0,
    "tempo_pausa": 1.5,
    "tempo_final_extra": 5.0,
    "valores_marcos": [100, 500, 1000],
    "efeito_piscar_final": True,
    "cores_piscar": [(255, 255, 255), (255, 215, 0)],
    "piscar_por_segundo": 5,
    "arquivo_saida": "my_video.mp4",
    "texto_unidade_monetaria": "$"
}
```

> ✅ **Note:** If a field is missing, the script will use default values.

### CONFIG Field Descriptions

Same as the table above, just translated.

---

## Licença / License

MIT — livre para uso, modificação e distribuição.
