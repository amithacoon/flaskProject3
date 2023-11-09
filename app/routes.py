from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
import os
from utils.audio_utils import get_audio_duration

# A fake "database" to keep our results handy
results_db = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Got a file in the POST request?
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            duration = get_audio_duration(filepath)
            # Save the file info and how long it plays
            results_db.append({'filename': filename, 'duration': duration})
            # Go back to the main page once we're done here
            return redirect(url_for('index'))
    # Show the main page and any results we've got
    return render_template('index.html', results=results_db)

def allowed_file(filename):
    # Is this the kind of file we're ok with?
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
