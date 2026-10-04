# Semantic FAQ RAG Assistant

A small Retrieval-Augmented Generation (RAG) project built with Python.

The application takes a user question, retrieves the most relevant FAQ using semantic similarity, and then uses a local language model to generate a final answer.

---

## Overview

The project combines two AI components:

- Sentence Transformer for semantic search
- FLAN-T5 for response generation

The pipeline is:

```text
User Question
      ↓
Create Embedding
      ↓
Compare With FAQ Embeddings
      ↓
Retrieve Best Match
      ↓
Build Prompt With Retrieved Context
      ↓
FLAN-T5
      ↓
Generated Answer
```

---

## Features

- Semantic FAQ search
- Sentence embeddings
- Cosine similarity
- Top-3 retrieval results
- Similarity threshold for unrelated questions
- Local text generation with FLAN-T5
- CSV-based FAQ knowledge base
- Fully local RAG-style pipeline

---

## Project Structure

```text
Day-06-Semantic-FAQ-Matcher/
│
├── main.py
├── faq.csv
├── requirements.txt
└── README.md
```

---

## How It Works

### 1. FAQ Loading

The FAQ data is stored in `faq.csv`.

Example:

```csv
question,answer,category
How do I reset my password?,Use the forgot password option on the login page to receive a reset link.,account
Why was my card declined?,Check your card details and whether online payments are enabled.,billing
Why is my microphone not working?,Check your browser microphone permissions and input device.,technical
```

---

### 2. Embeddings

Each FAQ question is converted into a semantic embedding using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The same process is applied to the user's question.

These embeddings represent the meaning of the sentences as numerical vectors.

---

### 3. Retrieval

The user's embedding is compared with all FAQ embeddings using cosine similarity.

The system retrieves the most similar FAQ.

It also displays the top three matches for inspection.

Example:

```text
--- RETRIEVAL ---

0.875 - Why was my card declined?
0.326 - My payment isn't going through. What should I do?
0.221 - How do I upgrade to Pro?
```

---

### 4. Similarity Threshold

If the best similarity score is below:

```text
0.45
```

the system refuses to answer.

This prevents unrelated questions from being matched with random FAQ entries.

---

### 5. Generation

The best FAQ question and answer are added to a prompt.

Example:

```text
FAQ Question:
Why was my card declined?

FAQ Answer:
Check your card details and whether online payments are enabled.

User Question:
Why does my card keep getting declined?

Answer:
```

This prompt is passed to:

```text
google/flan-t5-small
```

The model then generates the final answer.

---

## Example

```text
Ask a question: why does my card keep getting declined

--- RETRIEVAL ---

0.875 - Why was my card declined?
0.326 - My payment isn't going through. What should I do?
0.221 - How do I upgrade to Pro?

--- AI ANSWER ---

Check your card details and make sure online payments are enabled.
```

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
pandas
scikit-learn
sentence-transformers
transformers
torch
sentencepiece
```

---

## Usage

Run the program:

```bash
python main.py
```

Then enter a question:

```text
Ask a question: I forgot my password
```

Type:

```text
exit
```

to stop the program.

---

## Technologies

- Python
- Pandas
- Scikit-learn
- Sentence Transformers
- Hugging Face Transformers
- PyTorch
- FLAN-T5
- Cosine Similarity

---

## What I Learned

This project helped me understand:

- Sentence embeddings
- Semantic search
- Cosine similarity
- Top-k retrieval
- Retrieval-Augmented Generation
- The difference between retrieval and generation
- How pretrained transformer models can be used in Python
- How retrieval failures differ from generation failures

---

## Limitations

This is a learning project and is not intended for production use.

Current limitations include:

- Small FAQ dataset
- No vector database
- Linear search across all FAQ embeddings
- Small generation model
- No conversation memory
- Retrieval is based mainly on FAQ questions
- FLAN-T5-small can sometimes generate inaccurate responses

---

## Possible Improvements

Future improvements could include:

- Larger FAQ dataset
- Embedding both questions and answers
- FAISS or another vector database
- Stronger language model
- Better prompt design
- Conversation history
- Web interface
- Retrieval evaluation metrics