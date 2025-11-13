def process_list(text: str) -> list:
    return [item.strip() for item in text.split(",") if item.strip()]