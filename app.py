import streamlit as st
import ollama
import faiss
import numpy as np
from models import HypotenuseArgs, QuadraticArgs, CompoundInterestArgs, GeneralMathArgs
from tools import calculate_hypotenuse, solve_quadratic, compound_interest, general_calculator

st.set_page_config(page_title="Math AI Assistant", page_icon="🤖")
st.title("🤖 Math AI Chatbot")

with st.expander("📊 View My Capabilities", expanded=True):
    st.write("""
    - **Hypotenuse**: Solve $a^2 + b^2 = c^2$
    - **Quadratic**: Solve $ax^2 + bx + c = 0$
    - **Compound Interest**: Financial growth
    - **General Math**: Arithmetic & Unit Conversions
    """)

if "messages" not in st.session_state:
    st.session_state.messages = []

@st.cache_resource
def init_rag():
    model = 'nomic-embed-text'
    kb = [
        "Pythagorean theorem: Relation among the three sides of a right triangle.",
        "Quadratic formula: Used to solve equations of the form ax^2 + bx + c = 0.",
        "Compound interest: P * (1 + r/n)^(nt).",
        "Basic Arithmetic: Addition, subtraction, multiplication, and division.",
        "Unit Conversion (Length): 1 km = 1000m, 1m = 100cm.",
        "Unit Conversion (Weight): 1 kg = 1000g.",
        "Unit Conversion (Volume): 1 litre = 1000ml, 1 gallon = 3.785 litres."
    ]
    embeddings = [ollama.embeddings(model=model, prompt=t)['embedding'] for t in kb]
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings).astype('float32'))
    return index, kb

index, kb = init_rag()

TOOL_MAP = {
    'calculate_hypotenuse': (calculate_hypotenuse, HypotenuseArgs),
    'solve_quadratic': (solve_quadratic, QuadraticArgs),
    'compound_interest': (compound_interest, CompoundInterestArgs),
    'general_calculator': (general_calculator, GeneralMathArgs)
}

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a calculation question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        status_placeholder = st.empty()
        
        unrelated_words = ["your name", "who are you", "weather", "news", "joke", "hello", "hi"]
        is_unrelated = any(word in prompt.lower() for word in unrelated_words)

        if is_unrelated:
            full_response = "I am Math AI Chatbot, ask questions related to my capabilities 🙂"
            st.markdown(full_response)
        else:
            status_placeholder.info("Working on the problem...")
            
            vec = np.array([ollama.embeddings(model='nomic-embed-text', prompt=prompt)['embedding']]).astype('float32')
            _, i = index.search(vec, 1)
            context = kb[i[0][0]]

            resp = ollama.chat(
                model='llama3.1:8b', 
                messages=[
                    {
                        'role': 'system', 
                        'content': f"Context: {context}. You are a pure calculator. Do not define terms. If the user asks a math/conversion question, call the appropriate tool immediately using the context. If unrelated, say you only do calculations."
                    },
                    {'role': 'user', 'content': prompt}
                ],
                tools=[calculate_hypotenuse, solve_quadratic, compound_interest, general_calculator],
                options={'num_predict': 50, 'temperature': 0}
            )

            status_placeholder.empty()
            msg = resp.get('message', {})
            full_response = ""

            if msg.get('tool_calls'):
                info_display = f"**Information:** {context}"
                st.markdown(info_display)
                for tc in msg['tool_calls']:
                    name = tc['function']['name']
                    args = tc['function']['arguments']
                    func, schema = TOOL_MAP[name]
                    res = func(**schema(**args).model_dump())
                    st.success(f"Calculation Result: {res}")
                    full_response = f"{info_display}\n\nResult: {res}"
            else:
                full_response = msg.get('content', "I can only perform calculations based on my capabilities 🙂")
                st.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})