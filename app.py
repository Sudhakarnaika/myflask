from flask import Flask

# Create an instance of the Flask app
app = Flask(__name__)
print("Hello World")
# Define routes and add your app logic here

# Run the Flask app
if __name__ == '__main__':
    app.run()
