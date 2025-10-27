import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, stats, youtube_link):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"  # Use app password if Gmail

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Rugby Match Analysis"
    msg['From'] = sender_email
    msg['To'] = to_email

    # Convert stats dict to clickable HTML links
    html_content = "<h2>Rugby Match Stats</h2><ul>"
    for event, timestamps in stats.items():
        html_content += f"<li>{event}: "
        html_content += ", ".join([f'<a href="{youtube_link}?t={ts}">{ts}</a>' for ts in timestamps])
        html_content += "</li>"
    html_content += "</ul>"

    msg.attach(MIMEText(html_content, 'html'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)
