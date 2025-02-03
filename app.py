from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Route for rendering the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Collect form data
        full_name = request.form['full_name']
        date_of_birth = request.form['date_of_birth']
        gender = request.form['gender']
        contact_number = request.form['contact_number']
        email_address = request.form['email_address']
        city = request.form['city']
        state = request.form['state']
        pin_code = request.form['pin_code']

        # File uploads
        passport_photo = request.files['passport_photo']
        aadhaar_card = request.files['aadhaar_card']
        pan_card = request.files['pan_card']

        # Checkboxes for declaration and consent
        declaration = request.form.get('declaration', 'off')
        consent = request.form.get('consent', 'off')

        # Google App Script URL
        google_script_url = 'https://script.google.com/macros/library/d/1K5KfDVwgKYJO6iYLhGcJxK4AD45cNvWoN7dmJXTB2T2KLChuvxJu-SHy/1'
        
        # Data to send
        data = {
            "full_name": full_name,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "contact_number": contact_number,
            "email_address": email_address,
            "city": city,
            "state": state,
            "pin_code": pin_code,
            "declaration": declaration,
            "consent": consent
        }

        # Sending files
        files = {
            'passport_photo': passport_photo.stream.read(),
            'aadhaar_card': aadhaar_card.stream.read(),
            'pan_card': pan_card.stream.read()
        }

        # Sending POST request to Google App Script
        response = requests.post(google_script_url, data=data, files=files)
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
