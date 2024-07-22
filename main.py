from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    sec_question1 = request.form['sec_question1']
    sec_answer1 = request.form['sec_answer1']
    sec_question2 = request.form['sec_question2']
    sec_answer2 = request.form['sec_answer2']
    sec_question3 = request.form['sec_question3']
    sec_answer3 = request.form['sec_answer3']

    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Security Question 1: {sec_question1}, Answer 1: {sec_answer1}")
    print(f"Security Question 2: {sec_question2}, Answer 2: {sec_answer2}")
    print(f"Security Question 3: {sec_question3}, Answer 3: {sec_answer3}")

    return "Form submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)
