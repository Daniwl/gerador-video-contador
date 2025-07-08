import numpy as np
from moviepy import VideoClip, ColorClip
from PIL import Image, ImageDraw, ImageFont
from functools import lru_cache

try:
    from config_local import CONFIG
except ImportError:
    CONFIG = {}

# ============================
# 🔧 CONFIGURAÇÕES PADRÃO (usadas se não definidas em config_local.py)
# ============================
DEFAULT_CONFIG = {
    "largura": 1920,
    "altura": 1080,
    "fps": 24,
    "cor_fundo": (255, 183, 77),
    "cor_texto": (255, 255, 255),
    "cor_contorno": (0, 0, 0),
    "espessura_contorno": 2,
    "caminho_fonte": "C:\\Windows\\Fonts\\arialbd.ttf",
    "tamanho_fonte": 200,
    "tempo_animacao": 3.0,
    "tempo_pausa": 1.5,
    "tempo_final_extra": 5,
    "valores_marcos": [1, 5, 10],
    "efeito_piscar_final": True,
    "cores_piscar": [(255, 255, 255), (255, 215, 0)],
    "piscar_por_segundo": 6,
    "arquivo_saida": "video_contador_configuravel.mp4",
    "texto_unidade_monetaria": "R$"
}

# Substitui valores ausentes no CONFIG pelos padrões
for chave, valor in DEFAULT_CONFIG.items():
    CONFIG.setdefault(chave, valor)

FUNDO_BASE = ColorClip(size=(CONFIG["largura"], CONFIG["altura"]),
                       color=CONFIG["cor_fundo"]).get_frame(0)

@lru_cache(maxsize=512)
def gerar_imagem_texto(texto, cor_texto_dinamica=None):
    fonte = ImageFont.truetype(CONFIG["caminho_fonte"], CONFIG["tamanho_fonte"])
    img_temp = Image.new("RGBA", (1, 1))
    draw_temp = ImageDraw.Draw(img_temp)
    bbox = draw_temp.textbbox((0, 0), texto, font=fonte)
    largura, altura = bbox[2] - bbox[0], bbox[3] - bbox[1]

    img = Image.new("RGBA", (largura, altura), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    espessura = CONFIG["espessura_contorno"]
    cor_contorno = CONFIG["cor_contorno"]
    cor_texto = cor_texto_dinamica or CONFIG["cor_texto"]

    if espessura > 0:
        for dx in range(-espessura, espessura + 1):
            for dy in range(-espessura, espessura + 1):
                if dx != 0 or dy != 0:
                    draw.text((dx, dy), texto, font=fonte, fill=cor_contorno)

    draw.text((0, 0), texto, font=fonte, fill=cor_texto)
    return img

def calcular_valor(t):
    anim = CONFIG["tempo_animacao"]
    pausa = CONFIG["tempo_pausa"]
    valores = CONFIG["valores_marcos"]
    tempo_extra_final = CONFIG["tempo_final_extra"]
    faixa_total = anim + pausa

    total_duracao_sem_extra = len(valores) * faixa_total
    duracao_total = total_duracao_sem_extra + tempo_extra_final

    valor = 0
    cor_piscar = CONFIG["cor_texto"]

    if CONFIG["efeito_piscar_final"] and t >= total_duracao_sem_extra:
        valor = valores[-1]
        cores = CONFIG["cores_piscar"]
        indice = int(t * CONFIG["piscar_por_segundo"]) % len(cores)
        cor_piscar = cores[indice]
    else:
        for i, alvo in enumerate(valores):
            t_inicio = i * faixa_total
            t_fim_anim = t_inicio + anim
            t_fim_total = t_fim_anim + pausa

            if t_inicio <= t < t_fim_anim:
                inicio = 0 if i == 0 else valores[i - 1]
                progresso = (t - t_inicio) / anim
                fator = 3 * progresso**2 - 2 * progresso**3
                valor = inicio + (alvo - inicio) * fator
                break
            elif t_fim_anim <= t < t_fim_total:
                valor = alvo
                break
            elif t >= t_fim_total:
                valor = alvo

    texto_formatado = f"{CONFIG['texto_unidade_monetaria']} {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return texto_formatado, cor_piscar

def gerar_frame(t):
    largura = CONFIG["largura"]
    altura = CONFIG["altura"]
    frame = FUNDO_BASE.copy()

    texto, cor_dinamica = calcular_valor(t)
    imagem_texto = gerar_imagem_texto(texto, tuple(cor_dinamica))
    img_np = np.array(imagem_texto)

    x = (largura - imagem_texto.width) // 2
    y = (altura - imagem_texto.height) // 2

    alpha = img_np[..., 3] / 255.0
    for c in range(3):
        frame[y:y+imagem_texto.height, x:x+imagem_texto.width, c] = (
            alpha * img_np[..., c] + (1 - alpha) * frame[y:y+imagem_texto.height, x:x+imagem_texto.width, c]
        ).astype(np.uint8)

    return frame

def gerar_video():
    total_marcos = len(CONFIG["valores_marcos"])
    tempo_base = total_marcos * (CONFIG["tempo_animacao"] + CONFIG["tempo_pausa"])
    duracao_total = tempo_base + CONFIG["tempo_final_extra"]

    print("🔧 Gerando vídeo com duração:", duracao_total, "segundos...")

    video = VideoClip(gerar_frame, duration=duracao_total)
    video.write_videofile(CONFIG["arquivo_saida"], fps=CONFIG["fps"],
                          threads=4, preset='ultrafast')
    print("✅ Vídeo exportado:", CONFIG["arquivo_saida"])

if __name__ == "__main__":
    gerar_video()
