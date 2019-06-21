from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_b0b():
	return 'Hello, Bob!'

if __name__ == "__main__":
	app.run()

