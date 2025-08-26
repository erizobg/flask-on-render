from flask import Flask
import os

# Създаваме Flask приложението
app = Flask(__name__)

# Основен route
@app.route("/")
def home():
    return "Hello from Flask on Render!"

# Друг примерен route
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}! Welcome to Flask on Render."

# Стартираме приложението само ако файлът се изпълнява директно
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render задава PORT
    app.run(host="0.0.0.0", port=port)
