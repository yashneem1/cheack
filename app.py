from flask import Flask, render_template, request
import os

# Determine the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create the Flask app with the template folder set to the current directory
app = Flask(__name__, template_folder=current_directory)

# Example whitelist
WHITELIST = {"0x4925E62Df6aefB9398018D75DE26D86d1AA6B8ee"}

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        user_address = request.form.get('address')
        if user_address in WHITELIST:
            message = "You are eligible!"
        else:
            message = "You are not eligible."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
