from flask_restful import Resource


# --------------------------------------------------------------------------------------------------------------------
class UiResource(Resource):
    
    URI = '/'
    
    def get(self):
        return '''
        <html>
            <h1>Upload file</h1>
            <form method=post enctype=multipart/form-data>
                <input type=file name=file>
                <input type=submit value=Upload>
            </form>
        </html>
        '''
