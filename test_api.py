import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = "https://api.github.com"
USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")


def create_repo():
    url = f"{GITHUB_API_URL}/user/repos"
    headers = {
        "Authorization": f"token {TOKEN}"
    }
    data = {
        "name": REPO_NAME,
        "private": False
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 201


def check_repo_exists():
    url = f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO_NAME}"
    headers = {
        "Authorization": f"token {TOKEN}"
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 200


def delete_repo():
    url = f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO_NAME}"
    headers = {
        "Authorization": f"token {TOKEN}"
    }
    response = requests.delete(url, headers=headers)
    return response.status_code == 204


if __name__ == "__main__":
    if create_repo():
        print("Репозиторий успешно создан.")
        if check_repo_exists():
            print("Репозиторий существует.")
            if delete_repo():
                print("Репозиторий успешно удален.")
            else:
                print("Ошибка при удалении репозитория.")
        else:
            print("Репозиторий не найден.")
    else:
        print("Ошибка при создании репозитория.")
