# Twilio Voice API Notes
 Followed the [Getting started with Programming Voice](https://www.twilio.com/docs/voice/quickstart/python#respond-to-incoming-calls-with-twilio) guide on Twilio to create the Flask-based script on responding to incoming calls with twilio

 Things I Learned:
 - Used Flask to make and receive phone calls from the script (to test script locally)
 - Created Python virtual environment to install Twilio and Flask packages
 - Used Chocolatey package manager to install ngrok (Creates a public url to allow Twilio to reach the script)
 - To prototype without needing to host(?) our own server, we can use built-in [TwiML bins](https://support.twilio.com/hc/en-us/articles/230878368-How-to-use-templates-with-TwiML-Bins)  using [TwiML Syntax](https://www.twilio.com/docs/voice/twiml/say#attributes)