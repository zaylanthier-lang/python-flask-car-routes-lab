from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Existing car models in the fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route("/")
def home():
    """Default route."""
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def show_model(model):
    
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)
