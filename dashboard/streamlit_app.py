import streamlit as st
import pandas as pd
import json
from pathlib import Path
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="SOC Alert Monitoring", layout="wide")

ROOT = Path(__file__).parent.parent
ALERTS_FILE = ROOT / "logs" / "alerts.json"
LOG_FILE = ROOT / "logs" / "generated_logs.log"

st.title("SOC Alert Monitoring — Painel Operacional (Júnior)")

col1, col2 = st.columns([3,1])

with col2:
    st.markdown("### Controles")
    if st.button("Recarregar dados"):
        st.experimental_rerun()
    st.markdown("Filtro rápido:")
    tipo_filter = st.multiselect("Tipo de alerta", options=["brute_force","suspicious_http","high_activity","windows_logon_failure"], default=[])
    ip_filter = st.text_input("IP (substring)")

# Load alerts
def load_alerts():
    if not ALERTS_FILE.exists():
        return pd.DataFrame()
    try:
        with open(ALERTS_FILE, "r", encoding="utf-8") as f:
            alerts = json.load(f)
    except Exception as e:
        st.error(f"Erro ao carregar {ALERTS_FILE}: {e}")
        return pd.DataFrame()

    # Normalize to DataFrame
    rows = []
    for a in alerts:
        rows.append({
            "type": a.get("type"),
            "ip": a.get("ip", a.get("host", "-")),
            "severity": ("High" if a.get("type")=="brute_force" else "Medium" if a.get("type") in ("suspicious_http","high_activity") else "Low"),
            "description": a.get("description", a.get("raw", a.get("msg", "-"))),
            "raw": json.dumps(a)
        })
    df = pd.DataFrame(rows)
    return df

df = load_alerts()

st.markdown("## Resumo Rápido")
if df.empty:
    st.info("Nenhum alerta detectado. Execute o detector (`python scripts/detector.py`) e gere alerts.json.")
else:
    total = len(df)
    by_type = df['type'].value_counts().to_dict()
    colA, colB, colC = st.columns(3)
    colA.metric("Total de alertas", total)
    colB.metric("Tipos distintos", len(by_type))
    colC.metric("IPs distintos", df['ip'].nunique())

    # Apply filters
    if tipo_filter:
        df = df[df['type'].isin(tipo_filter)]
    if ip_filter:
        df = df[df['ip'].str.contains(ip_filter, na=False)]

    st.markdown("### Distribuição por tipo")
    fig1 = px.bar(x=list(df['type'].value_counts().index), y=list(df['type'].value_counts().values), labels={'x':'Tipo','y':'Contagem'})
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("### Atividade por IP (Top 10)")
    ip_counts = df['ip'].value_counts().reset_index()
    ip_counts.columns = ['ip','count']
    fig2 = px.bar(ip_counts.head(10), x='ip', y='count', labels={'count':'Eventos','ip':'IP'})
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Tabela de alertas")
    st.dataframe(df[['type','ip','severity','description']].reset_index(drop=True), use_container_width=True)

    with st.expander("Visualizar alertas raw (JSON)"):
        for i, row in df.iterrows():
            st.code(row['raw'])

# Optional: show tail of logs for context
st.markdown("---")
st.markdown("### Contexto de logs (últimas 200 linhas)")
if LOG_FILE.exists():
    try:
        tail = LOG_FILE.read_text(encoding="utf-8").splitlines()[-200:]
        st.text("\n".join(tail))
    except Exception as e:
        st.error(f"Não foi possível ler {LOG_FILE}: {e}")
else:
    st.info("Arquivo de logs não encontrado. Rode `python scripts/generate_logs.py` para criar.")
