from flask import Flask, request, render_template
import sys

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')
        print('Received email:', email)
        print('Received password:', password)
        sys.stdout.flush() # force output to be printed immediately
        return 'Thank you for signing up!'
    else:
        return render_template('Registration_Form.html')

if __name__ == '__main__':
    app.run(debug=True)