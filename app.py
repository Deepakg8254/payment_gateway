from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"  # You can use any secret key

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Home route that renders the form
@app.route('/')
def index():
    return render_template('form.html')

# Handle the form submission
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        date_of_birth = request.form['dateOfBirth']
        email = request.form['email']
        phone = request.form['phone']
        
        # File upload handling
        file = request.files['myFile']
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            flash(f'File successfully uploaded to {file_path}', 'success')
        else:
            flash('No file uploaded', 'warning')

        # Simulate saving to a Google Sheet or a database here
        # For now, just return a success message
        flash(f'Data for {first_name} {last_name} saved successfully!', 'success')

        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
