class Phone:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.__call_history = []
        self.__text_messages = []

    @property
    def model(self):
        return self.__model

    @property
    def brand(self):
        return self.__brand

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError('Model must be string')
        self.__model = value

    @property
    def call_history(self):
        return self.__call_history

    @property
    def text_messages(self):
        return self.__text_messages

    def clear_call_history(self):
        self.__call_history = []

    def clear_text_messages(self):
        self.__text_messages = []

    @staticmethod
    def validate_number(number: str):
        if not isinstance(number, str):
            raise TypeError('Number must be string')

        if not number.startswith('+380'):
            raise ValueError('Number must starts from +380')

        if len(number) != 13:
            raise ValueError('Incorrect number')

        return True

    def make_call(self, number: str):
        self.validate_number(number)
        self.__call_history.append(number)
        call_info = f'Calling {number}'
        return call_info

    def send_message(self, number: str, text: str):
        self.validate_number(number)
        self.__text_messages.append(f'{number} {text}')
        msg_info = f'sending {number} to {text}'
        return msg_info
