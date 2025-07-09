from moviepy import VideoClip
from src.animation.calculator import gerar_tempos
from src.rendering.frame_generator import gerar_frame, criar_fundo

def gerar_video(config):
    tempos = gerar_tempos(config)
    fundo = criar_fundo(config)
    duracao_total = sum(an + pp for an, pp in tempos) + config["tempo_final_extra"]
    video = VideoClip(lambda t: gerar_frame(t, fundo, config, tempos), duration=duracao_total)
    video.write_videofile(config["arquivo_saida"], fps=config["fps"], threads=4, preset='ultrafast')
    print(f"✅ Vídeo salvo como: {config['arquivo_saida']}")
