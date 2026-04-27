# AI_LOG.md

## Tools used
- **Gemini (1.5 Pro/Flash):** Used for architectural planning, code generation, and complex debugging.
- **Ollama (Local):** The primary runtime engine used for local LLM inference (Llama 3.1 8B) and embeddings (nomic-embed-text).
- **Streamlit Docs:** Referenced for session state and UI management.

## Significant prompts
1. **Prompt:** "Create a Streamlit chatbot using Ollama that only performs math calculations. Use FAISS for a local knowledge base (RAG) and Pydantic for structured tool output."
   - **AI produced:** A basic structure with `ollama.chat`, a simple FAISS index, and Pydantic schemas.
   - **Kept/Rejected:** Kept the Pydantic-to-tool mapping. Rejected the standard chat loop in favor of a streaming container to improve perceived speed.

2. **Prompt:** "The AI is confusing Simple Interest with Compound Interest. How can I fix the RAG retrieval?"
   - **AI produced:** Suggestions to use different indices or more complex metadata filtering.
   - **Kept/Rejected:** Rejected metadata filtering as it overcomplicated the "Tech Constraints." Instead, I kept the suggestion to "contrast" the text in the Knowledge Base (e.g., adding "This is NOT compound interest" to the Simple Interest entry).

3. **Prompt:** "Fix AttributeError: st.session_state has no attribute 'messages'. It happens on the first run."
   - **AI produced:** A snippet to initialize the list inside the chat input block.
   - **Kept/Rejected:** Rejected. I moved the initialization to the very top of `app.py`. Streamlit's top-to-bottom execution requires state to be ready before any UI elements attempt to append to it.

4. **Prompt:** "Optimize the code for a 5-8 second response time on a local machine."
   - **AI produced:** Recommended reducing `num_predict` and switching to a smaller model (Llama 3.2).
   - **Kept/Rejected:** Kept both. Reducing max tokens and using the 3B model significantly hit the target latency.

## A bug your AI introduced
**The "Unit-in-Calculator" Bug:**
The AI suggested a `general_calculator` tool that used a raw `eval(expression)`. However, when a user asked "100 meters to km", the AI would pass the string `"100/1000 meters"` to the tool. Because the tool didn't strip the word "meters," it threw a `SyntaxError` in Python. I caught this by seeing "Calculation error" in the UI. I fixed it by adding a Regex cleaner (`re.sub(r'[^0-9+\-*/().]', '', expression)`) to ensure only math-safe characters reached the evaluator.

## A design choice you made against AI suggestion
**Hardcoded Guardrails vs. LLM Guardrails:**
The AI initially suggested using a "Supervisor" LLM call to determine if a prompt was math-related or "off-topic" (like asking for the bot's name). I ignored this because it would double the response time (two LLM calls instead of one). Instead, I implemented a Python-based keyword check (`is_unrelated` and `is_math_query`) at the start of the chat logic. This provides an **instant** (0s latency) rejection of off-topic questions without wasting GPU resources.

## Time split
- **Prompting & Architecture:** 25%
- **Reviewing & Refining AI Output:** 20%
- **Debugging (State & Tool Logic):** 30%
- **Testing (Edge cases/Unit conversions):** 15%
- **Reading Documentation (Ollama API/FAISS):** 10%
