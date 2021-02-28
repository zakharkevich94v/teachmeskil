class MyTime:
    def __init__(self, *args):

        if not args:
            self.hours, self.minutes, self.seconds = 0, 0, 0

        elif type(args[0]) == str and len(args) == 1:
            self.hours, self.minutes, self.seconds = [int(x) for x in args[0].split(':')]

        elif type(args[0]) == int and len(args) == 3:
            self.hours, self.minutes, self.seconds = args

        elif isinstance(args[0], MyTime):
            self.hours = args[0].__dict__['hours']
            self.minutes = args[0].__dict__['minutes']
            self.seconds = args[0].__dict__['seconds']

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        self_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        other_seconds = other.hours * 3600 + other.minutes * 60 + other.seconds
        return self_seconds > other_seconds

    def __lt__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __add__(self, other):
        self_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        other_seconds = other.hours * 3600 + other.minutes * 60 + other.seconds
        total = self_seconds + other_seconds
        hours = total // 3600
        total -= (total // 3600) * 3600
        minutes = total // 60
        total -= (total // 60) * 60
        seconds = total % 60
        return MyTime(hours, minutes, seconds)

    def __sub__(self, other):
        self_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        other_seconds = other.hours * 3600 + other.minutes * 60 + other.seconds
        diff = abs(self_seconds - other_seconds)
        hours = diff // 3600
        diff -= (diff // 3600) * 3600
        minutes = diff // 60
        diff -= (diff // 60) * 60
        seconds = diff % 60
        return MyTime(hours, minutes, seconds)

    def __mul__(self, value):
        self_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        total = self_seconds * value
        hours = total // 3600
        total -= (total // 3600) * 3600
        minutes = total // 60
        total -= (total // 60) * 60
        seconds = total % 60
        return MyTime(hours, minutes, seconds)

    def __repr__(self):
        x = y = z = None
        if self.hours < 10:
            x = 0
        if self.minutes < 10:
            y = 0
        if self.seconds < 10:
            z = 0
        return ''.join(f'{x}{self.hours}:{y}{self.minutes}:{z}{self.seconds}'.split('None'))