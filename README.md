# Small example for streaming endpoint and a generator to consume it.

How it works: we create a file test1.txt with a json array of random numbers on every line of the file. This is done in the file "random_file_generator.py"
We then have a generator read the file line by line and yield the line as a string. The generator is then used by flask's streaming capability. This is done in the file "app.py" On the client side we use requests and it's streaming capabilities to load each json in a generator. This is done in test_json_streaming.py.

First run pipenv install in the directory to make sure the correct dependencies are installed.
```bash
pipenv install
```
Next create the file we wil read to simulate a stream of data.
```bash
pipenv run python3 random_file_generator.py
```

Next start the flask server.
```bash
pipenv run flask run
```
Finally test the server with th following command.
```bash
pipenv run python3 test_json_streaming.py
```
## Notes
The generator that reads the file also sleeps for half a milisecond, this is just to lower cpu usage and is not advised. 
