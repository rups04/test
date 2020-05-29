import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("rplgurjar@gmail.com","8058228686")
message= """\
Subject: Mlops-Project

Congrats !! Your model has been successfully Trained and You achieved more than 80% accuracy."""
s.sendmail("rplgurjar@gmail.com","rplgurjar@gmail.com",message)
s.quit()