import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


retriever = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

generator_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(generator_name)
generator = AutoModelForSeq2SeqLM.from_pretrained(generator_name)

data = pd.read_csv("faq.csv")

questions = data["question"].tolist()

question_embeddings = retriever.encode(questions)

print("\n--- SEMANTIC FAQ RAG ASSISTANT ---")
print("Type 'exit' to stop.")

while True:
    user_question = input("\nAsk a question: ")

    if user_question.lower() == "exit":
        break

    user_embedding = retriever.encode([user_question])

    similarities = cosine_similarity(
        user_embedding,
        question_embeddings
    )[0]

    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    if best_score < 0.45:
        print("\nI couldn't find relevant enough information.")
        print("Best similarity:", round(best_score, 3))
        continue

    top_indices = similarities.argsort()[-3:][::-1]

    print("\n--- RETRIEVAL ---")

    for index in top_indices:
        print(
            round(similarities[index], 3),
            "-",
            data.iloc[index]["question"]
        )

    best_question = data.iloc[best_match_index]["question"]
    best_answer = data.iloc[best_match_index]["answer"]

    prompt = f"""
You are a customer support assistant.

Answer the user's question using only the FAQ information below.
Do not use information from anywhere else.
Keep the answer short and clear.

FAQ Question:
{best_question}

FAQ Answer:
{best_answer}

User Question:
{user_question}

Answer:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = generator.generate(
        **inputs,
        max_new_tokens=100
    )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    print("\n--- AI ANSWER ---")
    print(answer)