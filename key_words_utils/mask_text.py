import re

def mask_text(text: str, words_to_mask: list) -> str:
    """
    Заменяет все слова из списка на [MASKED] в исходном тексте
    """
    pattern = r'\b(' + '|'.join(map(re.escape, words_to_mask)) + r')\b'
    
    masked_text = re.sub(pattern, '[MASKED]', text, flags=re.IGNORECASE)
    return masked_text