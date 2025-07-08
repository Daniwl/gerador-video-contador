# 📊 Counter Video Generator

This project generates animated videos that count numerical values up to defined milestones, with smooth animations and visual effects at the end.

## 📦 Requirements

* Python 3.9+
* Windows (or adjusted fonts for Linux/Mac)

### 📅 Install dependencies:

```bash
pip install moviepy pillow numpy
```

## 🚀 How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/gerador-video-contador.git
cd gerador-video-contador
```

2. Create a `config_local.py` file with your preferred settings (see example below). If it doesn't exist, the system will use internal default values.

3. Run the main script:

```bash
python main.py
```

4. The video will be exported using the name and folder specified in `arquivo_saida`.

## 🔧 Example `config_local.py`

```python
CONFIG = {
    "largura": 1280,                         # Video width (px)
    "altura": 720,                           # Video height (px)
    "fps": 30,                               # Frames per second

    "cor_fundo": (0, 0, 0),                 # RGB - Background color
    "cor_texto": (255, 255, 255),           # RGB - Number color
    "cor_contorno": (255, 0, 0),            # RGB - Border color
    "espessura_contorno": 3,               # Border thickness (px)

    "caminho_fonte": "C:\\Windows\\Fonts\\arialbd.ttf",  # Font path
    "tamanho_fonte": 120,                   # Font size (pt)

    "valores_marcos": [100, 250, 400],      # List of values to be displayed
    "texto_unidade_monetaria": "R$",       # Number prefix

    "tempo_animacao": 3.0,                  # Default time between values (s)
    "tempo_pausa": 1.0,                     # Pause after each value (s)
    "tempo_final_extra": 4.0,               # Extra time after final value (s)

    "efeito_piscar_final": True,            # Flash final value?
    "cores_piscar": [(255,255,255), (255,215,0), (255,0,0)],  # Flash colors
    "piscar_por_segundo": 6,               # Flash frequency (times/sec)

    "tempo_animacao_aleatorio": False,      # If True, random time per value
    "intervalo_tempo_animacao": [3.0, 5.0], # Random animation interval (s)

    "fator_suavizacao": 1.0,                # Interpolation smoothing factor (0.2 to 2.0)

    "arquivo_saida": "saida_video.mp4"      # Final video file name
}
```

## 🗒️ CONFIG Field Descriptions

| Field                      | Type          | Unit          | Description                        |
| -------------------------- | ------------- | ------------- | ---------------------------------- |
| `largura` / `altura`       | `int`         | px            | Video dimensions                   |
| `fps`                      | `int`         | frames/second | Frame rate                         |
| `cor_*`                    | `tuple[int]`  | RGB           | Background, text and border colors |
| `espessura_contorno`       | `int`         | px            | Text border thickness              |
| `caminho_fonte`            | `str`         | system path   | Path to .ttf font                  |
| `tamanho_fonte`            | `int`         | pt            | Font size                          |
| `valores_marcos`           | `list[int]`   | currency unit | Values to be counted               |
| `texto_unidade_monetaria`  | `str`         | symbol        | E.g. "R\$", "US\$"                 |
| `tempo_animacao`           | `float`       | seconds       | Default animation duration         |
| `tempo_pausa`              | `float`       | seconds       | Pause after each value             |
| `tempo_final_extra`        | `float`       | seconds       | Time for final effect              |
| `efeito_piscar_final`      | `bool`        | -             | Enables final effect               |
| `cores_piscar`             | `list[tuple]` | RGB           | Colors used in flashing            |
| `piscar_por_segundo`       | `int`         | times/second  | Flashing frequency                 |
| `tempo_animacao_aleatorio` | `bool`        | -             | Enables time variation             |
| `intervalo_tempo_animacao` | `list[float]` | seconds       | Range for random durations         |
| `fator_suavizacao`         | `float`       | no unit       | 0.2 = smoother, 2.0 = faster       |
| `arquivo_saida`            | `str`         | filename      | Name of exported video             |

## 📁 Suggested `.gitignore`

```bash
config_local.py
__pycache__/
*.pyc
*.mp4
```

## 🌐 International Versions

* [`README.en.md`](README.en.md): English version
* [`README.pt.md`](README.pt.md): Portuguese version

---

Made with 💻 by \[Your Name Here] — contributions welcome!
