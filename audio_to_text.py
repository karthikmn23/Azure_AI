client = AzureOpenAI(
    azure_endpoint = "https:",
    api_version = "2023-06-01-preview"
    api_key = os.environ['OPENAI_API_KEY']
)

audio_file = open("sample_english.m4a","rb")

#response = cilent.audio.translations.create()
response = cilent.audio.transcriptions.create(
    model = "audio_demo",
    file = audio_file
)
print(response)
