
# This program is meant to share bulk emails
# This oprogram will only work after enterng your passpword
import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
password="Fun@1234566"    #Correct your password to proceed further
ob.login("saregama20212021",password)
subject="Greetings...!"
body="Hello dear..! Gaurav this side welcome you to our new service,\n where we can send multiple emails alltogether.\n This will help you to save your time"
message="subject:{}\n\n{}".format(subject,body)
# print(message)
listofadress=[""]    # Enter your email ids here to send emails 
ob.sendmail("gaurav.raghav97@gmail.com",listofadress,message)

print("sent sucussfully.....cheers!!!")
