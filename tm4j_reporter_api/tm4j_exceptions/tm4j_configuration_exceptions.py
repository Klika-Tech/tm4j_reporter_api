class TM4JConfigurationException(Exception):
    """
    Class to represent TM4J configuration exceptions
    """

    def __init__(self, message):
        self.message = message
