from pathlib import Path
from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play

api_key = "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"
client = OpenAI(api_key=api_key)
# client = "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"

speech_file_path = Path(__file__).parent / "speech.mp3"
print(speech_file_path)
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="joy baba sunjid"
)
#
response.stream_to_file(speech_file_path)
sound = AudioSegment.from_file("speech.mp3", format="mp3")
play(sound)