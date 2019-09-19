import sys
import re

from intents import arithmetic, networking

intents = {**arithmetic.intents, **networking.intents}

def get_intent_handler(intent):
    """ Pareses an intent and calls the appropriate intent processor 
    
    >>> get_intent_handler("What is 2 + 2").__name__
    'compute_addition_result'
    >>> get_intent_handler("What is 18 plus 6").__name__
    'compute_addition_result'
    >>> get_intent_handler("2+2").__name__
    'compute_addition_result'
    """
    
    for pattern in intents.keys():
        if re.search(pattern, intent, flags=re.I):
            return intents[pattern]
    
    return None

def handle_intent(intent):
    """ Handles an intent

    >>> handle_intent("What is 2+2?")
    '2 + 2 = 4'
    """
    handler = get_intent_handler(intent)

    if not handler:
        raise RuntimeError(f'No handler found for "{intent}"')

    return handler(intent)
    