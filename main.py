from pipeline import run_pipeline
from llm_logic_functions import gemini_embedding, ollama_query_model, gemini_query_model
import pandas as pd

df = pd.read_excel("data/datanoprompts.xlsx")
df = df.head(2)
understanding_list = []
key_concepts_list = []
dictionary_list = []
masked_text_list = []
alt_answer_list = []
comparison_list = []

for hypothesis in df['Гипотеза']:
    result = run_pipeline(hypothesis, model_query_func=ollama_query_model, embedding_function=gemini_embedding) # Замените model_query_func в случае использования другой модели
    print(hypothesis)
    understanding_list.append(result["understanding"])
    key_concepts_list.append(result["key_concepts"])
    dictionary_list.append(result["dictionary"])
    masked_text_list.append(result["masked_text"])
    alt_answer_list.append(result["alt_answer"])
    comparison_list.append(result["comparison"])

df["understanding"] = understanding_list
df["key_concepts"] = key_concepts_list
df["dictionary"] = dictionary_list
df["masked_text"] = masked_text_list
df["alt_answer"] = alt_answer_list
df["comparison"] = comparison_list

df.to_csv("data/hypotheses_processed.csv", encoding='utf-8-sig', index=False)