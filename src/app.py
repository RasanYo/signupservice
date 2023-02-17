from flask import Flask, request, render_template
import sys
from InfluxClient import InfluxClient

app = Flask(__name__, template_folder='../templates', static_folder='../static')
influxclient = InfluxClient()
@app.route('/', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')
        print('Received email:', email)
        print('Received password:', password)
        influxclient.insert_data(email)
        
        sys.stdout.flush() # force output to be printed immediately

        return 'Thank you for signing up!'
    else:
        return render_template('Registration_Form.html')

if __name__ == '__main__':
    app.run(debug=True)
    sys.stdout.flush()
    # stop the app after 10 seconds
    import time
    time.sleep(10)


# from flask import Flask, request, render_template

# app = Flask(__name__, template_folder='../templates', static_folder='../static')

# saved_email = None
# saved_password = None

# @app.route('/', methods=['GET', 'POST'])
# def registration_form():
#     global saved_email
#     global saved_password

#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         # Assign values to global variables
#         saved_email = email
#         saved_password = password

#         return 'Thank you for signing up!'
#     else:
#         return render_template('Registration_Form.html')

# if __name__ == '__main__':
#     app.run(debug=True)
