import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Diagnostico Financiero Empresarial",
    layout="wide",  # 'centered' o 'wide'
    initial_sidebar_state="expanded"
)
 
# -----------------------------------
# ENCABEZADO
# -----------------------------------

st.markdown(
    """
    <h1 style='text-align: center; color:#1F4E79;'>
        DIAGNÓSTICO FINANCIERO EMPRESARIAL
    </h1>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    col_img1, col_img2, col_img3 = st.columns([1,3,1])
    with col_img2:
        st.image("Imagen.png", width=300)

st.markdown("""
### Herramienta de Evaluación Financiera

Esta herramienta ha sido diseñada para que usted pueda conocer y analizar la situación financiera actual de su empresa mediante el cálculo automático de los principales indicadores financieros. 

En la primera sección encontrará una explicación clara y sencilla de cada indicador: qué mide, cómo se calcula y cuál es su utilidad en la gestión empresarial, especialmente en el contexto de las micro y pequeñas empresas. 

En la segunda sección se encuentra la herramienta de diagnóstico. Allí deberá ingresar la información básica de su empresa y luego hacer clic en el botón **Calcular Indicadores Financieros**. El sistema procesará automáticamente los datos y le mostrará los principales indicadores financieros, junto con un diagnóstico general sobre el estado de su empresa y algunas recomendaciones orientadas a mejorar su desempeño financiero. 

**Recuerde que este diagnóstico es de carácter informativo y no reemplaza asesoría profesional personalizada.** 
""")

st.divider()
st.header("""¿Qué son los Indicadores Financieros y para qué sirven en nuestros negocios?
Los indicadores financieros son números que se sacan de las cuentas del negocio y que ayudan a entender si va bien o mal económicamente. Imagine que su negocio fuera una persona. Así como una persona necesita tomarse la presión o hacerse exámenes para saber si está sana, el negocio necesita revisar ciertos números para saber si está fuerte, si está en riesgo o si necesita mejorar algo. 

Básicamente, los indicadores financieros son relaciones entre números importantes del negocio, por ejemplo: ¿Cuánto se vende? ¿Cuánto se gasta? ¿Cuánto debe? ¿Cuánto dinero queda libre? ¿Cuánto dinero hay en la caja? Al comparar esos números entre sí, se obtienen indicadores que dicen claramente la situación del negocio. 
¿Por qué son tan importantes? Son importantes porque:
- Evitan pérdidas
- Ayudan a tomar mejores decisiones
- Permiten planear el futuro
- Hacen que el negocio esté más organizado

 Los indicadores financieros se clasifican según el aspecto que analizan, y se agrupan en indicadores de liquidez, indicadores de actividad, indicadores de endeudamiento e indicadores de rentabilidad: 

**INDICADORES DE LIQUIDEZ**

Este tipo de indicador mide la capacidad de la empresa para cumplir con sus obligaciones de corto plazo. En este grupo se tienen los siguientes indicadores:

- **Liquidez Corriente**: Indica cuántos pesos en activos corrientes existen por cada peso de deuda a corto plazo. 

- **Prueba Ácida**: Evalúa la capacidad de pago inmediato sin depender de la venta de los inventarios. 

**INDICADORES DE ACTIVIDAD**

Miden la eficiencia con la que la empresa utiliza sus recursos. En este grupo se tienen los siguientes indicadores:

- **Rotación de Inventarios**: Indica cuántas veces se renuevan los inventarios en un periodo.
- **Rotación de Activos Totales**: Mide la capacidad de los activos para generar ingresos. 

**INDICADORES DE ENDEUDAMIENTO:**
Evalúan el nivel de deuda y el grado de financiación con recursos de terceros:

- **Índice de Endeudamiento**: Muestra qué proporción de los activos está financiada con deuda. Un valor alto implica mayor dependencia de terceros y mayor riesgo financiero.

**INDICADORES DE RENTABILIDAD**

Miden la capacidad de la empresa para generar utilidades. En este grupo se tienen los siguientes indicadores:

- **Margen de Utilidad Bruta**: Refleja la ganancia después de cubir los costos directos de producción.
- **Margen de Utilidad Operativa**: Indica la rentabilidad generada por la actividad principal del negocio.
- **Margen de Utilidad Neta**: Mide la ganancia final obtenida por cada peso vendido.
- **ROA**: Evalúa qué tan eficientemente los activos generan utilidades 
- **ROE**: Mide la rentabilidad obtenida por los propietarios sobre su inversión.

En conjunto, los anteriores indicadores permiten analizar la estabilidad financiera, eficiencia operativa, nivel de riesgo y capacidad de generación de ganancias de una empresa. 
""")
st.subheader("Esquema General de Indicadores Financieros:")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("imagen2.jpeg", width=1000)

st.divider()

# -----------------------------------
# FORMULARIO
# -----------------------------------

st.markdown(
    "<h1 style='text-align: center;'>INGRESE LA INFORMACIÓN FINANCIERA DE SU EMPRESA</h1>",
    unsafe_allow_html=True
)

# -------------------------
# FORMULARIO COMPACTO
# -------------------------

with st.expander("Ingreso de Información Financiera", expanded=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        activos = st.number_input(
            "Activos Totales",
            min_value=0.0,
            step=1000.0,
            help="Total de bienes y recursos que posee la empresa."
        )
        # Mostrar con separador de miles en formato latino
        st.caption(f"Valor: {activos:,.0f}".replace(",", "."))

        pasivos_totales = st.number_input(
            "Pasivos Totales",
            min_value=0.0,
            step=1000.0,
            help="Total de deudas y obligaciones que tiene la empresa."
        )
        # Mostrar el valor con separador de miles (formato latino)
        st.caption(f"Valor: {pasivos_totales:,.0f}".replace(",", "."))

        pasivos_corrientes = st.number_input(
            "Pasivos Corrientes",
            min_value=0.0,
            step=1000.0,
            help="Deudas que deben pagarse en el corto plazo (menos de un año)."
        )
        # Mostrar el valor con separador de miles (formato latino)
        st.caption(f"Valor: {pasivos_corrientes:,.0f}".replace(",", "."))

    with col2:
        inventarios = st.number_input(
            "Inventarios",
            min_value=0.0,
            step=1000.0,
            help="Valor de mercancías disponibles para la venta."
        )
        # Mostrar el valor con separador de miles (formato latino)
        st.caption(f"Valor: {inventarios:,.0f}".replace(",", "."))

        ventas = st.number_input(
            "Ventas / Ingresos Totales",
            min_value=0.0,
            step=1000.0,
            help="Total de ingresos generados por la empresa."
        )
        # Mostrar el valor con separador de miles (formato latino)
        st.caption(f"Valor: {ventas:,.0f}".replace(",", "."))

    with col3:
        costos = st.number_input(
            "Costos directos",
            min_value=0.0,
            step=1000.0,
            help="Costos que están directamente asociados a la producción o adquisición de bienes vendidos o servicios prestados."
        )
        # Mostrar el valor con separador de miles (formato latino)
        st.caption(f"Valor: {costos:,.0f}".replace(",", "."))

        gastos_financieros = st.number_input(
            "Gastos Financieros",
            min_value=0.0,
            step=1000.0,
            help="Pago de intereses y costos derivados del financiamiento (Préstamos bancarios)."
        )
       # Mostrar el valor con separador de miles (formato latino)
        st.caption(f"Valor: {gastos_financieros:,.0f}".replace(",", "."))

        gastos_operativos = st.number_input(
            "Gastos operativos",
            min_value=0.0,
            step=1000.0,
            help="Son los gastos necesarios para operar el negocio (Sueldos, arriendo, servicios, logística, etc)."
        )
        # Mostrar el valor con separador de miles (formato latino)
        st.caption(f"Valor: {gastos_operativos:,.0f}".replace(",", "."))

st.divider()

# -------------------------
# CÁLCULOS
# -------------------------

if st.button("Calcular Indicadores Financieros"):


    utilidad_bruta = ventas - costos
    utilidad_operativa = utilidad_bruta - gastos_operativos
    utilidad_neta = utilidad_operativa - gastos_financieros
    patrimonio = activos - pasivos_totales

    # -------------------------
    # INDICADORES
    # -------------------------

    liquidez_corriente = activos / pasivos_totales if pasivos_totales > 0 else 0
    prueba_acida = (activos - inventarios) / pasivos_corrientes if pasivos_corrientes > 0 else 0

    rotacion_inventarios = costos / inventarios if inventarios > 0 else 0
    rotacion_activos = ventas / activos if activos > 0 else 0

    indice_endeudamiento = pasivos_totales / activos if activos > 0 else 0

    margen_bruto = utilidad_bruta / ventas if ventas > 0 else 0
    margen_operativo = utilidad_operativa / ventas if ventas > 0 else 0
    margen_neto = utilidad_neta / ventas if ventas > 0 else 0

    roa = utilidad_neta / activos if activos > 0 else 0
    roe = utilidad_neta / patrimonio if patrimonio > 0 else 0


    # -------------------------
    # RESULTADOS
    # -------------------------

    st.subheader("RESULTADOS DEL DIAGNOSTICO")

    # -------- LIQUIDEZ --------
    st.markdown("### Indicadores de Liquidez")

    st.write(f"**Liquidez Corriente:** {liquidez_corriente:.2f}")

    if liquidez_corriente < 1:
        st.warning("Menor a 1 → Se presentan posibles problemas para cubrir pagos inmediatos en su empresa debido a problemas de liquidez, ya que los activos disponibles no son suficientes para cubrir con las obligaciones inmediatas. Asegúrese de identificar la causa de este problema, pues podría enfrentar incumplimiento de pagos en el corto plazo.")
    elif 1 <= liquidez_corriente <= 1.5:
        st.info("Mayor a 1 → Su empresa presenta buena liquidez, pero tiene un margen limitado de maniobra.")
    elif 1.5 <= liquidez_corriente <= 3:
        st.success("Rango ideal (1.5 - 3) → Su empresa presenta una buena gestión del capital de trabajo, debido a que tiene suficientes activos líquidos para cubrir sus deudas a corto plazo, indicando solvencia y estabilidad financiera.")
    else:
        st.warning("Mayor a 3 → Este resultado indica que, aunque hay gran liquidez, puede existir capital o inventario ocioso, reduciendo rentabilidad. Debe identificar la causa de este exceso de liquidez, pues puede señalar una gestión ineficiente del capital de trabajo. ")

    st.write(f"**Prueba Ácida:** {prueba_acida:.2f}")

    if prueba_acida > 1:
        st.success("Escenario ideal → Puede cubrir deudas sin vender inventario. La empresa tiene más activos líquidos que pasivos a corto plazo. Es una señal positiva de que la empresa puede cubrir sus obligaciones inmediatas sin vender inventario.")
    elif prueba_acida == 1:
        st.info("Cobertura exacta → Alto riesgo ante imprevistos. Los activos líquidos y los pasivos a corto plazo son iguales. La empresa podría enfrentar problemas de pago si se presentan imprevistos .")
    else:
        st.warning("Menor a 1 → Riesgo de liquidez si no vende inventario. La empresa no tiene suficientes activos líquidos para cubrir sus pasivos a corto plazo. !Señal de alerta!.")

    # -------- ACTIVIDAD --------
    st.markdown("### Indicadores de Actividad")

    st.write(f"**Rotación de Inventarios:** {rotacion_inventarios:.2f}")
    st.info(f"Esto significa que su inventario se vendió y se repuso "
    f"{rotacion_inventarios:.2f} veces durante el período analizado. Revise qué tan rápido está vendiendo su inventario y posibles acciones de mejora."
)

    st.write(f"**Rotación de Activos Totales:** {rotacion_activos:.2f}")
    st.info(f"Por cada 1 peso invertido en activos, su empresa generó "
    f"${rotacion_activos:.2f} en ventas durante el período."
)

    # -------- ENDEUDAMIENTO --------
    st.markdown("### Indicadores de Endeudamiento")

    st.write(f"**Índice de Endeudamiento:** {indice_endeudamiento:.2%}")

    if 0.4 <= indice_endeudamiento <= 0.6:
        st.success("Su empresa registra un nivel equilibradado de endeudamiento.")
    elif indice_endeudamiento > 0.6:
        st.warning("Su empresa registra un alto riesgo financiero debido a un nivel de endeudamiento elevado, identifique las causas de este hecho.")
    else:
        st.info("Su empresa registra un uso conservador de deuda.")
    st.info(f"Por cada 1 peso en activos, "
    f"{indice_endeudamiento:} fue financiado con deuda y el restante con recursos propios."
)
    # -------- RENTABILIDAD --------
  
    st.markdown("### Indicadores de Rentabilidad")

    st.write(f"**Margen Bruto:** {margen_bruto:.2%}")

    if margen_bruto > 0:
        st.success(f"La empresa obtiene una ganancia bruta del {margen_bruto:.2%}.")
    elif margen_bruto < 0:
        st.error(f"La empresa registra una pérdida bruta del {abs(margen_bruto):.2%}.")
    else:
        st.warning("La empresa está en punto de equilibrio.")

    st.write(f"**Margen Operativo:** {margen_operativo:.2%}")
    if margen_operativo > 0:
        st.success(f"La empresa obtiene una ganancia operativa del {margen_operativo:.2%}.")
    elif margen_operativo < 0:
        st.error(f"La empresa tiene una pérdida operativa del {abs(margen_operativo):.2%}.")
    else:
        st.warning("La empresa está en punto de equilibrio.")

    st.write(f"**Margen Neto:** {margen_neto:.2%}")
    if margen_neto > 0:
        st.success(f"La empresa obtiene una ganancia neta del {margen_neto:.2%}.")
    elif margen_neto < 0:
        st.error(f"La empresa tiene una pérdida neta del {abs(margen_neto):.2%}.")
    else:
        st.warning("La empresa está en punto de equilibrio.")

    st.write(f"**ROA:** {roa:.2%}")
    if roa > 0:
     st.success(
        f"La empresa está generando una rentabilidad sobre activos del {roa:.2%}. "
        f"Esto significa que por cada $100 invertidos en activos, "
        f"se generan {roa*100:.2f} de utilidad neta."
    )

    elif roa < 0:
     st.error(
        f"La empresa presenta una rentabilidad NEGATIVA sobre activos del {abs(roa):.2%}. "
        f"Esto indica que los activos no están generando utilidades, "
        f"sino pérdidas en el período analizado."
    )

    else:
     st.warning(
        "La rentabilidad sobre activos es 0%. "
        "La empresa no generó utilidad ni pérdida en relación con sus activos."
    )

    st.write(f"**ROE:** {roe:.2%}")

    if roe > 0:
     st.success(
        f"La empresa está generando una rentabilidad sobre el patrimonio del {roe:.2%}. "
        f"Esto significa que por cada $100 invertidos por los accionistas, "
        f"se obtienen {roe*100:.2f} de utilidad neta."
    )

    elif roe < 0:
     st.error(
        f"La empresa presenta una rentabilidad NEGATIVA sobre el patrimonio del {abs(roe):.2%}. "
        f"Esto indica que los accionistas están perdiendo valor en el período analizado."
    )

    else:
     st.warning(
        "La empresa presenta patrimonio negativo debido a que sus deudas son mayores a sus activos. "
        "Su patrimonio no está generando rentabilidad."
    )
    # ===================================
    # RECOMENDACIONES GENERALES
    # ===================================

    alertas = []

    if margen_bruto < 0:
        alertas.append("El margen bruto es negativo.")

    if margen_operativo < 0:
        alertas.append("El margen operativo es negativo.")

    if margen_neto < 0:
        alertas.append("El margen neto es negativo.")

    if patrimonio <= 0:
        alertas.append("Los pasivos superan los activos (patrimonio negativo).")

    # ===== MOSTRAR RECOMENDACIONES =====

    st.markdown("---")
    st.subheader("Recomendación General")

    if len(alertas) == 0:
        st.success("La empresa presenta indicadores financieros estables. Sin embargo, se recomienda revisar la estructura financiera completa para tener una visión más completa.")
    else:
        for alerta in alertas:
            st.warning(alerta)

        st.write(
            "Se recomienda revisar costos, optimizar gastos y mejorar la "
            "estructura financiera para fortalecer la rentabilidad de su empresa."
        )

   

