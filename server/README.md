# Getting Started

## Install dependencies

You need python3.7+ and pip installed. Once installed, clone the repo locally and run:  
```bash
$ cd server
$ pip install -r requirements.txt
```

## Running the server and testing

To run the server, use uvicorn (will be automatically installed in the previous step)
```bash
$ uvicorn app:app
```

This will start the server. Note the IP it starts on, and open test.sh in a text editor. Change the HOST variable if the url is different than the one printed by the server.

Once done, open another terminal window and run: 
```bash
$ ./test.sh
```

This will run the tests for saving location and power status remotely.