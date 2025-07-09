# 📊 Gerador de Vídeo Contador

Sistema Python para gerar vídeos com contagem animada até valores definidos, com suavização e efeitos visuais no final.

---

## 📁 Estrutura do Projeto

```
video_counter_system/
├── main.py
├── requirements.txt
├── config/
│   ├── config_loader.py
│   └── default_config.py
├── src/
│   ├── animation/
│   ├── rendering/
│   └── video/
└── tests/
```

---

## 📦 Requisitos

* Python 3.9 ou superior
* Windows (ou ajustar caminho da fonte no Linux/Mac)

---

## ⚙️ Instalação

```bash
pip install -r requirements.txt
```

---

## 🚀 Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/video_counter_system.git
cd video_counter_system
```

2. (Opcional) Crie um arquivo `config_local.py` na raiz com suas configurações personalizadas.
   Se não existir, serão usados valores padrão (`config/default_config.py`).

3. Execute o sistema:

```bash
python main.py
```

4. O vídeo será exportado conforme o nome e caminho definidos no campo `arquivo_saida`.

---

## 🔧 Exemplo de `config_local.py`

```python
CONFIG = {
    "largura": 1280,
    "altura": 720,
    "fps": 30,
    "cor_fundo": (0, 0, 0),
    "cor_texto": (255, 255, 255),
    "cor_contorno": (255, 0, 0),
    "espessura_contorno": 3,
    "caminho_fonte": "C:\\Windows\\Fonts\\arialbd.ttf",
    "tamanho_fonte": 120,
    "valores_marcos": [100, 250, 400],
    "texto_unidade_monetaria": "R$",
    "tempo_animacao": 3.0,
    "tempo_pausa": 1.0,
    "tempo_final_extra": 4.0,
    "efeito_piscar_final": True,
    "cores_piscar": [(255, 255, 255), (255, 215, 0), (255, 0, 0)],
    "piscar_por_segundo": 6,
    "tempo_animacao_aleatorio": False,
    "intervalo_tempo_animacao": [3.0, 5.0],
    "fator_inicio_suave": 1.0,
    "fator_fim_suave": 1.0,
    "arquivo_saida": "saida_video.mp4"
}
```

---

## 🧾 Campos de Configuração

| Campo                      | Tipo          | Descrição                             |
| -------------------------- | ------------- | ------------------------------------- |
| `largura`, `altura`        | `int`         | Dimensões do vídeo (px)               |
| `fps`                      | `int`         | Frames por segundo                    |
| `cor_*`                    | `tuple[int]`  | Cores do fundo, texto, contorno (RGB) |
| `espessura_contorno`       | `int`         | Espessura da borda do texto           |
| `caminho_fonte`            | `str`         | Caminho para a fonte `.ttf`           |
| `tamanho_fonte`            | `int`         | Tamanho da fonte                      |
| `valores_marcos`           | `list[int]`   | Valores de contagem                   |
| `texto_unidade_monetaria`  | `str`         | Prefixo monetário                     |
| `tempo_animacao`           | `float`       | Tempo de transição entre valores (s)  |
| `tempo_pausa`              | `float`       | Pausa após cada valor (s)             |
| `tempo_final_extra`        | `float`       | Tempo após o valor final (s)          |
| `efeito_piscar_final`      | `bool`        | Ativar piscar no final?               |
| `cores_piscar`             | `list[tuple]` | Cores usadas no efeito final          |
| `piscar_por_segundo`       | `int`         | Frequência do piscar                  |
| `tempo_animacao_aleatorio` | `bool`        | Tempos variáveis entre valores        |
| `intervalo_tempo_animacao` | `list[float]` | Intervalo de tempo aleatório (s)      |
| `fator_inicio_suave`       | `float`       | Suavidade no início da transição      |
| `fator_fim_suave`          | `float`       | Suavidade no fim da transição         |
| `arquivo_saida`            | `str`         | Nome do arquivo final                 |

---

## ✅ `.gitignore` sugerido

```bash
config_local.py
__pycache__/
*.pyc
*.mp4
```

---

## 🌍 Internacionalização

| Idioma  | Arquivo                        |
| ------- | ------------------------------ |
| 🇧🇷 PT | `README.md`                    |
| 🇺🇸 EN | [`README.en.md`](README.en.md) |

---

🔧 Feito com dedicação por \[Daniwl] — contribuições e sugestões são bem-vindas!