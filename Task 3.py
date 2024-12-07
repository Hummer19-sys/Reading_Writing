def opening_and_forming(file_path, dishes, person_count):
    with open(file_path, encoding='utf-8') as f:
        data = f.read()

    cook_book = {}
    ingredients = []
    current_dish = None
    words = data.split('\n')
    non_empty_lines = [line for line in words if line.strip()]

    for i in non_empty_lines:
        if '|' in i:
            parts = [part.strip() for part in i.split('|')]
            ingridient = {
                'ingredient_name': parts[0],
                'quantity': int(parts[1]),
                'measure': parts[2]
            }
            ingredients.append(ingridient)
        if not i.isdigit() and "|" not in i:
            if current_dish:
                cook_book[current_dish] = ingredients
                ingredients = []
            current_dish = i

    if current_dish:
        cook_book[current_dish] = ingredients

    list_by_dishes = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if ingredient_name in list_by_dishes:
                    list_by_dishes[ingredient_name]['quantity'] += quantity
                else:
                    list_by_dishes[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' не найдено в cook_book.")

    return list_by_dishes


def main():
    file_path = 'recipes.txt'
    dishes = ['Омлет', 'Запеченный картофель']
    person_count = 2
    result = opening_and_forming(file_path, dishes, person_count)
    print(result)


if __name__ == "__main__":
    main()














