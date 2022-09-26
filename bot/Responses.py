import smtplib


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("enviar_correu"):
        return "Estas enviant un correu"
    
    if user_message in ("enviar_sms"):
        return "Estas enviant un sms"

    if user_message in ("adjuntar_media"):
        return "Estas adjuntant media"

# Queda pendent afegir al correu el factor de doble autenticació per a que el gmail envii correctament, ja que sino no hi té accés 
def enviar_correu():
    message = "Subject: mi correo del bot \n\nHola, un mensaje desde Python!"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('dnagertesting@gmail.com', 'admin1234!')
    server.sendmail('dnagertesting@gmail.com', 'dnagertesting@gmail.com', message)
    server.quit()
    print("Correo enviado")

def enviar_sms():

enviar_correu()
