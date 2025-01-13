def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        cats_list = []  # інформація про котиків

        for line in lines:
            try:
                # Ділимо рядок по кожному критерію
                cat_id, name, age = line.strip().split(',')
                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age  # Залишаємо вік як рядок
                }
                cats_list.append(cat_dict) 
            except ValueError:
                # Пропускаємо рядки з некоректним форматом
                print(f"Пропущено некоректний рядок: {line.strip()}")

        return cats_list
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

cats_info = get_cats_info("D:\\Progect 2.0\\Pythone core\\home _work 3.4\\cats_file.txt")
print(cats_info)
