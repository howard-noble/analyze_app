from flask import Flask, render_template, request, redirect, flash
from authorized_users import AUTHORIZED_USERS
from analysis import analyze_rugby_match
from utils import send_email

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        youtube_link = request.form['youtube_link']

        # Check if user is authorized
        user = next((u for u in AUTHORIZED_USERS if u['email'] == email and u['youtube'] == youtube_link), None)
        if not user:
            flash("You are not authorized to access this system.", "danger")
            return redirect('/')

        # Analyze the match (returns dict with timestamps & stats)
        stats = analyze_rugby_match(youtube_link)

        # Send stats to user email
        send_email(email, stats, youtube_link)
        flash("Analysis complete! Check your email for clickable timestamps.", "success")
        return redirect('/')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

