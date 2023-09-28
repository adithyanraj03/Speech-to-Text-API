import assemblyai as aai

# replace with your API token
aai.settings.api_key = f"f4b0aafc76a44933a6f3569672155b81"

# URL of the file to transcribe
FILE_URL = "C:\Users\madhav\Desktop\assembly ai api memo\SnapInsta.io - KGF Power inspiring Mass Dialog Malayalam _ KGF Mass scene _ Yash,Prashanth Neel (128 kbps).mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL,config = aai.TranscriptionConfig(summarize=True,summary_model = aai.SummarizationModel.conversational,summary_type = aai.summarization_type.bullets_verbose))

print(transcript.text)
