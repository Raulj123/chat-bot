import re
import long_responses as long


def message_probabilty(user_message, recongnised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recongnised_words:
            message_certainty += 1

    # find % of recognised words in a user message
    # print(message_certainty)
    percentage = float(message_certainty) / float(len(recongnised_words))
    for word in recongnised_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probabilty(message, list_of_words, single_response, required_words)

    # responses----------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'yuh', 'sup', 'hola', 'bonjour'], single_response=True)
    response('I\'m doing fine, and yourself?', ['how', 'are', 'you'], required_words=['how'])
    response('Thank you, it is cool', ['python', 'is', 'cool'], required_words=['python'])
    response(long.R_EATING, ['what',  'do', 'you', 'eat'], required_words=['eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    return long.unkown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    print('Bot ' + get_response(input('You: ')))
