from prompts import PROMPT_1, PROMPT_2, PROMPT_3, PROMPT_5
from key_words_utils.process_sting_to_dict import process_string_to_dict
from key_words_utils.process_list import process_list
from key_words_utils.mask_text import mask_text
from key_words_utils.compare_resulst import compare_results

def run_pipeline(hypothesis: str, model_query_func, embedding_function) -> dict:
    results = {}

    results["understanding"] = model_query_func(PROMPT_1.format(hypothesis=hypothesis))

    key_concepts = model_query_func(PROMPT_2.format(hypothesis=hypothesis))
    
    results["key_concepts"] = process_list(key_concepts)

    text_dict = model_query_func(PROMPT_3.format(hypothesis=hypothesis, key_concepts=key_concepts))
    results["dictionary"] = process_string_to_dict(text_dict)

    masked_texts = [mask_text(text=hypothesis, words_to_mask = x) for x in list(results["dictionary"].values()) if x]
    results["masked_text"] = masked_texts

    alt_answers = []
    for mtext in masked_texts:
        alt_answers.append(model_query_func(PROMPT_5.format(masked_text=mtext)))
    results["alt_answer"] = alt_answers
    results["comparison"] = []
    for answer in alt_answers:
        results["comparison"].append(compare_results(hypothesis, answer, embedding_function))

    return results
