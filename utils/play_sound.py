from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("indossare_mascherina.wav")
play(song)