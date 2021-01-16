from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/hack", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    inb_msg = request.form['Body'].lower().strip() #gets incoming message
    resp = MessagingResponse()
    if inb_msg == "hi":
        # Add a message
        msg = resp.message("hi back")
        msg.media("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg")
    else:
        resp.message("not hi")

    return str(resp)

if __name__ == "__main__":
    #port 5000 !!!! 
    app.run(debug=True)