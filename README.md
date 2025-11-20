# 📊 Marketing Data Automator

> Uma ferramenta Python para processar dados brutos de campanhas e gerar insights estratégicos automaticamente.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Finalizado-success?style=for-the-badge)

## 🎯 O Problema
No dia a dia de Marketing Digital, analistas perdem horas calculando métricas manualmente em planilhas (Excel), o que gera gargalos operacionais e risco de erro humano.

## 💡 A Solução
Desenvolvi este script para automatizar a ingestão de dados de campanhas e o cálculo instantâneo de KPIs críticos. O algoritmo processa listas de dados e devolve um dashboard via terminal com as melhores performances.

## ⚙️ Funcionalidades
- **Cálculo de CTR (Click-Through Rate):** Mede a atratividade do anúncio.
- **Cálculo de CPA (Cost Per Acquisition):** Monitora a eficiência do investimento.
- **Cálculo de ROI (Return on Investment):** Identifica lucro ou prejuízo real.
- **Ranking Automático:** O script compara as campanhas e elege a "Campeã de Performance" baseada no ROI.
- **Tratamento de Erros:** O código previne falhas comuns como divisão por zero em campanhas sem impressões.

## 🚀 Como Rodar
Você não precisa instalar nenhuma biblioteca externa, apenas o Python nativo.

1. Clone este repositório:
```bash
git clone https://github.com/cristalwolfff/marketing-data-automator.git
```

2. Entre na pasta:
```bash
cd marketing-data-automator
```

3. Execute o script:
```bash
python analisador.py
```

##📸 Exemplo de Saída
```Plaintext

--- INICIANDO PROCESSAMENTO DE 3 CAMPANHAS ---

CAMPANHA             | CTR        | ROI        | STATUS
------------------------------------------------------------
Black Friday Ads     | 5.00%      | 400.00%    | ✅ Lucro
Lançamento App       | 1.50%      | -25.00%    | 🔻 Prejuízo
Promoção Relâmpago   | 8.00%      | 500.00%    | ✅ Lucro
------------------------------------------------------------

🏆 CAMPEÃ DE PERFORMANCE: Promoção Relâmpago (ROI: 500.00%)
```

## 🛠️ Tecnologias Utilizadas
* Python 3: Estruturas de dados (Listas/Dicionários), Funções, F-Strings e Lógica Condicional.
* Lógica de Negócio: Modelagem de fórmulas financeiras aplicadas ao Marketing.

## Desenvolvido por Cristalwolf Dias 🐺
