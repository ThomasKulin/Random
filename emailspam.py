import smtplib

# Specify the From and To addresses
fromaddress = "ballisticbunny49@gmail.com"
toaddress = "16csm1@queensu.ca"

# need to send from a gmail address
# make sure to enable less secure app access on your google accnt
username = "ballisticbunny49@gmail.com"
password = "fuckyouyoucanthavemyshittypassword"

# write something cancer
message = """From:aids
aids 
"""

server =smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username,password)

# fuckn send it
for i in range (0,10):
    server.sendmail(fromaddress,toaddress,message)

server.quit()