class ComputingDevice:
    """
    Base class for computing devices.
    :param name: name of the device
    :param price: price of the device in dollars and cents (e.g. 10099 for $100.99)
    :param performance: performance of the device in calculations per second
    """

    def __init__(self, name: str, price: int, performance: int):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        self.name = name

        if not isinstance(price, int):
            raise TypeError('Price must be an integer')
        self.price = price

        if not isinstance(performance, int):
            raise TypeError('Performance must be an integer')
        self.performance = performance

    def __str__(self) -> str:
        return f'Name: {self.name}, Price: {self.price}, Power: {self.performance}'

    def __repr__(self) -> str:
        return f'ComputingDevice({self.name}, {self.price}, {self.performance})'

    def execute(self, program: str) -> float:
        """
        Executes a program on the device
        :param program: program to execute
        :return: execution time in seconds
        """
        if not isinstance(program, str):
            raise TypeError('Program must be a string')
        return len(program) / self.performance

    def execute_remote(self, program: str, device: 'ComputingDevice') -> float:
        """
        Executes a program on the device remotely
        :param program: program to execute
        :return: execution time in seconds
        """
        if not isinstance(program, str):
            raise TypeError('Program must be a string')
        if not isinstance(device, ComputingDevice):
            raise TypeError('Device must be a computing device')
        return device.execute(program)


class Laptop(ComputingDevice):
    """
    Laptop is a computing device with a screen and a keyboard
    """

    def __init__(self, name: str, price: int, performance: int, screen_resolution: tuple[int, int], weight: int):
        super().__init__(name, price, performance)

        if not isinstance(screen_resolution, tuple) or len(screen_resolution) != 2 \
                or not isinstance(screen_resolution[0], int) or not isinstance(screen_resolution[1], int):
            raise TypeError('Screen resolution must be a tuple of two integers')
        self.screen_resolution = screen_resolution

        if not isinstance(weight, int):
            raise TypeError('Weight must be an integer')
        self.weight = weight

    def __str__(self) -> str:
        return f'Name: {self.name}, Price: {self.price}, Power: {self.performance}, Screen resolution: {self.screen_resolution}, Weight: {self.weight}'

    def __repr__(self) -> str:
        return f'Laptop({self.name}, {self.price}, {self.performance}, {self.screen_resolution}, {self.weight})'

    def play_game(self, game: str) -> float:
        """
        Plays a game
        :param game: game to play
        :return: game fps
        """
        if not isinstance(game, str):
            raise TypeError('Game must be a string')
        return len(game) / self.performance


class PushButtonPhone(ComputingDevice):
    """
    PushButtonPhone is a computing device with a camera and a screen and a keyboard
    """

    def __init__(self, name: str, price: int, performance: int, camera: int):
        super().__init__(name, price, performance)

        if not isinstance(camera, int):
            raise TypeError('Camera must be an integer')
        self.camera = camera

    def __str__(self) -> str:
        return f'Name: {self.name}, Price: {self.price}, Power: {self.performance}, Camera: {self.camera}'

    def __repr__(self) -> str:
        return f'PushButtonPhone({self.name}, {self.price}, {self.performance}, {self.camera})'

    def take_photo(self) -> float:
        """
        Takes a photo
        :return: photo size in megapixels
        """
        return self.camera / 1000000

    def call(self, number: str) -> str:
        """
        Calls a number
        :param number: number to call
        :return: call duration in seconds
        """
        if not isinstance(number, str):
            raise TypeError('Number must be a string')
        return number

    def execute_remote(self, program: str, device: 'ComputingDevice') -> float:
        raise NotImplementedError('Remote execution is not supported by this device')
