import os
from flask import request, g
from flask_restful import Resource
from werkzeug.utils import secure_filename


# --------------------------------------------------------------------------------------------------------------------
class FilesResource(Resource):
    
    URI = '/files'
    
    def get(self):
        return [], 200
    
    def post(self):
        if 'file' not in request.files:
            return {'message': 'No file uploaded'}, 401
        f = request.files['file']
        if f.filename == '':
            return {'message': 'No file selected for upload'}, 401
        if f.filename.split('.', 1).lower() != 'csv':
            return {'message': 'File must be in comma-separated value format'}, 401
        filename = secure_filename(f.filename)
        f.save(os.path.join(g.config['UPLOAD_DIR'], filename))
        return 'Ok'.format(filename), 201
    
    
# --------------------------------------------------------------------------------------------------------------------
class FileResource(Resource):
    
    URI = '/files/{}'
    
    def get(self, name):
        return {}, 200
