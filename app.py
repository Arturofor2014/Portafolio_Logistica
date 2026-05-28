import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.set_page_config(page_title="Portafolio · Arturo Aguilar", layout="wide", page_icon="🚚",
                   initial_sidebar_state="expanded")

st.markdown("""
<style>
  /* Fondo blanco general */
  .stApp { background-color: #ffffff; }

  /* Hero card */
  .hero-box {
    background: #ffffff;
    border: 1px solid #e0e7f0;
    border-radius: 16px;
    padding: 44px 52px;
    color: #1a1a2e;
    box-shadow: 0 2px 16px rgba(0,0,0,.06);
  }
  .hero-box .eyebrow {
    font-size: 12px; color: #4D93D9; letter-spacing: 2px;
    text-transform: uppercase; margin-bottom: 10px;
  }
  .hero-box h1 {
    font-size: 36px; font-weight: 900; margin: 0 0 6px 0; letter-spacing: .5px; color: #1a1a2e;
  }
  .hero-box h1 span { color: #4D93D9; }
  .hero-box .role {
    font-size: 15px; color: #4D93D9; font-weight: 700;
    letter-spacing: 1px; margin-bottom: 20px;
  }
  .hero-box .bio {
    font-size: 15px; color: #444; line-height: 1.75;
    max-width: 820px; margin-bottom: 26px;
  }
  .tags { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 28px; }
  .tag {
    background: rgba(77,147,217,.18); border: 1px solid #4D93D9;
    color: #4D93D9; font-size: 12px; font-weight: 700;
    padding: 5px 14px; border-radius: 20px;
  }
  .tag-ai {
    background: rgba(46,204,113,.15); border: 1px solid #2ECC71;
    color: #2ECC71; font-size: 12px; font-weight: 700;
    padding: 5px 14px; border-radius: 20px;
  }
  .kpi-row { display: flex; gap: 40px; flex-wrap: wrap; }
  .kpi-item { text-align: center; }
  .kpi-num { font-size: 32px; font-weight: 900; color: #4D93D9; line-height: 1; }
  .kpi-lbl { font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }

  /* Separador de sección */
  .sec-title { font-size: 22px; font-weight: 800; color: #1a1a2e; margin-bottom: 4px; }
  .sec-sub { font-size: 13px; color: #888; margin-bottom: 20px; }

  @media(max-width: 768px) {
    .hero-box { padding: 24px 20px; }
    .hero-box h1 { font-size: 26px; }
    .kpi-row {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      text-align: center;
    }
    .kpi-item { width: 100%; }
    .kpi-num { font-size: 26px; }
  }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
st.sidebar.markdown("### 👤 Arturo Aguilar")
st.sidebar.caption("Senior Commercial & Financial Analytics Engineer · 7+ años")
st.sidebar.divider()
st.sidebar.markdown("**Navegación:**")

proyecto = st.sidebar.radio("Sección", [
    "🏠  Presentación",
    "1 · KPIs de Flota",
    "2 · Desempeño Proveedores",
    "3 · Rentabilidad por Ruta",
    "4 · Predicción de Demanda",
    "5 · Detección de Anomalías",
    "6 · Optimización de Rutas",
    "7 · Pipeline ETL",
    "8 · Reportes Automáticos",
    "9 · Costo-Servicio",
])

st.sidebar.divider()
st.sidebar.caption("🤖 Desarrollado con apoyo de IA")

components.html("""
<script>
  window.addEventListener('load', function() {
    setTimeout(function() {
      var btn = window.parent.document.querySelector('[data-testid="collapsedControl"]');
      if (btn) btn.click();
    }, 300);
  });
</script>
""", height=0)

st.divider()

# ── 0 · PRESENTACIÓN ──────────────────────────────────────────────────────────
if proyecto == "🏠  Presentación":
    st.markdown("""
    <div class="hero-box">
      <div class="eyebrow">Portafolio de Proyectos · Data Analytics & Logística</div>
      <h1>Arturo <span>Aguilar</span></h1>
      <div class="role">Senior Commercial & Financial Analytics Engineer</div>
      <p class="bio">
        Más de <strong style="color:#1a1a2e">7 años</strong> de experiencia liderando proyectos analíticos de alto impacto,
        tanto en <strong style="color:#1a1a2e">iniciativas propias</strong> como dentro de empresas de logística, transporte
        y cadena de suministro. Convierto datos operativos en decisiones que
        <strong style="color:#1a1a2e">reducen costos, mejoran el nivel de servicio y generan ventaja competitiva real.</strong>
        Me apoyo estratégicamente en <strong style="color:#2ECC71">Inteligencia Artificial</strong> para acelerar el
        desarrollo de soluciones, reducir tiempos de entrega y elevar la calidad de cada análisis.
      </p>
      <div class="tags">
        <span class="tag">📊 Senior Data Analyst</span>
        <span class="tag">🚚 Logística & Supply Chain</span>
        <span class="tag">🐍 Python · SQL · Power BI</span>
        <span class="tag">🏗️ Proyectos propios & corporativos</span>
        <span class="tag-ai">🤖 Potenciado con IA</span>
      </div>
      <div class="kpi-row">
        <div class="kpi-item">
          <div class="kpi-num">7+</div>
          <div class="kpi-lbl">Experiencia en Análisis de Datos</div>
        </div>
        <div class="kpi-item">
          <div class="kpi-num">9</div>
          <div class="kpi-lbl">Proyectos en portafolio</div>
        </div>
        <div class="kpi-item">
          <div class="kpi-num">3x</div>
          <div class="kpi-lbl">Velocidad con IA</div>
        </div>
        <div class="kpi-item">
          <div class="kpi-num">↑</div>
          <div class="kpi-lbl">Orientado a impacto</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Selecciona un proyecto en el menú lateral para explorar los análisis.")

# ── 1 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "1 · KPIs de Flota":
    st.markdown('<div class="sec-title">📊 Dashboard de KPIs de Flota</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Métricas operativas diarias de la flota de transporte</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Entregas hoy", "142", "+8")
    c2.metric("Tiempo promedio", "2.4 h", "-0.3 h")
    c3.metric("Costo por entrega", "$12.80", "-$0.50")
    c4.metric("Nivel de servicio", "97.2%", "+1.1%")

    dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
    df = pd.DataFrame({"Día": dias, "Entregas": [120, 135, 110, 142, 158, 95]})
    st.bar_chart(df.set_index("Día"))

# ── 2 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "2 · Desempeño Proveedores":
    st.markdown('<div class="sec-title">🏭 Monitor de Desempeño de Proveedores</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Scorecard de nivel de servicio y cumplimiento SLA</div>', unsafe_allow_html=True)

    df = pd.DataFrame({
        "Proveedor":           ["Logitrans", "FastCargo", "MovilExpress", "CargoPlus"],
        "Entregas a Tiempo %": [96, 88, 92, 79],
        "SLA Cumplido %":      [98, 85, 90, 75],
        "Incidencias":         [3, 12, 7, 18],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.line_chart(df.set_index("Proveedor")[["Entregas a Tiempo %", "SLA Cumplido %"]])

# ── 3 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "3 · Rentabilidad por Ruta":
    st.markdown('<div class="sec-title">💰 Rentabilidad por Ruta y Cliente</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Análisis de margen por corredor logístico</div>', unsafe_allow_html=True)

    rutas = ["Norte", "Sur", "Este", "Oeste", "Centro"]
    df = pd.DataFrame({
        "Ruta":         rutas,
        "Ingresos ($)": [45000, 32000, 28000, 51000, 38000],
        "Costos ($)":   [31000, 24000, 22000, 33000, 27000],
    })
    df["Margen ($)"] = df["Ingresos ($)"] - df["Costos ($)"]
    df["Margen %"]   = (df["Margen ($)"] / df["Ingresos ($)"] * 100).round(1)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.bar_chart(df.set_index("Ruta")["Margen %"])

# ── 4 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "4 · Predicción de Demanda":
    st.markdown('<div class="sec-title">🤖 Predicción de Demanda</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Modelo de forecasting sobre histórico semanal de entregas</div>', unsafe_allow_html=True)

    semanas = list(range(1, 13))
    real = [200, 210, 195, 230, 225, 240, 255, 245, 260, 270, 265, 280]
    pred = [205, 208, 200, 225, 228, 238, 252, 248, 258, 272, 268, 278]
    df = pd.DataFrame({"Semana": semanas, "Real": real, "Predicción": pred})
    st.line_chart(df.set_index("Semana"))
    st.caption("Modelo: regresión lineal simple · Error promedio: 3.1 unidades")

# ── 5 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "5 · Detección de Anomalías":
    st.markdown('<div class="sec-title">🚨 Detector de Anomalías en Operaciones</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Identifica entregas con tiempos fuera del rango esperado</div>', unsafe_allow_html=True)

    np.random.seed(7)
    tiempos = np.random.normal(loc=2.5, scale=0.3, size=50).tolist()
    tiempos[15] = 6.2
    tiempos[32] = 5.8
    df = pd.DataFrame({"Entrega": range(1, 51), "Tiempo (h)": tiempos})
    umbral = 2.5 + 2 * 0.3
    df["Anomalía"] = df["Tiempo (h)"] > umbral
    st.line_chart(df.set_index("Entrega")["Tiempo (h)"])
    anomalias = df[df["Anomalía"]]
    st.error(f"⚠️ {len(anomalias)} entregas con tiempo anómalo detectadas")
    st.dataframe(anomalias[["Entrega", "Tiempo (h)"]], hide_index=True)

# ── 6 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "6 · Optimización de Rutas":
    st.markdown('<div class="sec-title">🗺️ Optimización de Rutas de Entrega</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Comparativa de rutas por costo, tiempo y distancia</div>', unsafe_allow_html=True)

    df = pd.DataFrame({
        "Origen":           ["CDMX", "CDMX", "CDMX", "CDMX"],
        "Destino":          ["Monterrey", "Guadalajara", "Puebla", "Querétaro"],
        "Distancia (km)":   [940, 540, 130, 210],
        "Tiempo est. (h)":  [9.5, 5.2, 1.5, 2.1],
        "Costo ($)":        [1800, 1100, 350, 480],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    mejor = df.loc[df["Costo ($)"].idxmin()]
    st.success(f"✅ Ruta más eficiente: {mejor['Origen']} → {mejor['Destino']} — ${mejor['Costo ($)']}")

# ── 7 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "7 · Pipeline ETL":
    st.markdown('<div class="sec-title">🔄 Pipeline ETL de Datos de Transporte</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Flujo automatizado: Fuente → Limpieza → Transformación → Data Warehouse</div>', unsafe_allow_html=True)

    pasos = {
        "Paso":        ["1 · Extracción", "2 · Limpieza", "3 · Transformación", "4 · Carga"],
        "Descripción": [
            "Leer CSV / API de TMS",
            "Eliminar nulos y duplicados",
            "Calcular KPIs y agregar por ruta",
            "Guardar en Data Warehouse",
        ],
        "Estado":    ["✅ OK", "✅ OK", "✅ OK", "✅ OK"],
        "Registros": [5000, 4873, 4873, 4873],
    }
    st.dataframe(pd.DataFrame(pasos), use_container_width=True, hide_index=True)
    st.info("Última ejecución: 2026-05-27 09:00 · Duración: 42 seg · Sin errores")

# ── 8 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "8 · Reportes Automáticos":
    st.markdown('<div class="sec-title">📧 Automatización de Reportes Operativos</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Reportes programados sin intervención manual</div>', unsafe_allow_html=True)

    config = {
        "Reporte":       ["Reporte semanal flota", "SLA proveedores", "Costos por ruta"],
        "Frecuencia":    ["Cada lunes 8:00",        "Cada viernes 17:00", "Día 1 de cada mes"],
        "Destinatarios": ["gerencia@empresa.com",   "ops@empresa.com",    "finanzas@empresa.com"],
        "Formato":       ["Excel + PDF",            "PDF",                "Excel"],
        "Estado":        ["✅ Activo",              "✅ Activo",          "✅ Activo"],
    }
    st.dataframe(pd.DataFrame(config), use_container_width=True, hide_index=True)
    if st.button("▶ Generar reporte ahora (simulado)"):
        st.success("Reporte generado y enviado a gerencia@empresa.com")

# ── 9 ─────────────────────────────────────────────────────────────────────────
elif proyecto == "9 · Costo-Servicio":
    st.markdown('<div class="sec-title">⚖️ Análisis Costo-Servicio en Cadena de Suministro</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Simula el impacto económico de cambiar el nivel de servicio objetivo</div>', unsafe_allow_html=True)

    nivel = st.slider("Nivel de servicio objetivo (%)", 85, 99, 95)
    costo_base = 50000
    costo = costo_base * (1 + (nivel - 85) * 0.04)
    ventas_perdidas = max(0, (99 - nivel) * 800)

    c1, c2, c3 = st.columns(3)
    c1.metric("Costo operativo mensual", f"${costo:,.0f}")
    c2.metric("Ventas perdidas estimadas", f"${ventas_perdidas:,.0f}")
    c3.metric("Impacto neto", f"${costo + ventas_perdidas:,.0f}")

    niveles = list(range(85, 100))
    costos   = [costo_base * (1 + (n - 85) * 0.04) for n in niveles]
    perdidas = [max(0, (99 - n) * 800) for n in niveles]
    df = pd.DataFrame({"Nivel %": niveles, "Costo Op.": costos, "Ventas Perdidas": perdidas})
    st.line_chart(df.set_index("Nivel %"))
