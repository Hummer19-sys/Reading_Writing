import os
from pathlib import Path

# Чтение всех txt c определенной директории и сортировка значений списка
def read_files_from_directory(directory):
    content_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                content_list.append(content)
    sorted_contents = sorted(content_list, key=lambda x: len(x.split('\n')))
    return sorted_contents

# Запись output файла
def write_content_to_file(sorted_contents, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for content in sorted_contents:
            output_file.write(content)
            output_file.write('\n')

# Основная функция для определения параметров
def main():
    directory = 'C:\\Users\\Владислав\\Desktop\\Reading_Writing\\Files'

    sorted_contents = read_files_from_directory(directory)

    output_file_path = os.path.join(directory, 'output.txt')

    write_content_to_file(sorted_contents, output_file_path)

    print(f"Информация из директории {directory} записана в {output_file_path}")

# Проверка, запущен ли скрипт напрямую
if __name__ == "__main__":
    main()