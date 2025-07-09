from config.config_loader import load_config
from src.video.video_generator import gerar_video

if __name__ == "__main__":
    config = load_config()
    gerar_video(config)
