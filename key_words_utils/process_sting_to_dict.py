import ast

def process_string_to_dict(text: str) -> dict:
    start_index = text.find('{')
    end_index = text.rfind('}') + 1

    dict_str = text[start_index:end_index].strip()

    return ast.literal_eval(dict_str)