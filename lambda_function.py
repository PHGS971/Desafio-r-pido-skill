import random

def lambda_handler(event, context):
    if event["request"]["type"] == "LaunchRequest":
        return respond("Bem-vindo ao Desafio Rápido! Quer tentar um desafio aleatório?")

    if event["request"]["type"] == "IntentRequest":
        intent_name = event["request"]["intent"]["name"]

        if intent_name == "StartChallengeIntent":
            challenges = [
                "Imite uma galinha por 5 segundos!",
                "Fale uma palavra ao contrário!",
                "Diga um trava-língua agora!",
                "Dance sem música por 10 segundos!",
                "Fale 3 frutas em menos de 3 segundos!",
                "Imite um robô falando!",
                "Fale algo engraçado!",
                "Finja que você é a Alexa agora!",
                "Conte uma piada boba!",
                "Fale uma palavra que ninguém conhece!"
            ]
            return respond(random.choice(challenges))

        if intent_name == "AMAZON.HelpIntent":
            return respond("Você pode me pedir um desafio dizendo: me dê um desafio!")

        if intent_name in ["AMAZON.CancelIntent", "AMAZON.StopIntent"]:
            return respond("Tchau! Volte para mais desafios aleatórios!")

    return respond("Não entendi. Pode repetir?", end_session=False)

def respond(text, end_session=True):
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": text
            },
            "shouldEndSession": end_session
        }
    }
