# Gerador de Vídeo Contador 🎞️

Este projeto cria vídeos animados que contam valores numéricos até marcos definidos, com animações suaves e efeitos visuais no final.

## 📦 Requisitos

* Python 3.9+
* As bibliotecas abaixo (instale com o comando abaixo):

```bash
pip install moviepy pillow numpy
```

## 🚀 Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/gerador-video-contador.git
cd gerador-video-contador
```

2. Crie um arquivo chamado `config_local.py` na raiz, com as configurações desejadas (veja exemplo abaixo).

3. Execute o script principal:

```bash
python nome_do_arquivo.py
```

4. O vídeo será gerado conforme suas configurações no arquivo `config_local.py`.

## 🛠️ Exemplo de `config_local.py`

```python
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
    "valores_marcos": [150, 259, 585, 752, 1000],
    "efeito_piscar_final": True,
    "cores_piscar": [(255, 255, 255), (255, 215, 0)],
    "piscar_por_segundo": 6,
    "arquivo_saida": "video_final.mp4",
    "texto_unidade_monetaria": "R$"
}
```

> ⚠️ Este arquivo **não será versionado**, pois está no `.gitignore`. Isso permite personalizações locais sem afetar o projeto principal.

## 📊 Descrição dos Campos do `CONFIG`

| Campo                     | Tipo          | Unidade             | Descrição                                            |
| ------------------------- | ------------- | ------------------- | ---------------------------------------------------- |
| `largura`                 | `int`         | pixels              | Largura do vídeo                                     |
| `altura`                  | `int`         | pixels              | Altura do vídeo                                      |
| `fps`                     | `int`         | quadros por segundo | Taxa de quadros por segundo (frames per second)      |
| `cor_fundo`               | `tuple`       | RGB                 | Cor de fundo do vídeo                                |
| `cor_texto`               | `tuple`       | RGB                 | Cor principal do texto                               |
| `cor_contorno`            | `tuple`       | RGB                 | Cor do contorno do texto                             |
| `espessura_contorno`      | `int`         | pixels              | Espessura do contorno do texto                       |
| `caminho_fonte`           | `str`         | caminho do sistema  | Caminho absoluto da fonte `.ttf`                     |
| `tamanho_fonte`           | `int`         | pontos              | Tamanho da fonte                                     |
| `tempo_animacao`          | `float`       | segundos            | Tempo para animar até o próximo valor                |
| `tempo_pausa`             | `float`       | segundos            | Pausa entre animações                                |
| `tempo_final_extra`       | `float`       | segundos            | Tempo extra com efeito de piscar após o último valor |
| `valores_marcos`          | `list[int]`   | unidade monetária   | Lista com os valores a serem animados                |
| `efeito_piscar_final`     | `bool`        | -                   | Se verdadeiro, ativa o efeito de piscar no final     |
| `cores_piscar`            | `list[tuple]` | RGB                 | Lista de cores alternadas no efeito de piscar        |
| `piscar_por_segundo`      | `int`         | vezes por segundo   | Frequência da troca de cores no efeito de piscar     |
| `arquivo_saida`           | `str`         | nome do arquivo     | Nome do vídeo final exportado                        |
| `texto_unidade_monetaria` | `str`         | símbolo             | Prefixo do valor (ex: R\$, US\$, etc)                |

## 🌐 International README

English version is available at [`README.en.md`](README.en.md)

---

## 🧾 Licença

MIT. Livre para uso e modificação.
