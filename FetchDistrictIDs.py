import requests

url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"

payload={}

# :authority: cdn-api.co-vin.in
# :method: GET
# :path: /api/v2/admin/location/districts/36
# :scheme: https
# accept: application/json, text/plain, */*
# accept-encoding: gzip, deflate, br
# accept-language: en-US,en;q=0.9
# origin: https://www.cowin.gov.in
# referer: https://www.cowin.gov.in/
# sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"
# sec-ch-ua-mobile: ?0
# sec-fetch-dest: empty
# sec-fetch-mode: cors
# sec-fetch-site: cross-site
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'}

for state in range(36):
	response = requests.request("GET", url+str(state), headers=headers, data=payload, allow_redirects=False).json()
	for i in response['districts']:
		print(i['district_id'], " - ", i['district_name'])
#print(response['districts'])
