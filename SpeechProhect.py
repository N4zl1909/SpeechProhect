import speech_recognition as sr

# Tanıyıcı (Recognizer) oluştur
recognizer = sr.Recognizer()

# Mikrofonu başlat
with sr.Microphone() as source:
    print("Konuşabilirsiniz...")
    # Ses kaydet
    audio = recognizer.listen(source)

    try:
        # Google API ile sesi yazıya çevir
        text = recognizer.recognize_google(audio, language="tr-TR")
        print("Söylediğiniz: " + text)
    except sr.UnknownValueError:
        print("Ne dediğinizi anlayamadım.")
    except sr.RequestError:
        print("Google servisine ulaşılamıyor.")


