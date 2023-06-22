from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")

    contacts_list = list(rows)
# pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код
for i in contacts_list:
    if len(i[0].split()) == 3:
        name = i[0].split()
        for j in range(len(name)):
            i[j] = name[j]
# Мартиняхин
contacts_list[2][4] = contacts_list[4].pop(4)
contacts_list.pop(4)
# Наркаев
name = contacts_list[3][1].split()
contacts_list[3][1] = name[0]
contacts_list[3][2] = name[1]
# Лагунцов
contacts_list[6][6] = contacts_list[7].pop()
contacts_list.pop()

#номер мартиняхина
pattern = r'(\+7|8)(\d{3})(\d{3})(\d{2})(\d{2})'
subst_pattern = r'+7(\2)\3-\4-\5'
# numbers1 = re.findall(pattern, contacts_list[2][5])
result = re.sub(pattern, subst_pattern, contacts_list[2][5])
contacts_list[2][5] = result

# номер Усольцева
pattern = r'(\+7|8)(\s)(\(\d+\))(\s)(\d+)-(\d+)-(\d+)'
subst_pattern = r'+7\3\5-\6-\7'
result = re.sub(pattern, subst_pattern, contacts_list[1][5])
contacts_list[1][5] = result

# Номер Наркаева
pattern = r'(\+7|8)(\s)(\d+)-(\d+)-(\d{2})(\d{2})'
subst_pattern = r'\1(\3)\4-\5-\6'
result = re.sub(pattern, subst_pattern, contacts_list[3][5])
contacts_list[3][5] = result

# Номер Лукиной
pattern = r'(\+7|8)(\s)(\(\d+\))\s(\d+)-(\d+)-(\d+)\s(\w+.)\s(\d+)'
subst_pattern = r'\1\3\4-\5-\6 \7\8'
result = re.sub(pattern, subst_pattern, contacts_list[4][5])
contacts_list[4][5] = result

# Номер Лагунцова
pattern = r'(\+7|8)(\s)(\(\d+\))\s(\d+)-(\d+)-(\d+)\s\((\w+.)\s(\d+)\)'
subst_pattern = r'\1\3\4-\5-\6 \7\8'
result = re.sub(pattern, subst_pattern, contacts_list[-1][5])
contacts_list[-1][5] = result

print('-------------')
pprint(contacts_list)
# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)