<<<<<<< HEAD
# Calculator Bot

A Streamlit-based AI Math Assistant that uses advanced AI to answer math questions, perform calculations, and provide educational explanations.

## Features

- **Hypotenuse Calculator**: Solve Pythagorean theorem (a² + b² = c²)
- **Quadratic Solver**: Find roots of quadratic equations (ax² + bx + c = 0)
- **Compound Interest Calculator**: Calculate financial growth with compound interest
- **General Math Calculator**: Arithmetic operations and unit conversions(Length,Volume,Weight)
- **RAG-powered Responses**: Uses Retrieval-Augmented Generation to fetch correct formulas before calaculation for accurate answers

## Tech Stack

- **Language**: Python 3.11+
- **UI**: Streamlit
- **AI**: Ollama with Llama 3.1 8B (local LLM)
- **Vector Store**: FAISS (in-process)
- **Embeddings**: Ollama embeddings with nomic-embed-text
- **Structured Output**: Pydantic
- **Dependencies**: Managed via requirements.txt

## Installation

1. Install Python 3.11+
2. Install Ollama: `winget install Ollama.Ollama`
3. Pull embedding model: `ollama pull llama 3.1:8b, ollama pull nomic-embed-text`
4. Clone/download the project
5. Install dependencies: `pip install streamlit ollama faiss-cpu numpy pydantic`
6. Run: `streamlit run app.py`

## Usage

1. **View Capabilities**: Expand the "View My Capabilities" section to see available features
2. **Ask Questions**: Type math questions in the chat input
3. **Get Calculations**: Ask for specific calculations (hypotenuse, quadratic, compound interest)
4. **View Results**: See step-by-step results with explanations

## Architecture

- **RAG Pipeline**: Knowledge base → embeddings → FAISS indexing → retrieval → LLM generation
- **Instant Guardrails**: python-based keyword filtering to block non-math queries with zero latency
- **Tool-based Calculations**: Uses function calling for accurate math instead of model arithmetic
- **Error Handling**: Proper exception handling without silent failures
- **Session Management**: Conversation history persistence

## Files

- `app.py`: Main application with RAG and AI chatbot
- `models.py`: Pydantic models for calculation arguments
- `tools.py`: Calculation functions (hypotenuse, quadratic, compound interest, general calculator)
- `requirements.txt`: Dependencies (Streamlit, Ollama, FAISS, NumPy, Pydantic)
- `README.md`: This documentation

## Example Questions

- "Find the hypotenuse of a triangle with sides 3 and 4"
- "Solve x² - 5x + 6 = 0"
- "Calculate compound interest on 1000 at 5% for 2 years"
- "What is the Pythagorean theorem?"
=======
# AI-ML-Intern-Calculator-Bot-
AI/ML Developer Internship Variant B to develop a chatbot with Tool/function call and use
>>>>>>> ef50212e78e94407a62b63d4556fd024d4548e97
