import ...

client = AzureOpenAI(
    azure_endpoint="https://link of the openai.azure.com/",
    api_version="2023-09-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)

audio_file = open("file_name","rb")

response = client.audio.transcriptions.create(      #for translations we have to change form .audio.translations.create()
    model="audio_demo",            #the name of the file
    file = audio_file,
    response_format = text   #we can specifity this response format 
)

print(response)

