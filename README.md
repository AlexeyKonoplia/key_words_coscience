## Как запустить

1. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Создай файл `.env` в корне проекта:

   ```bash
   GOOGLE_API_KEY="твой_ключ_от_Gemini"
   ```

3. Убедись, что установлен **Ollama** и скачана нужная модель:

   ```bash
   ollama pull llama3.1:8b
   ```

4. Запусти анализ:

   ```bash
   python main.py
   ```

Результаты сохраняются в `data/hypotheses_processed.csv`.