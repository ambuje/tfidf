import os
import json
from flask import Flask, request
from werkzeug.utils import secure_filename
from controller.tf_idf import tfidf, cosine_similarity, read_doc
from controller.utils import loadnp, loadnp_file

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return "Runing"


@app.route('/files', methods=['POST'])
def files():
    if request.files is None:
        return {"Message": "No Parameters Passed", "Status": "Error"}

    if 'file' not in request.files:
        return {"Message": "No file uploaded", "Status": "Error"}

    files = request.files.getlist('file')

    for file in files:
        if not allowed_file(file.filename):
            return {"Message": "Incorrect File Format uploaded",
                    "Status": "Error"}

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            read_doc()
    return {"Message": "File Uploaded successfully ", "Status": "Success"}


@app.route('/input', methods=['POST'])
def input_string():

    if len(os.listdir('./tfidfvectors')) == 0:
        return {"Message": "Please upload file first", "Status": "Error"}

    if request.json is None:
        return {"Message": "No Parameters Passed", "Status": "Error"}

    if 'input' not in request.json:
        return {"Message": "Invalid request", "Status": "Error"}

    inp_str = request.json['input']

    if len(inp_str) == 0:
        return {"Message": "Invalid Input", "Status": "Error"}

    tfidf_inp = tfidf([inp_str])
    s = loadnp()
    file_nm = loadnp_file()
    out = {}

    for i in range(0, len(s)):

        out[file_nm[i]] = cosine_similarity(tfidf_inp[0], s[i])
    return {"Data": json.dumps(out),
            "Message": "Data Published Successfully",
            "Status": "Success"}


if __name__ == '__main__':
    app.run(debug=True)
