Этот проект предназначен для автоматического тестирования работы с GitHub API. 
Скрипт создает новый публичный репозиторий, проверяет его наличие и удаляет его.

1. Клонируйте репозиторий:



2. Установите зависимости:
pip install -r requirements.txt


3. Создайте файл `.env` и добавьте в него ваши переменные окружения:
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
REPO_NAME=test-repo


Запустите скрипт:
python test_api.py
