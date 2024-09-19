Проект предназначен для автоматического тестирования работы с GitHub API. 
Используются Python, Requests и Python-dotenv.
Скрипт создает новый публичный репозиторий, проверяет его наличие и удаляет его.

1. Клонируйте репозиторий:
git clone https://github.com/trumpumpel/effective_mobile_test_task_api
cd effective_mobile_test_task_api


2. Установите зависимости:
pip install -r requirements.txt


3. Создайте файл `.env` и добавьте в него ваши переменные окружения:
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
REPO_NAME=test-repo


Запустите скрипт:
python test_api.py