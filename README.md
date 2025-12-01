# SOC Alert Monitoring 🔐  
Pipeline educacional de monitoramento e análise de eventos de segurança, projetado para simular a operação de um SOC (Security Operations Center) em nível júnior.  
O projeto foi estruturado com foco em **detecção de incidentes**, **observabilidade** e **respostas rápidas**, seguindo práticas adotadas em ambientes corporativos.

---

## 🎯 Objetivo Estratégico
Este repositório demonstra minha capacidade de:
- Interpretar logs multiformato (SSH, HTTP e Windows Event).
- Implementar mecanismos de detecção baseados em padrões e volume.
- Automatizar análises operacionais.
- Gerar relatórios acionáveis para tomada de decisão.
- Documentar playbooks de resposta utilizados em operações de segurança.

---

## 🛠️ Funcionalidades Core
| Feature | Descrição |
|--------|-----------|
| 🔎 **Detecção de brute-force** | Identifica tentativas de invasão por SSH usando janelas móveis de tempo. |
| 🌐 **Análise HTTP** | Monitora acessos suspeitos a endpoints sensíveis. |
| 📈 **Atividade anômala** | Detecta IPs com volume acima do baseline. |
| 🧾 **Relatórios SOC** | Geração automática de incident report em Markdown. |
| 📚 **Playbooks** | Procedimentos de resposta estruturados. |

---

## 🧱 Arquitetura do Projeto
- `scripts/generate_logs.py` → Geração de logs simulados  
- `scripts/detector.py` → Motor de detecção de alertas  
- `scripts/report_generator.py` → Composição de relatórios estruturados  
- `logs/` → Saída de logs e relatórios  
- `playbooks/` → Procedimentos operacionais  

---

## 🚀 Como Executar Localmente
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python scripts/generate_logs.py
python scripts/detector.py
python scripts/report_generator.py

## 🗺️ Roadmap – SOC Alert Monitoring

```mermaid
graph LR
  A[🎯 Fase 1 — Fundação do Sistema] --> B[📎 Geração de logs realistas]
  B --> C[🧠 Motor de Detecção (Brute Force, HTTP, Windows)]
  C --> D[📝 Relatórios SOC automatizados]

  D --> E[🎨 Painel Streamlit – Versão 1]
  E --> F[📊 Visualizações Avançadas]

  F --> G[🔍 Threat Intelligence – IP Reputation]
  G --> H[🌐 Integração com APIs externas]

  H --> I[⚙️ CI/CD com GitHub Actions]
  I --> J[🧪 Testes Automáticos + QA]

  J --> K[🚀 Fase Final — Dashboard Completo & Operacional]
