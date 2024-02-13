import whisper
import ssl



ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("base")
result = model.transcribe("D:/GitRepo/DataScience/Audio_Model/CallRecording1.mp3")

with open("D:/GitRepo/DataScience/Audio_Model/CallRecording6.txt","w") as f:
    f.write(result["text"])
