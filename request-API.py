import requests,render
import json

"""
def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    print(response_body.headers["Content-Type"])
    # assert response_body.headers["Content-Type"] == "application/json"
    return response_body
# print(test_get_locations_for_us_90210_check_content_type_equals_json())

host_url="http://localhost:3000"
body={
    "name":"raj kumar",
    "age":30,
    "profession":"python developer",
    "pass-out":2014

}
def test_post():
    response=requests.post(host_url,data=body)
    print(response)
    response_result=(json.dumps(response.json(),indent=4))
    print(response_result)

test_post()
"""
#--------------------to add parameters in API Url
payload={"key1":"value1"}
cookies=dict(key1='value2')
# response = requests.get("http://api.zippopotam.us/us/90210",params=payload,cookies=cookies)   #to pass parameters to url
# print(response.url)     #  (http://api.zippopotam.us/us/90210?key1=value1) output after adding payload
# print(response.text)
# print(response.status_code)
# print(response.headers)
# print(response.cookies)
# response = requests.get("http://api.zippopotam.us/headers",params=payload,cookies=cookies)
# print(response.headers)

#session object persist cookies across all requests made from the session instance

s=requests.session()
s.get('htttps://httpbin.org/cookies/set/sessioncookie/1234567')
r=s.get('htttps://httpbin.org/cookies')
print(r.text)

def index(request):
    url="https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
    city='LONDON'
    r=requests.get(url.format(city)).json()
    city_weather={
        'city':city,
        'tempature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
    }
    context={'city_weather':city_weather}
    return render(request,'weather.html',context)


#https://openweathermap.org/current
"""
security issues and vulnerabilities in APIs fall in categories:
>>Access controls
.Authorization
.Authentication
>>Rate limiting
>>Input validation
>>Restricting HTTP methods
>>3rd party API abuse
>>Other application logic error

"""









