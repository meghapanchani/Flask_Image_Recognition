"""Flask web application for hand-sign digit recognition."""

import os
import secrets
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, request
from model import preprocess_img, predict_result


# Instantiating Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)
CSRFProtect(app)

# Home route
@app.route("/", methods=["GET"])
def main():
    """Display the homepage with the image upload form."""
    return render_template("index.html")


# Prediction route
@app.route("/prediction", methods=["POST"])
def predict_image_file():
    """Process an uploaded image and display its predicted digit."""
    try:
        uploaded_file = request.files.get("file")

        if uploaded_file is None:
            raise ValueError("No file was uploaded.")

        img = preprocess_img(uploaded_file.stream)
        pred = predict_result(img)
        return render_template("result.html", predictions=str(pred))

    except (KeyError, ValueError, TypeError, OSError) as error:
        app.logger.warning("Image processing failed: %s", error)
        return render_template("result.html", err="File cannot be processed.")


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=False)  # pragma: no cover
