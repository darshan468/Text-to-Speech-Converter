from gtts import gTTS

text = input("Enter the text want you need to convert into speech: ")
language = input("Enter language code (e.g., 'en' for English, 'hi' for Hindi, 'ta' for Tamil): ")

tts = gTTS(text=text, lang=language)              # conver the text to speech

tts.save("audio2.mp3")

print("Audio saved as audio1.mp3")
