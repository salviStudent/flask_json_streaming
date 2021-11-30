import requests
import json
import math

def json_iter(url):
    '''Returns an iterator the yields jsons from the provided url.'''
    # the second parameter being "stream=True" is important 
    r = requests.get(url, stream=True)
    # needs to have the right encoding
    if r.encoding is None:
        r.encoding = 'utf-8'
    for line in r.iter_lines(decode_unicode=True):
        # This is essentially going line by line in the response object's
        # content. This is why the return values need to be strings with a
        # newline "\n" at the end for the generator on the API side.
        if line:
            yield json.loads(line)

if __name__ == "__main__":
    # Doing some simple data processing just to simulate stuff actually
    # happening with the data.
    print("Calculating maxium of all random lists, output should be 101")
    print("Small chance it isn't though, just off of probability and stuff.")
    current_max = - math.inf
    for datum in json_iter("http://localhost:5000/data"):
        # There can be empty lists, max throws an empty list if it's passed an
        # empty list so we check it with the if statement
        if datum:
            current_max = max(current_max, max(datum))
    print(f"The current max is: {current_max}")
        

    
    
