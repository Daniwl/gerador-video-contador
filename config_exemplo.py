CONFIG = {
    # 🎥 Dimensões do vídeo
    "largura": 1920,
    "altura": 1080,
    "fps": 24,

    # 🎨 Cores
    "cor_fundo": (255, 183, 77),     # Laranja bebê
    "cor_texto": (255, 255, 255),    # Branco
    "cor_contorno": (0, 0, 0),       # Preto
    "espessura_contorno": 2,         # Espessura do contorno (0 = sem contorno)

    # 🅰️ Fonte
    "caminho_fonte": "C:\\Windows\\Fonts\\arialbd.ttf",
    "tamanho_fonte": 200,

    # ⏱️ Tempos de animação
    "tempo_animacao": 3.0,       # Tempo de aceleração entre os marcos
    "tempo_pausa": 1.5,          # Tempo de pausa após atingir o marco
    "tempo_final_extra": 5,      # Tempo extra no final (efeito de vitória)

    # 💰 Valores que serão contados
    #"valores_marcos": [150, 259, 585, 752, 1000],
    "valores_marcos": [1,5,10],

    # ✨ Efeito de "piscar" no final
    "efeito_piscar_final": True,
    "cores_piscar": [
        (255, 255, 255),  # Branco
        (255, 215, 0)    # Dourado
        #(255, 0, 0)       # Vermelho
    ],
    "piscar_por_segundo": 6,

    # 📤 Nome do arquivo final
    "arquivo_saida": "video_contador_configuravel.mp4",
    
    # Textos personalizaveis
    "texto_unidade_monetaria": "R$"
}