
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

email = "lucien.ledune@student.uclouvain.be"
coffee = "americano"


#SEND EMAIL 
sg = sendgrid.SendGridAPIClient(api_key='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')
from_email = Email("lucien.ledune.ds@gmail.com")  # Change to your verified sender
to_email = To(email)  # Change to your recipient
subject = "Your coffee order"
content = Content("text/plain", "Here's the {} you ordered".format(coffee))
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)

#or 

a = sg.send(mail)




