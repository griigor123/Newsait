from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница
@app.route("/")
def home():
    return render_template("index.html")

# Страница контактов
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Сохраняем сообщение в файл
        with open("messages.txt", "a") as f:
            f.write(f"Имя: {name}\nEmail: {email}\nСообщение: {message}\n---\n")

        return "<h2>Спасибо за сообщение!</h2><a href='/'>Назад</a>"

    return render_template("contact.html")

# Страница 'О сайте'
@app.route("/about")
def about():
    return render_template("about.html")

# Страница просмотра всех сообщений
@app.route("/messages")
def messages():
    try:
        with open("messages.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = "Сообщений пока нет."

    return f"<pre>{content}</pre>"

# Запуск сервера
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
