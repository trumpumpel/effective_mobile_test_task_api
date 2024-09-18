Этот проект предназначен для автоматического тестирования работы с GitHub API. Скрипт создает новый публичный репозиторий, проверяет его наличие и удаляет его.

Установка и запуск

Шаг 1: Клонирование репозитория
bash
git clone https://github.com/your_username/my_github_api_test.git
cd my_github_api_test

Шаг 2: Установка зависимостей
pip install -r requirements.txt

Шаг 3: Настройка переменных окружения
Создайте файл .env в корне проекта и добавьте в него следующие строки:

GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
REPO_NAME=test-repo

Шаг 4: Запуск теста
python test_api.py


Этот проект должен корректно создавать, проверять и удалять репозиторий на GitHub.