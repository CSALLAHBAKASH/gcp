"""Synthesizes speech from the input string of text."""
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

input_text = texttospeech.SynthesisInput(text="Hello my dear friend, how are you am fine thank you")

# Note: the voice can also be specified by name.
# Names of voices can be retrieved with client.list_voices().
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    # name="en-US-Studio-O",
    name="en-US-Studio-M",
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    speaking_rate=1
)

response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
    
    
    
    
    
# synthesise - sound to different accents    
# curl -X POST -H "Content-Type: application/json" \
# -H "X-Goog-User-Project: $(gcloud config list --format='value(core.project)')" \
# -H "Authorization: Bearer $(gcloud auth print-access-token)" \
# --data '{
# "input": {
#   "text": "hello how are you"
# },
# "voice": {
#   "languageCode": "en-GB",
#   "name": "en-GB-News-G"
# },
# "audioConfig": {
#   "audioEncoding": "LINEAR16"
# }
# }' "https://texttospeech.googleapis.com/v1/text:synthesize"