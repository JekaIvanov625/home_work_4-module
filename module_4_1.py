def total_salary(path):
    try:
      
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  

        total = 0.0  # Загальна сума
        count = 0  # Кількість людей

        for line in lines:
            try:
                # Людина та її зарплата
                name, salary = line.strip().split(',')
                total += float(salary)  # Додаємо зарплату до загальної суми
                count += 1
            except ValueError:
                # Якщо формат рядка некоректний, пропускаємо його
                print(f"Пропущено некоректний рядок: {line.strip()}")
        
        # Рахуємо середню зарплату
        average = total / count

        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None

# Шлях до файлу
path_to_file = "D:Progect 2.0\Pythone core\home _work 3.4\zarplata.txt"

# Використання функції
result = total_salary(path_to_file)
result
