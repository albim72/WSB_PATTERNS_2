from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress','queue preparation baking ready')
PizzaDough = Enum('PizzaDough','thin thick')
PizzaSauce= Enum('PizzaSauce','tomato cream_fraiche')
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3

class Pizza:
    def __init__(self,name):
        self.name = name
        self.dough = None
        self.sauce =  None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self,dough):
        self.dough = dough

        print(f'preparing the {self.dough.name} dough of your {self}')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')

class MaragritaBuilder:
    def __init__(self):
        self.pizza = Pizza('Maragrita')
        self.progress = PizzaProgress.queue
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print(f'adding tomato souce to your Margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        topping_desc = 'podwójna mozarella, oregano'
        topping_items = (PizzaTopping.double_mozarella, PizzaTopping.oregano)
        print(f'adding the toping({topping_desc}) to your Margarita')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping({topping_desc}')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your margarita for {self.baking_time} s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('Your Margarita is ready!!!')


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('Creamy Bacon')
        self.progress = PizzaProgress.queue
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print(f'adding creame fraiche souce to your Creamy Bacon...')
        self.pizza.sauce = PizzaSauce.cream_fraiche
        time.sleep(STEP_DELAY)
        print('done with the cream fraiche sauce')

    def add_topping(self):
        topping_desc = 'mozarella, boczek, szynka, grzyby, czerwona cebula, oregano'
        topping_items = (PizzaTopping.mozarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
        print(f'adding the toping({topping_desc}) to your Creamy Bacon')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping({topping_desc}')


    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your creamy bacon for {self.baking_time} s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('Your Creamy Bacon is ready!!!')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self,builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        input_msg = 'What pizza wolud you like, [m]argarita or [c]reamy bacon?'
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg =  'Sorry, only margarita (key m) and creamy bacon (key c) are avaliable'
    return (True,builder)


def main():
    builders = dict(m=MaragritaBuilder, c= CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print("\n")
    waiter= Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza

    print("\n")

    print(f'Enjoy your {pizza}!')

if __name__ == '__main__':
    main()


