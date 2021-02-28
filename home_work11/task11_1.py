class Synthesizer:
    def __init__(self, name, color, voices, amount_osc, synthesis_method, manufacturer):
        self.name = name
        self.color = color
        self.voices = voices
        self.__amount_osc = amount_osc
        self.__synthesis_method = synthesis_method
        self.__manufacturer = manufacturer

    def play_c(self):
        """Play c - note 3rd octave"""
        print('Ceeeeeeeeeeee ')

    def puls_width_modulation(self):
        """Run PWD"""
        print('Shhh-Bzzz  krrrrr')

    @property
    def amount_osc(self):
        """Returns oscillators amount"""
        return self.__amount_osc

    @amount_osc.setter
    def amount_osc(self, value):
        """Sets oscillators amount"""
        self.__amount_osc = value

    @property
    def synthesis_method(self):
        """Returns type of synthesis method machine use"""
        return self.__synthesis_method

    @synthesis_method.setter
    def synthesis_method(self, method):
        """Sets type of synthesis method machine use"""
        self.__synthesis_method = method

    @property
    def manufacturer(self):
        """Returns machine manufacturer"""
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, company):
        """Sets machine manufacturer"""
        self.__manufacturer = company


synth_1 = Synthesizer('Machinedrum', 'silver', 16, 16, 'frequency modulation', 'Elektron Music Machines')
synth_2 = Synthesizer('Analog Four', 'black', 4, 2, 'subtractive', 'Elektron Music Machines')


class MyCat:
    def __init__(self, name, color, eye_color, legs, hungry, fav_food, fav_sleep_place):
        self.name = name
        self.color = color
        self.eye_color = eye_color
        self.legs = legs
        self.__hungry = hungry
        self.__fav_food = fav_food
        self.__fav_sleep_place = fav_sleep_place

    def want_eat_at_5am(self):
        """The cat wants to eat in the early morning"""
        if self.__hungry:
            print('Meeeeeooowowww  aaaoow')

    def want_sleep(self):
        """The cat wants to sleep"""
        if not self.__hungry:
            print('Zzz Zzz Zzz')

    @property
    def hungry(self):
        """Returns how hungry cat"""
        return self.__hungry

    @hungry.setter
    def hungry(self, value):
        """Sets hungry value"""
        self.__hungry = value

    @property
    def fav_food(self):
        """Returns cats favourite food"""
        return self.__fav_food

    @fav_food.setter
    def fav_food(self, food):
        """Sets cats fvourite food"""
        self.__fav_food = food

    @property
    def fav_sleep_place(self):
        """Returns cats favourite sleep place"""
        return self.__fav_sleep_place

    @fav_sleep_place.setter
    def fav_sleep_place(self, place):
        """Sets cats favourite sleep place"""
        self.__fav_sleep_place = place


cat_1 = MyCat('Zhook', 'black', 'green', 4, True, 'fish', 'wherever under the sun')


class MyBook:
    def __init__(self, subject, name, author, cover, pages, knowledge):
        self.__subject = subject
        self.__name = name
        self.__author = author
        self.cover = cover
        self.pages = pages
        self.knowledge = knowledge

    def lie_on_the_shelf(self):
        """Retuns boolean value in dependeing by subject"""
        return True if self.__subject == 'belles-lettres' else False

    def give_knowledge(self):
        """Adds value to knowledge attribute"""
        if self.__subject == 'philosophy':
            self.knowledge += 20

    @property
    def subject(self):
        """Returns what subject is the book"""
        return self.__subject

    @subject.setter
    def subject(self, value):
        """Sets subjects book"""
        self.__subject = value

    @property
    def name(self):
        """Returns books title"""
        return self.__name

    @name.setter
    def name(self, value):
        """Sets books title"""
        self.__name = value

    @property
    def author(self):
        """Returns books author"""
        return self.__author

    @author.setter
    def author(self, value):
        """Sets books author"""
        self.__author = value


book_1 = MyBook('philosophy', 'dissemination', 'jacques derrida', 'hard', 605, 20)
book_1.author = 'euklid'
book_1.name = 'begins'
book_1.give_knowledge()


class MyCity:
    def __init__(self, name, country, founding_date, population, square, underground=False):
        self.name = name
        self.country = country
        self.founding_date = founding_date
        self.__population = population
        self.__square = square
        self.__underground = underground

    def enlargement(self):
        """Building up a new district"""
        self.__square += 10
        self.__population += 10000

    def emigration(self):
        """Outflow of population in the absence of metro"""
        if not self.__underground:
            self.__population -= 10000
            self.__square -= 10

    @property
    def population(self):
        """Returns cities population"""
        return self.__population

    @population.setter
    def population(self, value):
        """Sets cities population"""
        self.__population = value

    @property
    def square(self):
        """Returns cities square"""
        return self.__square

    @square.setter
    def square(self, value):
        """Sets cities square"""
        self.__square = value

    @property
    def underground(self):
        """Returns is there a metro in the city"""
        return self.__underground

    @underground.setter
    def underground(self, value):
        """Sets whether the metro will be in the city"""
        self.__underground = value


city_1 = MyCity('minsk', 'belarus', '961', 2000000, 340, True)
city_1.enlargement()


class Oscillator:
    def __init__(self, fine_tune, detune, pwd, sub_osc=False, sub_wave=None, wave='saw', vibrato=False):
        self.fine_tune = fine_tune
        self.detune = detune
        self.pwd = pwd
        self.__sub_osc = sub_osc
        self.__sub_wave = sub_wave
        self.__wave = wave
        self.__vibrato = vibrato

    def sub_puls_wave(self):
        if self.__sub_osc:
            self.__sub_wave = 'pulse'

    def sub_5th(self):
        if self.__sub_osc:
            self.__sub_wave = '5th'

    def high_tone(self):
        if self.fine_tune >= 90:
            print('piiiiiiii')

    def reduce_fine_tune(self):
        self.fine_tune -= 5

    @property
    def sub_osc(self):
        """Returns True if sub oscillator on, False otherwise"""
        return self.__sub_osc

    @sub_osc.setter
    def sub_osc(self, value):
        """Sets sub oscillator on/off"""
        self.__sub_osc = value

    @property
    def sub_wave(self):
        """Returns sub wave form if sub oscillator work"""
        return self.__sub_wave

    @sub_wave.setter
    def sub_wave(self, value):
        """Sets sub oscillators wave form"""
        if self.__sub_osc:
            self.__sub_wave = value

    @property
    def wave(self):
        """Returns oscillators wave form"""
        return self.__wave

    @wave.setter
    def wave(self, form):
        """Sets oscillators wave form"""
        self.__wave = form

    @property
    def vibrato(self):
        """Returns True if vibrato on, False otherwise"""
        return self.__vibrato

    @vibrato.setter
    def vibrato(self, value):
        """Sets vibratos on/off"""
        self.__vibrato = value


osc_1 = Oscillator(63, 0, 7, True, 'pulse', 'triangle')
osc_1.fine_tune = 91
osc_1.reduce_fine_tune()
osc_1.high_tone()