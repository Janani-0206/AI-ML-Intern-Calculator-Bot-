#  AI_LOG.md

## Project: AI Finance Assistant (RAG-based Chatbot using Ollama + FAISS + Streamlit)

##  Project Duration
**Thursday, 23 April 2026 → Monday, 27 April 2026**

##  Tools Used
**Gemini / Ollama**
  Used for architectural planning, local LLM tool-calling logic, and RAG implementation
**VS Code**
  Used as the primary editor for Python development and environment management

##  Significant Prompts

###  1. Date: Thursday, 23 April 2026
**Prompt:**
"Create a Calculator Bot using Streamlit and Ollama that handles quadratic equations and hypotenuse math."
**What AI produced:**
* Basic Streamlit chat interface
* Python functions for math logic
* Standard LLM-based responses
**What I kept:**
* Streamlit UI structure
* Math functions
**What I rejected:**
* Standard LLM responses for math
**Reason:**
LLM-generated math answers were often inaccurate, so a structured **tool-calling approach** was used instead.

###  2. Date: Friday, 24 April 2026
**Prompt:**
"Implement a RAG system using FAISS and nomic-embed-text for a math knowledge base."
**What AI produced:**
* Embedding logic for formulas
* FAISS-based similarity search
* Context retrieval system
**What I kept:**
* FAISS index
* Embedding logic
**What I rejected:**
* External vector databases
**Reason:**
Needed a **local, in-process setup** for simplicity and performance.

###  3. Date: Saturday, 25 April 2026
**Prompt:**
"Add support for Simple and Compound Interest calculations with Pydantic schemas."
**What AI produced:**
* Pydantic models
* Tools for Simple Interest (SI) and Compound Interest (CI)
**What I kept:**
* Both SI and CI calculation tools
**What I rejected:**
* Combining both into a single tool
**Reason:**
Keeping them separate improved **RAG retrieval accuracy**.

###  4. Date: Sunday, 26 April 2026
**Prompt:**
"The chatbot is explaining the math instead of just giving the answer. Fix the system prompt."
**What AI produced:**
* Updated system instructions
* Enforced tool-only responses
**What I kept:**
* "Do not define terms" instruction
**What I rejected:**
* Long response templates
**Reason:**
Needed **clean, fast, and minimal output**.

###  5. Date: Monday, 27 April 2026
**Prompt:**
"Fix the calculation error when users type units like 'ml' or 'cm' in the general calculator."
**What AI produced:**
* Complex NLP parser for unit detection
**What I kept:**
* Idea of cleaning user input
**What I rejected:**
* Complex NLP parsing logic
**Reason:**
To reduce latency and maintain simplicity, implemented a **Regex-based filter** instead.

##  Bug Introduced by AI
** Date:** Saturday, 25 April 2026
**Issue:**
Both Simple Interest and Compound Interest tools had the same description.
This caused the model to call the **Compound Interest tool** even when Simple Interest was requested.
**How I identified:**
* Tested Simple Interest query
* Output was unexpectedly high (compound effect)
**Fix:**
* Updated tool descriptions
* Added clear distinction:
  **"This is NOT compound interest"**

##  Design Decision Against AI
** Date:** Sunday, 26 April 2026
**AI Suggestion:**
Use a second LLM as a **Supervisor** to filter unrelated queries
**Decision:**
Used a **Python-based keyword check** instead
**Reason:**
* LLM call: ~5–8 seconds
* Python check: Instant
Result: **Better speed and efficiency**

##  Time Distribution
* Writing code: **40%**
* Prompting AI tools: **15%**
* Reviewing AI output: **15%**
* Debugging: **20%**
* Testing: **10%**
