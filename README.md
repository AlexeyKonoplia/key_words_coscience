## Как запустить

1. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Создайте файл `.env` в корне проекта:

   ```bash
   GOOGLE_API_KEY="твой_ключ_от_Gemini"
   ```

3. Убедитесь, что установлен **Ollama** и скачана нужная модель:

   ```bash
   ollama pull llama3.1:8b
   ```

4. Запустите анализ:

   ```bash
   python main.py
   ```
    или же в **main.ipynb** запускать код по отдельности
Результаты сохраняются в `data/hypotheses_processed.csv`.

Общий вид функции для подключения к модели
```python
def custom_query_model(prompt: str, model_name: str = "your_model_name") -> str:
    """
    Универсальный шаблон функции для запроса к любой языковой модели (LLM).

    Args:
        prompt (str): Текст запроса (инструкция, гипотеза и т.д.)
        model_name (str): Название используемой модели или эндпоинта API.

    Returns:
        str: Сгенерированный текстовый ответ модели.
    """
```