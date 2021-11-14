import os

from flask import Flask, render_template, request

from ocr_core import ocr_core


UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_folder='./static')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        else:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            print(file)
            # call the OCR function on it
            extracted_text = ocr_core(
                os.path.join(UPLOAD_FOLDER, file.filename))
            print(extracted_text)
            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')


@app.route('/draw', methods=['POST', 'GET'])
def draw():
    if request.method == 'GET':
        return render_template('Draw.html')
    if request.method == 'POST':
        print(request.files['image'])
        file = request.files['image']
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        extracted_text = ocr_core(
            os.path.join(UPLOAD_FOLDER, file.filename))
        print(extracted_text)
        # extract the text and display it
        return render_template('Draw.html',
                               msg='Successfully processed',
                               extracted_text=extracted_text,
                               img_src=UPLOAD_FOLDER + file.filename)


@app.route('/about')
def about():
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True)
