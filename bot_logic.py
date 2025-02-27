import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def facts():
    insfact = ""
    google = ["The first satellite on the moon was the Luna 10 in 1966","The creator of Python was Guido Van Rossum in 1989","The first commercial console of videogames was Magnavox Odyssey in 1972","The fist spreadsheet was VisiCalc in 1979"]
    insfact += random.choice(google)
    return insfact
