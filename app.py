import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        response = openai.Completion.create(
        engine=model_engine,
        prompt=request.form["question"],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
