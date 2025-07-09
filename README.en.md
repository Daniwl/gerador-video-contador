# 📊 Video Counter Generator

A Python-based system that generates animated videos counting up to specified milestones, with smooth transitions and optional final effects.

---

## 📁 Project Structure

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

## 📦 Requirements

* Python 3.9+
* Windows (or adjust the font path for Linux/Mac)

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/video_counter_system.git
cd video_counter_system
```

2. *(Optional)* Create a `config_local.py` file in the root folder to override default settings.
   If not provided, the defaults from `config/default_config.py` will be used.

3. Run the generator:

```bash
python main.py
```

4. The video will be exported with the name and path specified in `arquivo_saida`.

---

## 🔧 Example `config_local.py`

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
    "arquivo_saida": "output_video.mp4"
}
```

---

## 🧾 Configuration Fields

| Field                      | Type          | Description                                     |
| -------------------------- | ------------- | ----------------------------------------------- |
| `largura`, `altura`        | `int`         | Video resolution in pixels                      |
| `fps`                      | `int`         | Frames per second                               |
| `cor_*`                    | `tuple[int]`  | RGB values for background, text, and outline    |
| `espessura_contorno`       | `int`         | Text outline thickness                          |
| `caminho_fonte`            | `str`         | Path to `.ttf` font file                        |
| `tamanho_fonte`            | `int`         | Font size in points                             |
| `valores_marcos`           | `list[int]`   | Milestone values to animate                     |
| `texto_unidade_monetaria`  | `str`         | Currency or unit prefix (e.g., `"R$"`, `"US$"`) |
| `tempo_animacao`           | `float`       | Animation duration per milestone (seconds)      |
| `tempo_pausa`              | `float`       | Pause duration after each value (seconds)       |
| `tempo_final_extra`        | `float`       | Extra duration after the last value (seconds)   |
| `efeito_piscar_final`      | `bool`        | Enable blinking effect at final value           |
| `cores_piscar`             | `list[tuple]` | RGB colors used for blinking                    |
| `piscar_por_segundo`       | `int`         | Blinking frequency (times per second)           |
| `tempo_animacao_aleatorio` | `bool`        | Enable random animation duration per value      |
| `intervalo_tempo_animacao` | `list[float]` | Range for random duration (seconds)             |
| `fator_inicio_suave`       | `float`       | Smoothing factor at the start                   |
| `fator_fim_suave`          | `float`       | Smoothing factor at the end                     |
| `arquivo_saida`            | `str`         | Output video filename                           |

---

## ✅ Suggested `.gitignore`

```bash
config_local.py
__pycache__/
*.pyc
*.mp4
```

---

## 🌍 Multilingual Support

| Language | File           |
| -------- | -------------- |
| 🇧🇷 PT  | `README.md`    |
| 🇺🇸 EN  | `README.en.md` |

---

🛠️ Built with 💻 by \[Daniwl] — contributions are welcome!