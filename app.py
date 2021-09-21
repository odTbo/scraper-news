# https://towardsdatascience.com/how-to-send-beautiful-emails-with-python-the-essential-guide-a01d00c80cd0
from datetime import datetime
from interez import InterezMixin
from dotenv import load_dotenv
from email_formatting import create_message
from email.message import EmailMessage
import os
import smtplib

load_dotenv()


class News(InterezMixin):
    def __init__(self):
        super().__init__()
        self.from_email = os.getenv("FROM_EMAIL")
        self.to_email = os.getenv("TO_EMAIL")
        self.e_pass = os.getenv("PASSWORD")
        self.articles = self.get_articles()

    def create_email(self):
        today = datetime.now()
        today = today.strftime("%d/%m/%Y")

        mail_body = create_message(self.articles)

        msg = EmailMessage()
        msg["Subject"] = "Scraper News {}".format(today)
        msg["From"] = self.from_email
        msg["To"] = self.to_email
        msg.set_content(mail_body, subtype='html')

        return msg

    def send_email(self):
        mail_content = self.create_email()
        try:
            print("Sending...")
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(user=self.from_email, password=self.e_pass)
                connection.send_message(mail_content)
        finally:
            print("Done.")


if __name__ == "__main__":
    news = News()
    news.send_email()
