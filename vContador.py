import numpy as np
from moviepy import VideoClip, ColorClip
from PIL import Image, ImageDraw, ImageFont
from functools import lru_cache
import random
import os

# Carrega config externo se existir
if os.path.exists("config_local.py"):
    from config_local import CONFIG
else:
    CONFIG = {
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
        "texto_unidade_monetaria": "R$",
        "tempo_animacao_aleatorio": False,
        "intervalo_tempo_animacao": [2.0, 4.0],
        "fator_inicio_suave": 1.0,
        "fator_fim_suave": 1.0,
    }

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

# Pré-processa tempos por marco (caso aleatório esteja ativado)
TEMPOS_ANIMACAO = []
faixa_padrao = CONFIG["tempo_animacao"] + CONFIG["tempo_pausa"]

for _ in CONFIG["valores_marcos"]:
    if CONFIG.get("tempo_animacao_aleatorio", False):
        anim = random.uniform(*CONFIG["intervalo_tempo_animacao"])
    else:
        anim = CONFIG["tempo_animacao"]
    TEMPOS_ANIMACAO.append((anim, CONFIG["tempo_pausa"]))

def calcular_valor(t):
    valores = CONFIG["valores_marcos"]
    tempo_extra = CONFIG["tempo_final_extra"]
    total_duracao_sem_extra = sum(a + p for a, p in TEMPOS_ANIMACAO)
    valor = 0
    cor = CONFIG["cor_texto"]

    if CONFIG["efeito_piscar_final"] and t >= total_duracao_sem_extra:
        valor = valores[-1]
        cores = CONFIG["cores_piscar"]
        piscar = int(t * CONFIG["piscar_por_segundo"]) % len(cores)
        cor = cores[piscar]
    else:
        tempo_acumulado = 0
        for i, (an, pp) in enumerate(TEMPOS_ANIMACAO):
            inicio = tempo_acumulado
            fim_anim = inicio + an
            fim_total = fim_anim + pp
            tempo_acumulado = fim_total

            if inicio <= t < fim_anim:
                v_ini = 0 if i == 0 else valores[i - 1]
                v_fim = valores[i]
                progresso = (t - inicio) / an

                fi = CONFIG.get("fator_inicio_suave", 1.0)
                ff = CONFIG.get("fator_fim_suave", 1.0)
                curva = progresso**fi * (1 - (1 - progresso)**ff)

                valor = v_ini + (v_fim - v_ini) * curva
                break
            elif fim_anim <= t < fim_total:
                valor = valores[i]
                break
            elif t >= fim_total:
                valor = valores[i]

    texto = f"{CONFIG['texto_unidade_monetaria']} {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return texto, cor

def gerar_frame(t):
    frame = FUNDO_BASE.copy()
    texto, cor = calcular_valor(t)
    img_txt = gerar_imagem_texto(texto, cor)
    np_img = np.array(img_txt)

    x = (CONFIG["largura"] - img_txt.width) // 2
    y = (CONFIG["altura"] - img_txt.height) // 2

    alpha = np_img[..., 3] / 255.0
    for c in range(3):
        frame[y:y+img_txt.height, x:x+img_txt.width, c] = (
            alpha * np_img[..., c] + (1 - alpha) * frame[y:y+img_txt.height, x:x+img_txt.width, c]
        ).astype(np.uint8)

    return frame

def gerar_video():
    duracao_total = sum(an + pp for an, pp in TEMPOS_ANIMACAO) + CONFIG["tempo_final_extra"]
    video = VideoClip(gerar_frame, duration=duracao_total)
    video.write_videofile(CONFIG["arquivo_saida"], fps=CONFIG["fps"], threads=4, preset='ultrafast')
    print(f"✅ Vídeo salvo como: {CONFIG['arquivo_saida']}")

if __name__ == "__main__":
    gerar_video()
