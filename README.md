# Rasa_chatbot
Small Chatbot demonstration made with Rasa. 

This is a bot for placing coffee order. 
It can sell americano, cappucino or normal coffee. 
It will take your order, ask for email and send an email to your address (which represents the coffee)

Demo here : https://www.youtube.com/watch?v=xsxTN2ABjO4

(It isn't shown in the video but an email with the coffee name is sent at the end of the dialog).

If you want the email to be sent, you need to edit the lines in actions.py, under "#SEND EMAIL" with your own API KEY and user email. 

The key can be obtained for free on sendgrid website. 

# Running instructions : 

- Make sure docker is installed 
- Open terminal 
- sudo docker run -p 8000:8000 rasa/duckling
- Open another terminal and navigate to the repo folder. 
- (rasa train) #for re-training models
- rasa run actions & rasa shell #for talking to the bot
