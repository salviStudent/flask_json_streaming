# Small example for streaming endpoint and a generator to consume it.

Made with python and flask.

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
