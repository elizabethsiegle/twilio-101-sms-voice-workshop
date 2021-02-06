from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)
@app.route('/femmehacks', methods=['GET', 'POST'])
def sms():
    inb_msg = request.form['Body'].lower().strip()
    resp = MessagingResponse()
    if(inb_msg == "hi"):
        msg = resp.message("hi")
        msg.media("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg")
    else:
        resp.message("else still hi, no image")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)