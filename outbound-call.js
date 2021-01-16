const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

client.calls
      .create({
         twiml: '<Response><Say>Ahoy, World!</Say></Response>',
         to: process.env.MY_PHONE_NUMBER,
         from: '+14045864101'
       })
      .then(call => console.log(call.sid));