import json
from flask import Flask, request, render_template
import openai

app = Flask(__name__)
with open(r'/Users/amiaynarayan/Projects/credential.json') as config_file:
    config = json.load(config_file)

openai.api_key = config.get("OPENAI_API_KEY")

def create_math_problems(practice, grade):
    prompt = f"Create 5 question for {practice} for grade {grade}.  Please omit all words.  End each question with and equals sign.  start each question with a 1) 2) 3) etc. "
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

@app.route('/', methods=["GET", "POST"])
def index():
    result = None
    print('request was made<________', request.form)
    if request.method == "POST":
        practice = request.form['practice']
        grade = request.form['grade']
        result = create_math_problems(practice, grade)
        result = result.split("\n")
        result = [item.replace(".", "\n") for item in result]

    return render_template("index.html", result=result)

@app.route('/science', methods=["GET", "POST"])
def science():
    result = None
    if request.method == "POST":
        practice = request.form['practice']
        grade = request.form['grade']
        result = create_math_problems(practice, grade)
        result = result.split("\n")
        result = [item.replace(".", "\n") for item in result]

    return render_template("index.html", result=result)

@app.route('/maths', methods=["GET", "POST"])
def maths():
    result = None
    if request.method == "POST":
        practice = request.form['practice']
        grade = request.form['grade']
        result = create_math_problems(practice, grade)
        result = result.split("\n")
        result = [item.replace(".", "\n") for item in result]

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)