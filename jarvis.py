from pydub import AudioSegment
from pydub.playback import play
import openai
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import subprocess

openai.api_key = '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'

# Définissez le déclencheur (trigger)
trigger_phrase = "jarvis"

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("en attente du déclencheur...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        spoken_text = recognizer.recognize_google(audio, language="fr-FR").lower()
        print(f"Vous avez dit : {spoken_text}")

        if trigger_phrase in spoken_text:
            print(f"Déclencheur entendu: {trigger_phrase}")
            return spoken_text
        else:
            print("Déclencheur non entendu. En attente...")
            return None
    except sr.UnknownValueError as e:
        if "jarvis" in str(e).lower():
            print("Je suis désolé pouvez-vous répéter")
            text_to_audio("Je suis désolé, pouvez-vous répéter?")
            return None
        else:
            print(f"Erreur inconnue lors de la reconnaissance vocale : {e}")
            return None
    except sr.RequestError as e:
        print(f"Erreur lors de la requête à Google Speech Recognition service; {e}")
        return None

def chat_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful vocal assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message["content"]

def text_to_audio(text):
    tts = gTTS(text=text, lang='fr')
    audio_file_path = "output.mp3"
    tts.save(audio_file_path)
    return audio_file_path

# Ajout de la salutation
salutation_message = "Bonjour monsieur, comment puis-je vous aider ?"
audio_file_path = text_to_audio(salutation_message)

if audio_file_path:
    sound_salutation = AudioSegment.from_file(audio_file_path)
    play(sound_salutation)

while True:
    user_response = listen()


    if trigger_phrase in user_response:
        print("Déclencheur entendu. Vous pouvez maintenant poser des questions.")
        break
    else:
        print("Déclencheur non entendu. En attente...")

# Exemple d'utilisation
while True:
    # Demandez à l'utilisateur de poser une question
    ask_question_message = "Demandez moi ce que vous voulez."
    audio_file_path = text_to_audio(ask_question_message)

    if audio_file_path:
        sound = AudioSegment.from_file(audio_file_path)
        play(sound)

    # Attendez la question vocale de l'utilisateur
    user_question = ""
    while not user_question:
        user_question = listen()
    
    if "lance valorant" in user_question:
        response_message = "Bien sûr, monsieur. Lancement de Valorant."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Utilisez subprocess pour lancer le programme Valorant
        subprocess.run(["C:\\Riot Games\\Riot Client\\RiotClientServices.exe"])  

        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue

    if "lance microsoft edge" in user_question:
        response_message = "Bien sûr, monsieur. Lancement de microsoft edge."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Utilisez subprocess pour lancer le programme Valorant
        subprocess.run(["C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe"])  

        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue

    if "lance youtube musique" in user_question:
        response_message = "Tout de suite, monsieur. J'ouvre une page YouTube musique pour vous."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Ouvre YouTube dans le navigateur par défaut
        webbrowser.open("https://music.youtube.com/watch?v=cO3H9QACI1w&list=PLJv2h_s5WU6hiW-DpEkbNGhUMSybp2vMZ")
        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue
    
    if "lance cunchyroll" in user_question:
        response_message = "Tout de suite, monsieur. J'ouvre une page crunchyroll pour vous."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Ouvre YouTube dans le navigateur par défaut
        webbrowser.open("https://www.crunchyroll.com/fr")
        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue

    if "lance discord" in user_question:
        response_message = "Bien sûr, monsieur. Lancement de discord."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Utilisez subprocess pour lancer le programme Valorant
        subprocess.run(["C:\\Users\\dodog\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"])  

        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue

    if "lance league of legend" in user_question:
        response_message = "Bien sûr, monsieur. Lancement de league of legend."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Utilisez subprocess pour lancer le programme Valorant
        subprocess.run(["C:\\Riot Games\\League of Legends\\LeagueClient.exe"])  

        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue

    if "lance c s 2" in user_question:
        response_message = "Bien sûr, monsieur. Lancement de counter strike 2."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Utilisez subprocess pour lancer le programme Valorant
        webbrowser.open("steam://rungameid/730")  

        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle

        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue

    if "lance apex" in user_question:
        response_message = "Bien sûr, monsieur. Lancement de apex legende."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Utilisez subprocess pour lancer le programme Valorant
        webbrowser.open("steam://rungameid/1172470")  

        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue

    if "lance youtube" in user_question:
        response_message = "Tout de suite, monsieur. J'ouvre une page YouTube pour vous."
        audio_file_path = text_to_audio(response_message)

        if audio_file_path:
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Ouvre YouTube dans le navigateur par défaut
        webbrowser.open("https://www.youtube.com")

        # Maintenant, demandez si l'utilisateur souhaite poser une autre question
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            print(f"Chemin du fichier audio : {audio_file_path}")
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue

    else:
        # Générez la réponse
        response_text = chat_completion(user_question)

        # Affichez la réponse générée en texte
        print(f"Réponse générée : {response_text}")

        # Convertissez le texte en audio avec Google Text-to-Speech
        audio_file_path = text_to_audio(response_text)

        if audio_file_path:
            # Jouez le fichier audio avec Pydub
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Demandez si l'utilisateur souhaite poser une autre question vocalement
        another_question_message = "Voulez-vous poser une autre question ? Dites oui ou non."
        audio_file_path = text_to_audio(another_question_message)

        if audio_file_path:
            print(f"Chemin du fichier audio : {audio_file_path}")
            sound = AudioSegment.from_file(audio_file_path)
            play(sound)

        # Attendez la réponse vocale de l'utilisateur
        user_response = ""
        while not user_response:
            user_response = listen()
        
        user_response_lower = user_response.lower()

        if "non" in user_response_lower:
            pause_message = "Très bien. Je suis en pause. Appelez-moi si besoin."
            audio_file_path = text_to_audio(pause_message)

            if audio_file_path:
                sound = AudioSegment.from_file(audio_file_path)
                play(sound)

            # Attendez le déclencheur pour reprendre
            while not listen():
                pass

            continue  # Continuez à la prochaine itération de la boucle
        elif "oui" in user_response_lower:
            # Continuez la boucle pour la prochaine question
            continue   