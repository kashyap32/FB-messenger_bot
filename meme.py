#

import os
import sys
import json
import base64
from bs4 import BeautifulSoup
import random
import requests
#import pymongo
import requests
from flask import Flask, request
# from PIL import Image

app = Flask(__name__)
# app.config.from_pyfile('flaskapp.cfg')

PAGE_TOKEN = "PAGE TOKEN"
VERIFY_TOKEN = "app_secret"

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must
    # return the 'hub.challenge' value in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Working", 200


@app.route('/', methods=['POST'])
def webook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    print data
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

				if messaging_event.get("message"):  # someone sent us a message

					print '?'*20

					print messaging_event
					print '?'*20

					sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
					recipient_id = messaging_event["recipient"]["id"]
                    # the recipient's ID, which should be your page's facebook ID
                                        print messaging_event

					message_text = messaging_event["message"]["text"]
                    # the message's text
                                        if message_text=='Popular':


                                            url="http://www.memes.com/popular"+"/"+str(random.randrange(0,25))
                                            print url

                                            # links.append(url)
                                            # print links
                                            data=[]
                                            response=requests.get(url).text
                                            soup=BeautifulSoup(response,"html.parser")
                                            for image in soup.find_all('a',{'class':'imglink'}):
                                                    #print image

                                                    image_link= "http://images.memes.com/meme"+image['href'].replace('/tile','').replace('/img','')
                                                    #print image_link

                                            send_typing(sender_id)
                                                            #image=open('trump/image3.png','r')
                                                            #image=open('trump/image3.png','rb').read()
                                                            #encoded_string = base64.b64encode(image.read())

                                                            # print image
                                            send_message(sender_id,"hello")
                                            send_typing(sender_id)

                                            send_image(sender_id, image_link)
                                            send_quick_reply(sender_id)
                                        if message_text=='Trump':
                                            url="http://www.memes.com/search/trump"+"/"+str(random.randrange(0,60))
                                            print url

                                            # links.append(url)
                                            # print links
                                            data=[]
                                            response=requests.get(url).text
                                            soup=BeautifulSoup(response,"html.parser")
                                            for image in soup.find_all('a',{'class':'imglink'}):
                                                    #print image

                                                    image_link= "http://images.memes.com/meme"+image['href'].replace('/tile','').replace('/img','').replace('/searchresults','').replace('/trump','')
                                            print image_link

                                            send_typing(sender_id)
                                                            #image=open('trump/image3.png','r')
                                                            #image=open('trump/image3.png','rb').read()
                                                            #encoded_string = base64.b64encode(image.read())

                                                            # print image
                                            send_message(sender_id,"hello")
                                            send_typing(sender_id)

                                            send_image(sender_id, image_link)
                                            send_quick_reply(sender_id)
                                        if message_text=='Funny':
                                            url="http://memeblender.com/memes/funny-meme-mix/page"+"/"+str(random.randrange(0,230))
                                            print url

                                            # links.append(url)
                                            # print links
                                            data=[]
                                            response=requests.get(url).text
                                            soup=BeautifulSoup(response,"html.parser")
                                            for image in soup.find_all('img',{'class':'attachment-bimber-stream size-bimber-stream wp-post-image'}):
                                                    #print image

                                                    image_link=image['src']
                                            print image_link

                                            send_typing(sender_id)
                                                            #image=open('trump/image3.png','r')
                                                            #image=open('trump/image3.png','rb').read()
                                                            #encoded_string = base64.b64encode(image.read())

                                                            # print image
                                            send_message(sender_id,"hello")
                                            send_typing(sender_id)

                                            send_image(sender_id, image_link)
                                            send_quick_reply(sender_id)
                                        if message_text=='Meanwhile':
                                            url="http://www.memecenter.com/search/meanwhile"
                                            print url

                                            # links.append(url)
                                            # print links
                                            data=[]
                                            response=requests.get(url).text
                                            soup=BeautifulSoup(response,"html.parser")
                                            for image in soup.find_all('img',{'class':'rrcont'}):
                                                    #print image

                                                    image_link=image['src']
                                            print image_link

                                            send_typing(sender_id)
                                                            #image=open('trump/image3.png','r')
                                                            #image=open('trump/image3.png','rb').read()
                                                            #encoded_string = base64.b64encode(image.read())

                                                            # print image
                                            send_message(sender_id,"hello")
                                            send_typing(sender_id)

                                            send_image(sender_id, image_link)
                                            send_quick_reply(sender_id)

                                            #send_quick_reply(sender_id)
                                        if message_text=='Random':
                                            url="http://www.memes.com/random"
                                            print url

                                            # links.append(url)
                                            # print links
                                            data=[]
                                            response=requests.get(url).text
                                            soup=BeautifulSoup(response,"html.parser")
                                            for image in soup.find_all('a',{'class':'imglink'}):
                                                    #print image

                                                    image_link= "http://images.memes.com/meme"+image['href'].replace('/tile','').replace('/img','')
                                            print image_link

                                            send_typing(sender_id)
                                                            #image=open('trump/image3.png','r')
                                                            #image=open('trump/image3.png','rb').read()
                                                            #encoded_string = base64.b64encode(image.read())

                                                            # print image
                                            send_message(sender_id,"hello")
                                            send_typing(sender_id)

                                            send_image(sender_id, image_link)
                                            send_quick_reply(sender_id)




    					#send_quick_reply(sender_id)

				if messaging_event.get("delivery"):  # delivery confirmation
					pass

				if messaging_event.get("optin"):  # optin confirmation
					pass

				if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
					msg = messaging_event["postback"]['payload']
					send_id = messaging_event["sender"]['id']

					if msg == "Trump":
						send_message(send_id, "Welcome to HeyFacts! Explore crazy facts with just one tap.")
						send_message(send_id, "Tell us HI and start reading.")
					elif msg == "prattle":
						send_image(send_id, "http://i.imgur.com/kDhvK3w.png")
						send_msg = "HeyFacts is made by Prattle, Ahmedabad, India based chatbot focused startup. \nDrop us query : info@getprattle.com \nvisit website : www.getprattle.com"
						send_message(send_id, send_msg)
					elif msg == "what":
						send_message(send_id, "Send us HI and get cool facts around the world.")


    return "ok", 200


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": PAGE_TOKEN
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


def send_typing(recipient_id):

	params = {
        "access_token": PAGE_TOKEN
    }
	headers = {
        "Content-Type": "application/json"
    }
	data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "sender_action":"typing_on"
    })
	r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


def send_image(recipient_id, url):

	params = {
        "access_token": PAGE_TOKEN
    }
	headers = {
        "Content-Type": "application/json"
    }
	data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
		"message": {
			"attachment":{
				"type":"image",
				"payload":{
					"url": url
				}
			}
		},
    "quick_replies":[
        {
            "content_type":"text",
            "title":"Random",
            "payload":"next"
        },
        {
            "content_type":"text",
            "title":"Trump",
            "payload":"next"
        },
        {
            "content_type":"text",
            "title":"Popular",
            "payload":"next"
        }
    ]

    })
	r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


def send_quick_reply(recipient_id):


	params = {
        "access_token": PAGE_TOKEN
    }
	headers = {
        "Content-Type": "application/json"
    }
	data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
						"text":'Click "Next" or send "Next" to load more facts',
						"quick_replies":[
							{
								"content_type":"text",
								"title":"Random",
								"payload":"next"
							},
                            {
								"content_type":"text",
								"title":"Trump",
								"payload":"next"
							},
                            {
								"content_type":"text",
								"title":"Popular",
								"payload":"next"
							},
                            {
								"content_type":"text",
								"title":"Funny",
								"payload":"next"
							},

                            {
								"content_type":"text",
								"title":"Meanwhile",
								"payload":"next"
							}
						]
					}
    })

	r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)



#menu
def per_menu():
	params = {
		"access_token": PAGE_TOKEN
	}
	headers = {
		"Content-Type": "application/json"
	}

	data = json.dumps({
			"setting_type" : "call_to_actions",
			"thread_state" : "existing_thread",
			"call_to_actions":[
				{
					"type":"postback",
					"title":"What is HeyFacts?",
					"payload":"what"
				},
				{
					"type":"postback",
					"title":"Created by Prattle",
					"payload":"prattle"
				}
			]
		})
	r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings", params=params, headers=headers, data=data)

#menu
def start_button():
	params = {
		"access_token": PAGE_TOKEN
	}
	headers = {
		"Content-Type": "application/json"
	}

	data = json.dumps({
			"setting_type" : "call_to_actions",
			"thread_state" : "new_thread",
			"call_to_actions":[
				{
					"payload":"start_button"
				}
			]
		})
	r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings", params=params, headers=headers, data=data)


per_menu()
start_button()



def log(message):  # simple wrapper for logging to stdout on heroku
	print "-"*10
	# print str(message)
	sys.stdout.flush()

# app id - 1626493137661365
# page id - EAAXHSXGzLbUBABOG4sJMQYzHNYgf3419pwCGfXFSKYmJReXqxU9pjQEDqtq6r6liipbZCIMptoJ8exs0QOEAb81th61V95BQbpCJNDIgTFSTwq6B6ZCASCZBvSqsp4DdO27Y4Y2F4GzCTQtaaK5Jp3V9CHArqmGHPvnT8OCSQZDZD

if __name__ == '__main__':
    app.run(debug=True,port=5432)
