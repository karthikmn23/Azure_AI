import os
import requests
from openai import AzureOpenAI

def main():
    endpoint ="" 
    apikey = ""

    client = AzureOpenAI(
        api_version= "2024-02-02",
        azure_endpoint = endpoint,
        api_key = apikey
    
    )
    def main()
        location = function_argument["location"]
        if(location):
            print(f"city: {location}")
            get_weather(location)

        def get_weather(location):
            url = "https://api.openweathermap.org/data"+location + "api_key"
            response = requests.get(url)
            get_response = response.json()
            latitude=get_response["coord"]["lat"]
            longitude= get_response["corrd"]["lon"]
            print(f"latitude: {latitude}")
            print(f"longitude: {longitude}")

            url_final = "https://api.openweathermap.org/data/2.5/weather?lat="+str(latitude) + "&lon="+str(longitude) +"&application"
            final_response = requests.get(url_final)
            final_response_json["weather"][0]["description"]
            print(final_response_json)
            weather = final_response_json["weather"][0]["description"]
            print(f"weather condition:{weather}")
              
    functions=[
        {
            "name":"getweather",
            "description":"Retrieve real-time weather information/data about a particular location/place"
            "parameters":{
                "type":"object",
                "properties":{
                    "location":{
                        "type":"string:,
                        "description":"theextract location whose real-time weather is to be determined"
                    },
                },
                "required":["location"]
            },
        }
    ]
     
    complection = cilent.chat.complections.create(
        model="chatmodel",
        message=[
            "role": "system","connect":""
            "role":"user","connect":""
        ]
    )
    print(completion.to_json())

if __name__=="__main__":
    main()

#for trying to predict weather we have to use api of weather and also url code of the weather