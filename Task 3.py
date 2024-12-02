import os
from pathlib import Path

file1_path = "1.txt"
file2_path = "2.txt"
file3_path = "3.txt"

output_file_path = "output.txt"

with open(file1_path, 'r', encoding='utf-8') as file1:
    content1 = file1.read()

with open(file2_path, 'r', encoding='utf-8') as file2:
    content2 = file2.read()

with open(file3_path, 'r', encoding='utf-8') as file3:
    content3 = file3.read()

content_list = [content1,content2,content3]
sorted_contents = sorted(content_list, key=lambda x: len(x.split('\n')))

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for content in sorted_contents:
        output_file.write(content)


print(f"Информация из файлов {file1_path} , {file2_path} и {file3_path} записана в {output_file_path}")