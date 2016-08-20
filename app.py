import os
import sys
import json
from bs4 import BeautifulSoup
import urllib2,cookielib,requests
from flask import Flask, request

app = Flask(__name__)
ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN"
VERIFY_TOKEN = "VERIFY_TOKEN"


@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    site= "http://www.quotationspage.com/random.php3"
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    req = urllib2.Request(site, headers=hdr)
    try:
        page = urllib2.urlopen(req)
        soup2=BeautifulSoup(page)
        for name in soup2.find_all("dt",{'class':'quote'}):
              names=name.text



        print names
        for authors in soup2.find_all('dd',{'class':'author'}):
                author=authors.text
                author=author.replace(' More quotations on: ','')
        print author
        names=names+author

    except:
        pass
      




    data = request.get_json()
    log(data)  #its good for testing nothing else

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent  a message to page

                    sender_id = messaging_event["sender"]["id"]        
                    recipient_id = messaging_event["recipient"]["id"]  
                    message_text = messaging_event["message"]["text"]

                    


                    send(sender_id, names)#it will send quote(Random) to the user

                if messaging_event.get("delivery"):  
                    pass

                if messaging_event.get("optin"):  
                    pass

                if messaging_event.get("postback"):  
                    pass

    return "ok", 200


def send(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True,port=5432)
