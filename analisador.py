# Projeto: Analisador Automático de Performance de Marketing
# Autora: Cristalwolf Dias
# Objetivo: Processar dados brutos de campanhas e gerar insights estratégicos.

def calcular_kpis(campanhas):
    """
    Recebe uma lista de dicionários (campanhas) e calcula métricas essenciais:
    CTR (Click-Through Rate), CPA (Cost Per Acquisition) e ROI.
    """
    relatorio = []
    
    print(f"--- INICIANDO PROCESSAMENTO DE {len(campanhas)} CAMPANHAS ---\n")

    for campanha in campanhas:
        nome = campanha['nome']
        investimento = campanha['investimento']
        impressoes = campanha['impressoes']
        cliques = campanha['cliques']
        conversoes = campanha['conversoes']
        receita = campanha['receita']

        # Evitar divisão por zero (tratamento de erro básico)
        if impressoes == 0 or cliques == 0:
            print(f"⚠️ Aviso: Dados insuficientes para campanha '{nome}'. Pulando...")
            continue

        # 1. Cálculo de CTR (Taxa de Cliques)
        ctr = (cliques / impressoes) * 100

        # 2. Cálculo de CPA (Custo por Aquisição)
        cpa = investimento / conversoes if conversoes > 0 else 0

        # 3. Cálculo de ROI (Retorno sobre Investimento)
        roi = ((receita - investimento) / investimento) * 100

        # Adicionando dados processados ao relatório
        dados_processados = {
            "Campanha": nome,
            "CTR": f"{ctr:.2f}%",
            "CPA": f"R$ {cpa:.2f}",
            "ROI": f"{roi:.2f}%",
            "Status": "✅ Lucro" if roi > 0 else "🔻 Prejuízo"
        }
        relatorio.append(dados_processados)

    return relatorio

def gerar_dashboard_texto(dados):
    """Imprime um relatório formatado no terminal."""
    print(f"{'CAMPANHA':<20} | {'CTR':<10} | {'ROI':<10} | {'STATUS'}")
    print("-" * 60)
    
    melhor_campanha = None
    maior_roi = -float('inf')

    for item in dados:
        print(f"{item['Campanha']:<20} | {item['CTR']:<10} | {item['ROI']:<10} | {item['Status']}")
        
        # Lógica para encontrar a melhor campanha
        roi_numerico = float(item['ROI'].replace('%', ''))
        if roi_numerico > maior_roi:
            maior_roi = roi_numerico
            melhor_campanha = item['Campanha']

    print("-" * 60)
    print(f"\n🏆 CAMPEÃ DE PERFORMANCE: {melhor_campanha} (ROI: {maior_roi:.2f}%)")

# --- SIMULAÇÃO DE DADOS (O que viria de um CSV ou API) ---
dados_brutos = [
    {"nome": "Black Friday Ads", "investimento": 1000, "impressoes": 50000, "cliques": 2500, "conversoes": 120, "receita": 5000},
    {"nome": "Lançamento App", "investimento": 2000, "impressoes": 100000, "cliques": 1500, "conversoes": 50, "receita": 1500},
    {"nome": "Promoção Relâmpago", "investimento": 500, "impressoes": 10000, "cliques": 800, "conversoes": 40, "receita": 3000},
]

# Execução do Script
if __name__ == "__main__":
    insights = calcular_kpis(dados_brutos)
    gerar_dashboard_texto(insights)
