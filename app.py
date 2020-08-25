from flask import Flask, Response, request, render_template, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # FIXME: this is where the credentials would be checked against the db

        message_content = request.get_json()
        json_dump = json.dumps(message_content)

        return Response(json_dump, status=200, mimetype='application/json')

    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    # Run the app on the IP of your current machine in debug mode
    app.run(host='0.0.0.0', debug=True, threaded=True)