from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.json  # Get the JSON data from the request

        # Append the new data to the JSON file
        try:
            with open('form_data.json', 'r+') as json_file:
                # Read existing data
                existing_data = json.load(json_file)
                # Add new data to the existing data
                existing_data.append(data)
                # Set the file's current position at the offset
                json_file.seek(0)
                # Write updated data back to the file
                json.dump(existing_data, json_file, indent=4)
        except FileNotFoundError:
            # If file doesn't exist, create it and write the data
            with open('form_data.json', 'w') as json_file:
                json.dump([data], json_file, indent=4)

        return jsonify({"message": "Form data saved successfully!"}), 200

    except Exception as e:
        print(f"An error occurred: {e}")  # Print the error to the server console
        return jsonify({"error": str(e)}), 500

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)