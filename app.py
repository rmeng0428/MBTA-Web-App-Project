from flask import Flask, request, render_template, redirect, url_for
from mbta_helper import find_stop_near

# Initialize the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """
    Renders the home page with an input form.
    """
    return render_template('index.html')

@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    """
    Handles the form submission and renders the result page with the nearest MBTA stop details.
    """
    try:
        place_name = request.form.get('place_name')
        transportation_type = request.form.get('transportation_type')
        if not place_name:
            return render_template('error.html', message="Place name cannot be empty.")

        # Call the find_stop_near function from mbta_helper
        latitude, longitude, station, accessible = find_stop_near(place_name, transportation_type)
        
        if station == "No nearby station found":
            return render_template('error.html', message="No nearby MBTA station found.")

        return render_template(
            'mbta_station.html',
            place_name=place_name,
            latitude=latitude,
            longitude=longitude,
            station=station,
            accessible="Yes" if accessible else "No"
        )
    except ValueError as e:
        return render_template('error.html', message=str(e))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)