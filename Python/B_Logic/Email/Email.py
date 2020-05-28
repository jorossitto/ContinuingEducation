import smtplib

class Email:

    def sendMail(URL):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('test@gmail.com', 'testpassword')
        subject = 'Price went down'
        body = 'Check the link ' + URL

        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail('test@gmail.com', 'joRossitto@hotmail.com', msg)
        print('Email has been sent')
        server.quit()
