import os
import json
from flask import Flask, make_response, g
from flask_restful import Api
from api.ui import UiResource
from api.storage import FilesResource, FileResource

# Create application and set its configuration
app = Flask(__name__)
app.config.from_pyfile(os.path.abspath('settings.py'))

# Create API
api = Api(app)
api.add_resource(UiResource, UiResource.URI)
api.add_resource(FilesResource, FilesResource.URI)
api.add_resource(FileResource, FileResource.URI.format('<name>'))


# ----------------------------------------------------------------------------------------------------------------------
@api.representation('application/json')
def output_json(data, code, headers=None):
    if isinstance(data, dict) or isinstance(data, list) or isinstance(data, str):
        # Only wrap data in JSON string if it's a dictionary. If it's a file
        # stream we directly return it
        response = make_response(json.dumps(data), code)
        response.headers.extend(headers or {})
        return response
    return data


# ----------------------------------------------------------------------------------------------------------------------
@api.representation('text/html')
def output_html(data, code, headers=None):
    response = make_response(data, code)
    response.headers.extend(headers or {})
    return response


# ----------------------------------------------------------------------------------------------------------------------
@app.before_request
def before_request():
    g.config = app.config


if __name__ == '__main__':

    # This code gets executed only if we're doing local testing, so remove the /tmp/files
    # folder where all uploaded files gets stored.
    os.system('rm -f {}/*'.format(app.config['UPLOAD_DIR']))
    
    # Specify host and port number
    host = '0.0.0.0'
    port = 5000

    # Run application
    app.run(host='0.0.0.0', port=5000)
