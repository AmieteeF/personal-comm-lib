from dotenv import load_dotenv

import smtplib
from email.message import EmailMessage

SMPTP_SERVER = "smtp-mail.server.com"
SMTP_PORT = 587

class SMTPClient:
    def __init__(self, username: str, password: str):
        self.smtp_server = SMPTP_SERVER
        self.port = SMTP_PORT
        self.username = username
        self.password = password
        self.client = smtplib.SMTP(self.smtp_server, self.port)

    def send_email(self, subject: str, body: str, to: str, to_cc: str = "") -> None:
        """
        Send an email using the SMTP client.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        :param to: Recipient email address.
        :return: None
        """
        # build the email message
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to
        msg['Cc'] = to_cc

        with self.client as client:
            try:
                # puts connection to the SMTP client in TLS mode
                client.starttls()
                client.login(self.username, self.password)
                client.send_message(msg)
                print(f"Email sent to {to} successfully.")
            except Exception as e:
                print(f"Failed to send email to {to}: {e}")

if __name__ == "__main__":
    # Example usage
    email_client = SMTPClient()
    email_client.send_email(
        subject="Test Email",
        body="This is a test email sent from SMTPClient.",
        to="name@example.com",
    )
