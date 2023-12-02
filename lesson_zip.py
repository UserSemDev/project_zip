from zipfile import ZipFile
from pathlib import Path
import shutil


def new_folder():
    """Функция создает новую папку"""
    user_answer = input("Введите название папки: ").strip()
    user_fold = Path(user_answer)
    if not user_fold.exists():
        user_fold.mkdir()
        print(f"[INFO] Папка [{user_answer}] создана")
        return user_fold
    else:
        print("[INFO] Такая папка уже есть")


def add_files_user(folder):
    """Функция создает введенное количество файлов в папке"""
    user_answer = input("Введите сколько файлов вы хотите создать в папке: ")
    if user_answer.isdigit():
        user_answer = int(user_answer)
        for file in range(1, user_answer+1):
            with open(f"{folder}/file{file}.txt", "w", encoding="utf-8") as f:
                f.write(f"Какой то текст №{file}")
                print(f"Файл № {file} из {user_answer} создан")
    else:
        print("[ERROR] Вы ввели не число")


def delete_folder(folder):
    """Функция удаляет папку рекурсивно"""
    user_answer = input(f"Вы хотите удалить папку [{folder}] и файлы в ней? Да/Нет: ")
    if user_answer.lower() in ["да", "yes"]:
        if folder.exists():
            shutil.rmtree(folder)
            print(f"[INFO] Папка '{folder}' удалена")
    elif user_answer.lower() in ["нет", "no"]:
        print(f"[INFO] отмена")
    else:
        print("[ERROR] Таково ответа нет.")


def add_zip_file(folder):
    """Функция добавляет файлы в zip архив"""
    with ZipFile(f"{folder}.zip", "w") as zip_file:
        for file in folder.iterdir():
            zip_file.write(file)
        print(f"[INFO] Zip-архив с названием [{folder}.zip] создан")


def unzip_file(folder):
    """Функция распаковывает zip архив"""
    with ZipFile(f"{folder}.zip", "r") as zip_file:
        zip_file.extractall(f"unzip_{folder}")
        print(f"[INFO] Zip-архив [{folder}.zip] разархивирован")


def start():
    """Основная логика программы"""
    # запрашиваем название папки и создаем ее
    user_folder = new_folder()
    # если папка создалась идём дальше
    if user_folder:
        # вызываем функцию создания файлов в папке
        add_files_user(user_folder)
        user_answer = input("Вы хотите добавить файл в архив? Да/Нет: ").strip()
        if user_answer.lower() in ["да", "yes"]:
            # Добавляем папку с файлами в zip архив
            add_zip_file(user_folder)
            # Запрос на удаление папки с файлами
            delete_folder(user_folder)
            user_answer = input(f"Вы хотите распаковать архив [{user_folder}.zip]? Да/Нет: ").strip()
            if user_answer.lower() in ["да", "yes"]:
                # распаковка zip архива
                unzip_file(user_folder)


if __name__ == '__main__':
    start()
