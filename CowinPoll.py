import requests
import json
from playsound import playsound
from time import sleep
#playsound('audio.wav')

from datetime import datetime
now = datetime.now() # current date and time
Date = now.strftime("%d-%m-%Y")

print("\n\nDate:", Date, "\n")
print("******************************************************************************\n")
print("OMNI AUTOMATION")
print("COWIN POLLER")
print("Beta-V0")
print("Developed by Omkar Bhatt.")
print("The script will take DistrictID from the user and then poll the Cowin Server for data for the next 4 days every 10 seconds.")
print("If it finds any center with vaccines 18-45 years age group, it will sound an alarm - Look for the last entry on the screen.")
print("Searching using DistrictID has turned to show more results.\n")
print("******************************************************************************\n")
DistrictID = input("Enter District ID (not PinCode): ")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
def check(ID, Tarikh):
	print('Requesting server... ', ID, Tarikh)
	#try:
	x = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=' + ID + '&date=' + Tarikh, headers = headers)
	#x = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=384002&date='+ Tarikh, headers = headers)
	#Only sessions in this type of response

	if x.status_code == 200:
		print("Sucessful!\n")
		response = x.json()
		#print(response)
		#response = json.loads(requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=384002&date=31-03-2021').text)
		for i in response['centers']:
			# print('----------------------------------------------------------------------------')
			# print('CENTER : ', i['name'])
			# print('----------------------------------------------------------------------------')
			for a in i['sessions']:
				#print('Date: ', a['date'], ' Available: ', a['available_capacity'], " Vaccine: ", a['vaccine'], " Age Limit: ", a['min_age_limit'])
				if a['min_age_limit'] == 18:
					#print('Date: ', a['date'], ' Available: ', a['available_capacity'], " Vaccine: ", a['vaccine'], " Age Limit: ", a['min_age_limit'])
					if int(a['available_capacity']) > 0:
						print('Date: ', a['date'], ' Available: ', a['available_capacity'], " Vaccine: ", a['vaccine'], " Age Limit: ", a['min_age_limit'])
						print("Vaccine Found !!!")
						playsound('audio.wav')
	else:
		print("Server has blocked the request. ;)")
	#except Exception as e:
	#	print(e)

while True:
	check(DistrictID, Date)
	sleep(10)