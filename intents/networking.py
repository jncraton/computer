import re

def compute_effective_bandwidth(intent):
    """ Computes the effective bandwidth of a storage device being transported

    Examples:

    >>> compute_effective_bandwidth("What is the effective bandwidth of a 6 TB hard drive shipped in 3 days")
    'The effective bandwidth is 0.185 Gb/s'

    >>> compute_effective_bandwidth("Calculate the effective bandwidth of 1 PB of tapes transported in 1 week")
    'The effective bandwidth is 13.228 Gb/s'

    >>> compute_effective_bandwidth("What is the effective bandwidth of a 700MB CD delivered in 1 minute?")
    'The effective bandwidth is 0.093 Gb/s'

    >>> compute_effective_bandwidth("How much effective bandwidth does a 100 GB Blu-ray disk mailed in 16 hours have?")
    'The effective bandwidth is 0.014 Gb/s'

    >>> compute_effective_bandwidth("How are you feeling today?")
    Traceback (most recent call last):
    ...
    ValueError: Unable to parse "How are you feeling today?" as an effective bandwidth intent
    """

    pass
