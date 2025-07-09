import numpy as np
from moviepy import ColorClip
from src.animation.calculator import calcular_valor
from src.rendering.text_renderer import gerar_imagem_texto

def criar_fundo(config):
    return ColorClip(size=(config["largura"], config["altura"]),
                     color=config["cor_fundo"]).get_frame(0)

def gerar_frame(t, fundo, config, tempos):
    frame = fundo.copy()
    texto, cor = calcular_valor(t, config, tempos)
    img_txt = gerar_imagem_texto(
        texto,
        config["caminho_fonte"],
        config["tamanho_fonte"],
        config["espessura_contorno"],
        config["cor_contorno"],
        cor
    )

    np_img = np.array(img_txt)

    x = (config["largura"] - img_txt.width) // 2
    y = (config["altura"] - img_txt.height) // 2

    alpha = np_img[..., 3] / 255.0
    for c in range(3):
        frame[y:y+img_txt.height, x:x+img_txt.width, c] = (
            alpha * np_img[..., c] + (1 - alpha) * frame[y:y+img_txt.height, x:x+img_txt.width, c]
        ).astype(np.uint8)

    return frame
