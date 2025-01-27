from flask import Flask, render_template, request  # Імпорт Flask та необхідних модулів для роботи з веб-додатком

app = Flask(__name__)  # Створення екземпляра Flask-додатка

# Основний маршрут для калькулятора, підтримує методи GET і POST
@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None  # Змінна для зберігання результату обчислень

    # Перевіряємо, якщо метод запиту POST (тобто форма була відправлена)
    if request.method == "POST":
        try:
            # Отримуємо значення з форми та перетворюємо їх у числа
            num1 = float(request.form["num1"])  # Перше число
            num2 = float(request.form["num2"])  # Друге число
            operation = request.form["operation"]  # Операція, вибрана користувачем

            # Виконання відповідної операції залежно від вибору користувача
            if operation == "add":
                result = num1 + num2  # Додавання
            elif operation == "subtract":
                result = num1 - num2  # Віднімання
            elif operation == "multiply":
                result = num1 * num2  # Множення
            elif operation == "divide":
                if num2 != 0:  # Перевірка на ділення на нуль
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"  # Повідомлення про помилку
        except ValueError:
            # Якщо введено некоректні дані (наприклад, текст замість числа)
            result = "Invalid input"

    # Повертаємо HTML-шаблон разом із результатом обчислень
    return render_template("index.html", result=result)

# Точка входу для запуску додатка
if __name__ == "__main__":
    app.run(debug=True)  # Запускаємо сервер Flask у режимі налагодження
