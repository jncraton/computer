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

def compute_max_digital_bandwidth(intent):
    """ Computes the maximum digital bandwidth of an analog channel

    Values are computed using theorems from Nyquist and Shannon. In particular:

    2 B \log_2{V}

    B \log_2(1 + {S \over N})

    Examples:

    >>> compute_max_digital_bandwidth("What is the maximum digital bandwidth of an analog channel with a bandwidth of 20MHz that uses 2 discrete signal levels?")
    '40.000 Mb/s'

    >>> compute_max_digital_bandwidth("What is the max digital bandwidth of a channel with an analog bandwidth of 3KHz that uses 8 discrete signal levels?")
    '9000.000 Kb/s'

    >>> compute_max_digital_bandwidth("What is the highest digital bandwidth of an analog channel with a bandwidth of 12MHz and a 30dB signal to noise ratio?")
    '3.867 Mb/s'

    >>> compute_effective_bandwidth("How are you feeling today?")
    Traceback (most recent call last):
    ...
    ValueError: Unable to parse "How are you feeling today?" as a max digital bandwidth intent
    """

    pass

intents = {
    "effective bandwidth": compute_effective_bandwidth,
    "(max|maximum|greatest|largest|highest) digital bandwidth": compute_max_digital_bandwidth,
}

if __name__ == '__main__':
    import doctest
    doctest.run_docstring_examples(compute_max_digital_bandwidth, globals())