from PIL import Image, ImageDraw, ImageFont
from functools import lru_cache

@lru_cache(maxsize=512)
def gerar_imagem_texto(texto, caminho_fonte, tamanho_fonte, espessura, cor_contorno, cor_texto):
    fonte = ImageFont.truetype(caminho_fonte, tamanho_fonte)
    img_temp = Image.new("RGBA", (1, 1))
    draw_temp = ImageDraw.Draw(img_temp)
    bbox = draw_temp.textbbox((0, 0), texto, font=fonte)
    largura, altura = bbox[2] - bbox[0], bbox[3] - bbox[1]

    img = Image.new("RGBA", (largura, altura), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if espessura > 0:
        for dx in range(-espessura, espessura + 1):
            for dy in range(-espessura, espessura + 1):
                if dx != 0 or dy != 0:
                    draw.text((dx, dy), texto, font=fonte, fill=cor_contorno)

    draw.text((0, 0), texto, font=fonte, fill=cor_texto)
    return img
