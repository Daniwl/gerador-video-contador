import random

def gerar_tempos(config):
    tempos = []
    for _ in config["valores_marcos"]:
        if config.get("tempo_animacao_aleatorio", False):
            anim = random.uniform(*config["intervalo_tempo_animacao"])
        else:
            anim = config["tempo_animacao"]
        tempos.append((anim, config["tempo_pausa"]))
    return tempos

def calcular_valor(t, config, tempos):
    valores = config["valores_marcos"]
    total_duracao_sem_extra = sum(a + p for a, p in tempos)
    valor = 0
    cor = config["cor_texto"]

    if config["efeito_piscar_final"] and t >= total_duracao_sem_extra:
        valor = valores[-1]
        cores = config["cores_piscar"]
        piscar = int(t * config["piscar_por_segundo"]) % len(cores)
        cor = cores[piscar]
    else:
        tempo_acumulado = 0
        for i, (an, pp) in enumerate(tempos):
            inicio = tempo_acumulado
            fim_anim = inicio + an
            fim_total = fim_anim + pp
            tempo_acumulado = fim_total

            if inicio <= t < fim_anim:
                v_ini = 0 if i == 0 else valores[i - 1]
                v_fim = valores[i]
                progresso = (t - inicio) / an

                fi = config.get("fator_inicio_suave", 1.0)
                ff = config.get("fator_fim_suave", 1.0)
                curva = progresso**fi * (1 - (1 - progresso)**ff)

                valor = v_ini + (v_fim - v_ini) * curva
                break
            elif fim_anim <= t < fim_total:
                valor = valores[i]
                break
            elif t >= fim_total:
                valor = valores[i]

    texto = f"{config['texto_unidade_monetaria']} {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return texto, cor
