from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        with open("messages.txt", "a") as f:
            f.write(f"Имя: {name}\nEmail: {email}\nСообщение: {message}\n---\n")

        return "<h2>Спасибо за сообщение!</h2><a href='/'>Назад</a>"

    return render_template("contact.html")

@app.route("/messages")
def messages():
    try:
        with open("messages.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = "Сообщений пока нет."

    return f"<pre>{content}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
