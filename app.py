from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained pipeline model
model = joblib.load("audi_price_model.pkl")

GBP_TO_INR = 118.0


def format_indian(num):
    """Format a number using the Indian numbering system, e.g. 1000000 -> '10,00,000'."""
    num = int(round(num))
    negative = num < 0
    num = abs(num)
    s = str(num)

    if len(s) <= 3:
        result = s
    else:
        last3 = s[-3:]
        rest = s[:-3]
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.insert(0, rest)
        result = ",".join(parts) + "," + last3

    return f"-{result}" if negative else result


app.jinja_env.filters["indian"] = format_indian

# Upper bound used to scale the valuation gauge (needle + arc fill).
# Values above this are simply shown at full scale.
GAUGE_MAX_INR = 5_000_000
GAUGE_ARC_LENGTH = 251.3  # path length of the semicircle used in the SVG gauge


def gauge_values(prediction_inr):
    """Return (percent, needle_angle_deg, arc_dash_length) for the cockpit gauge."""
    percent = 0.0
    if prediction_inr:
        percent = max(0.0, min(prediction_inr / GAUGE_MAX_INR, 1.0))
    angle = -90 + percent * 180
    dash = percent * GAUGE_ARC_LENGTH
    return round(percent * 100, 1), round(angle, 1), round(dash, 1)


@app.route("/")
def home():
    percent, angle, dash = gauge_values(0)
    return render_template(
        "index.html",
        form_data={},
        gauge_percent=percent,
        gauge_angle=angle,
        gauge_dash=dash
    )


@app.route("/predict", methods=["POST"])
def predict():
    form_data = request.form.to_dict()

    try:
        # Get form data
        model_name = request.form["model"]
        year = int(request.form["year"])
        transmission = request.form["transmission"]

        # User inputs
        mileage_km = float(request.form["mileage"])
        kmpl = float(request.form["mpg"])

        # Convert to dataset units
        mileage = mileage_km / 1.60934      # km → miles
        mpg = kmpl * 2.35215                # km/l → mpg

        fuel = request.form["fuel"]
        engine_size = float(request.form["engine_size"])

        # Default UK road tax
        tax = 145

        # Create input dataframe
        X = pd.DataFrame({
            "model": [model_name],
            "year": [year],
            "transmission": [transmission],
            "mileage": [mileage],
            "fuelType": [fuel],
            "tax": [tax],
            "mpg": [mpg],
            "engineSize": [engine_size]
        })

        # Predict in GBP
        prediction_gbp = model.predict(X)[0]

        # Convert to INR
        prediction_inr = prediction_gbp * GBP_TO_INR
        percent, angle, dash = gauge_values(prediction_inr)

        return render_template(
            "index.html",
            prediction=prediction_inr,
            form_data=form_data,
            gauge_percent=percent,
            gauge_angle=angle,
            gauge_dash=dash
        )

    except Exception as e:
        percent, angle, dash = gauge_values(0)
        return render_template(
            "index.html",
            error=f"Error: {str(e)}",
            form_data=form_data,
            gauge_percent=percent,
            gauge_angle=angle,
            gauge_dash=dash
        )


if __name__ == "__main__":
    app.run(debug=True)