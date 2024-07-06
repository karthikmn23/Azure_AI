import ..
openai.api_type = "azure"
openai.api_base  = ""
openai.api_version = '2023-09-0=25-perview"
openai.api_key = os.getenv("OPENAI_API_KEY")

training_file_name = 'training_set.jsonl'
validation_file_name = 'validation_set.jsonl'

#Uploading the training adn validation dataset files to Azure Openai

training_response = openai.File.create(
    file=open(training_file_name, "rb"), purpose="fine_tune", user_provided_filename = "training_set.jsonl"
)

training_file_id = training_response["id"]

validation_response = openai.File.create(
    file = open(validaion_file_name, "rb"),purpose = "fine-tune",user_provided_filename= "training_set.jsonl"

)
validation_file_id = validation_response["id"]

print("Training file ID:", training_file_id)
print("validation file ID:", validation_file_id)

response = openai.FineTuningJob.create(
    training_file = training_file_id,
    validation_file = validation_file_id,
    model = "gpt-35-turbo-0613",
)

job_id = response['id']

#you can use the job ID to mointor the status of the fine-tuning jsonl
#the fine_tuning jo will take some time to start and complete.
