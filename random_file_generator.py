import random
import json
import os
from time import sleep


"""
The file created will look like this:

[3,4,59]\n
[5,90,1]\n
[]\n
[1,5,6]\n
.
.
.

"""




def generate_random_number_list(list_len):
    '''Returns a list of random integers from 0-101. The list's length
is specified by the list_len parameter. '''
    return [random.randint(0,101) for _ in range(list_len)]

def generate_random_list_file(file_name, number_of_lists):
    '''
    Creates a file with a random list as described ina
    generate_random_number_list. file_name is the name of the list and 
    number_of_lists is how many lists will be in the file.
    '''
    with open(file_name, "a") as _file:
        for _ in range(number_of_lists):
            _list = generate_random_number_list(random.randint(0,101))
            # json.dumps is short for json.dumpstring, so it creates a string
            # representation of the object you are passing if the object
            # can be represented as a json.
            # in this case it would look something like "[1,9,5]"
            list_string = json.dumps(_list) + '\n'
            _file.write(list_string)

def random_list_generator(file_name):
    '''Returns a lists from a file. The file format is specified above.'''
    with open(file_name, 'r') as f:
        for index, line in enumerate(f):
            #this is just so that the cpu usuage goes down. 
            if (index + 1) % 10 == 0:
                sleep(0.0005)
            yield line
            
if __name__ == "__main__":
    #checks if the file already exists, if it does not then it makes the file.
    if not os.path.isfile('test1.txt'):
        generate_random_list_file('test1.txt', 10000)
    count = 0
    #Just a small sanity that the correct amount of lists got made.
    #Goes through every file in the list and adds 1 to count per iteration.
    for random_list in random_list_generator('test1.txt'):
        count += 1
    #This is an f string
    print(f"Total number of lists: {count}")
    
