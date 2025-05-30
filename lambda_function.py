import random
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

# Categorias de desafios
perguntas_rapidas = [
    "Qual é sua cor favorita?",
    "Quantas letras tem a palavra ‘abacaxi’?",
    "Qual animal faz miau?",
]

desafios_acao = [
    "Pule 3 vezes agora!",
    "Toque o nariz e diga ‘banana’!",
    "Dê uma volta e diga ‘fiz isso!’",
]

imitacoes = [
    "Imite um leão!",
    "Faça o som de um robô!",
    "Finge que você é uma porta rangendo.",
]

criatividade = [
    "Invente uma palavra agora!",
    "Fale uma frase que rime com 'cachorro'!",
    "Invente o nome de um super-herói engraçado.",
]

enigmas = [
    "O que é, o que é: tem dente mas não morde?",
    "Sou grande de dia e sumo à noite. Quem sou eu?",
    "Se você tem 3 maçãs e pega mais 2, quantas tem?",
]

categorias = [
    perguntas_rapidas,
    desafios_acao,
    imitacoes,
    criatividade,
    enigmas,
]

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.object_type == "LaunchRequest"

    def handle(self, handler_input):
        speech = "Bem-vindo ao Desafio Rápido! Preparado para rir e se divertir? Diga 'começar'!"
        return handler_input.response_builder.speak(speech).ask(speech).response

class StartChallengeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.intent.name == "StartChallengeIntent"

    def handle(self, handler_input):
        categoria = random.choice(categorias)
        desafio = random.choice(categoria)
        speech = f"Seu desafio aleatório é: {desafio}"
        return handler_input.response_builder.speak(speech).ask("Qual a sua resposta ou reação?").response

class AnswerIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.intent.name == "AnswerIntent"

    def handle(self, handler_input):
        user_answer = handler_input.request_envelope.request.intent.slots.get("userAnswer", None)
        answer_text = user_answer.value if user_answer and user_answer.value else "Você não respondeu nada!"
        speech = f"Haha! Você disse: {answer_text}. Quer outro desafio maluco?"
        return handler_input.response_builder.speak(speech).ask("Quer mais diversão?").response

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.intent.name == "AMAZON.HelpIntent"

    def handle(self, handler_input):
        speech = "É só dizer 'começar' e eu te lanço um desafio maluco. Vamos lá?"
        return handler_input.response_builder.speak(speech).ask(speech).response

class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        intent_name = handler_input.request_envelope.request.intent.name
        return intent_name in ["AMAZON.CancelIntent", "AMAZON.StopIntent"]

    def handle(self, handler_input):
        return handler_input.response_builder.speak("Valeu por jogar! Até a próxima!").set_should_end_session(True).response

class FallbackHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return True

    def handle(self, handler_input):
        return handler_input.response_builder.speak("Humm, não entendi. Quer tentar outro desafio?").ask("Diga 'começar' para um novo desafio.").response

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(StartChallengeIntentHandler())
sb.add_request_handler(AnswerIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackHandler())

lambda_handler = sb.lambda_handler()
