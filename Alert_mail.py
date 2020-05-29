import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("rplgurjar@gmail.com","8058228686")
message= """\
Subject: Mlops-Project ALERT !!!

There is some issue while launching the container."""
s.sendmail("rplgurjar@gmail.com","rplgurjar@gmail.com",message)
s.quit()