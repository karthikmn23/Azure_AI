import os
from openai import AzureOpenAI
import numpy as np


cilent = AzureOpenAI(
    azure_endpoint='https://',
    api_version = "2023-06-01-preview"
    api_key = os.environ['OPENAI_API_KEY']

)

response = cilent.embeddings.create(
    model= "embed_demo",      #we can also find similarity of the model using 
    #input="cat "             #for only one word we use this like without similarity

    input=["hot","cold"]    #for both letters we find similarity
)

print(response)
#print(response.data[0].embedding)
#print(response.data[1].embedding)        #for similarity use embedding 1 and embedding 2 for comparison 
embedding1 = response.data[0].embedding   #and also for comparing this we should use like similarity_score
embedding2 = response.data[1].embedding

similarity_score = np.dot(embedding1, embedding2)    #to find similarity we use numpy function 
print(similarity_score*100, "%")

