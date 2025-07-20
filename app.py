import streamlit as st

def generate_expression(a: int, r: int, n: int):
    poly1 = a**2 + a + 1
    poly2 = a**3 + 1
    target_value = r**n
    denominator = poly1 * poly2
    numerator = target_value - 1

    st.markdown("### 🔢 Given")
    st.write(f"a = {a}")
    st.write(f"Desired result (r) = {r}")
    st.write(f"Root (n) = {n}")

    st.markdown("### 📐 Expression Structure")
    st.latex(r"((a^2 + a + 1)(a^3 + 1) \cdot k + 1)^{1/n} = r")

    if numerator % denominator != 0:
        approx_k = numerator / denominator
        st.error("⚠️ Not a perfect root.")
        st.write(f"Closest k ≈ {approx_k:.6f}")
        return

    k = numerator // denominator

    st.markdown("### ✅ Perfect Expression")
    st.latex(
        rf"(({poly1}) \cdot ({poly2}) \cdot {k} + 1)^{{1/{n}}} = {r}"
    )
    st.markdown("### 📊 Computation Check")
    st.write(f"({poly1}) * ({poly2}) * {k} + 1 = {target_value:,}")
    st.success("It works!")

st.title("🔢 Root Expression Generator")
st.write("Build expressions of the form:")
st.latex(r"((a^2 + a + 1)(a^3 + 1) \cdot k + 1)^{1/n} = r")

a = st.number_input("Enter a (base value)", min_value=1, value=81)
r = st.number_input("Enter r (desired result)", min_value=1, value=11)
n = st.number_input("Enter n (root)", min_value=2, value=16)

if st.button("Generate Expression"):
    generate_expression(int(a), int(r), int(n))
