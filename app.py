# Primeiro Exercicio
import streamlit as st

# Configuração inicial da página (título da aba e ícone)
st.set_page_config(
    page_title="Calculadora Interativa",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Simples & Elegante")
st.markdown("Selecione os números, escolha a operação e veja a mágica do Python!")

st.divider()

# 2. Entradas numéricas organizadas lado a lado em duas colunas
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input(
        "Primeiro número:",
        value=0.0,
        format="%.2f"
    )

with col2:
    num2 = st.number_input(
        "Segundo número:",
        value=0.0,
        format="%.2f"
    )

# 3. Componente de seleção para a operação matemática
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

st.write("") # Espaço em branco para respiro visual

# 4. Botão de ação
if st.button("Calcular", type="primary", use_container_width=True):
    resultado = None
    erro = None

    # Lógica de cálculo
    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        # 5. Tratamento de divisão por zero
        if num2 == 0:
            erro = "Operação inválida: não é possível realizar divisão por zero (0.0)."
        else:
            resultado = num1 / num2

    # Exibição do feedback ao usuário
    if erro:
        st.error(f"⚠️ {erro}")
    else:
        # Formatação do resultado (remove casas decimais excedentes se for inteiro)
        resultado_formatado = f"{resultado:.4f}".rstrip("0").rstrip(".") if isinstance(resultado, float) else f"{resultado}"
        
        st.success("Cálculo realizado com sucesso!")
        st.metric(
            label="Resultado Final",
            value=resultado_formatado
        )
