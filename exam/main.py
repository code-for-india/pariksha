from flask import Flask, render_template, request
import base64
from binascii import a2b_base64
from random import randint
import pyimgur
import json
import unirest

app = Flask(__name__)


def n():
	return str((randint(0,9)))

def about_image(link):
	link = link[19:]
	print link
	response = unirest.post("https://kairos-face-recognition.p.mashape.com/recognize",
  headers={
    "X-Mashape-Key": "3Q8lK5DobzmshPkPDp0bi4LfVCOyp1h1jlTjsnnNnxhGTAl1MX",
    "Content-Type": "application/json",
    "app_id": "d7d36416",
    "app_key": "4b27bb14a0d2dfeb76d4c902b950cce7",
    "Accept": "application/json"
  },
  params=("{\"url\":\"http://i.imgur.com/"+link+"\",\"gallery_name\":\"pariksha\",\"threshold\":\".7\",\"max_num_results\":\"3\"}")
  )
  	return response


def image_upload(path):
	CLIENT_ID = "dbf557dc83d3b71"	
	PATH = path

	im = pyimgur.Imgur(CLIENT_ID)	
	uploaded_image = im.upload_image(PATH, title="")
	print "image uploaded"
	print uploaded_image.link
	return uploaded_image.link


@app.route('/')
def index():
	return render_template('start.html')

@app.route('/capture', methods=['POST'])
def capture():
	return render_template('index.html')

@app.route('/uploads', methods=(['POST']))
def upload():
	imgData = request.form['imgData']
	imgData = imgData[22:]
	fh = open("check.png", "wb")
	fh.write(imgData.decode('base64'))
	fh.close()
	roll = request.form['roll']
	return imgData

@app.route('/decide')
def decide():
	link = image_upload("/home/ruchi/Desktop/CFI/exam/check.png")
	a =  about_image(link).body
	try:
		b = a['images'][0]
		print b['attributes']
		return render_template('recognised.html')
	except:
		return render_template('unrecognised.html') 

@app.route('/exam')
def exam():
	return render_template('exam.html')

@app.route('/block')
def block():
	return render_template('blocked.html')

@app.route('/teacher')
def teacher():
	return render_template('teacher.html')
@app.route('/otp', methods=(['POST']))
def otp():
	msg = "Your OTP is 27514"
	phn = request.form['number']
	response = unirest.get("https://webaroo-send-message-v1.p.mashape.com/sendMessage?message="+msg+"&phone="+phn,
  		headers={
    		"X-Mashape-Key": "3Q8lK5DobzmshPkPDp0bi4LfVCOyp1h1jlTjsnnNnxhGTAl1MX"
  		}
	)
	try:
		data = (response.body)['response']['phone']
		data = "Message sent"
	except:
		data = (response.body)['data']['message']
	return render_template('message.html', phn=phn, msg=data)

if __name__ == '__main__':
	app.run(debug=True, port=5003)