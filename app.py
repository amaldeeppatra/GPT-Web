from flask import Flask, render_template, request, redirect
# from sample import output, text
import webbrowser
import os

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("landing.html")


@app.route('/kiit-gpt', methods=["GET", "POST"])
def kiit():
    display = ''
    if request.method == "POST":
        prompt = request.form.get("prompt")
        with open("prompt.txt", "w", encoding='utf8') as f:
            f.write(prompt)
        print(type(prompt))
        os.system(f'python sample.py --start="{prompt}"')
        with open("output.txt", 'r', encoding='utf8') as f:
            display = f.read()

    return render_template('kiit.html', output=display)




if __name__ == "__main__":
    app.run(debug=True)