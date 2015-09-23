from flask import Flask , render_template, send_file, request, make_response
from learn import linear_regression, nearest_neighbour, neural_network, clustering, svm
from functools import wraps, update_wrapper
from datetime import datetime
import os
from PIL import Image
import numpy as np
import base64


app = Flask(__name__)
app.debug = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
        
    return update_wrapper(no_cache, view)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/linear_regression')
def linear_reg():
    return send_file(linear_regression.get_data(), mimetype='image/png')

@app.route('/naive_bayes')
def naive_bayes():
    return render_template('naive_bayes.html')

@app.route('/nearest_neighbour')
def nearest_neighbour_func():
    return render_template('nearest_neighbour.html')

@app.route('/nearest_neighbour_image/<int:damage_amount>')
@nocache
def nearest_neighbour_image(damage_amount):
    return send_file(nearest_neighbour.get_damaged_image(damage_amount), mimetype='image/png')

@app.route('/nearest_neighbour_image_repaired')
def nearest_neighbour_image_repaired():
    return send_file(nearest_neighbour.get_repaired_image(), mimetype='image/png')

@app.route('/neural_network',methods=['GET', 'POST'])
def neural_network_func():
    if request.method == 'POST':
        imgdata = base64.b64decode(request.form['img'][22:])
        filename = 'handwritten/tmp.png'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
        im = Image.open(filename)
        im.thumbnail((50,50), Image.ANTIALIAS)
        im.save(filename, "png")
        return 'saved'

        
    else:
        return render_template('neural_network.html')

@app.route('/svm')
def svm_func():
    return render_template('svm.html')

@app.route('/svm_img')
def svm_img():
    return send_file(svm.img(), mimetype='image/png')


@app.route('/clustering')
def clustering_func():
    return render_template('clustering.html')

@app.route('/clustering1')
def clustering_func1():
    return send_file(clustering.image1(), mimetype='image/png')

@app.route('/clustering2')
def clustering_func2():
    return send_file(clustering.image2(), mimetype='image/png')

@app.route('/clustering3')
def clustering_func3():
    return send_file(clustering.image3(), mimetype='image/png')

@app.route('/stock_market')
def stock_market():
    return render_template('stock_market.html')


@app.route('/digits_recognition')
def digits_recognition():
    return render_template('digits_recognition.html')

@app.route('/digits_image')
def digits_image():
    return send_file(neural_network.digits(), mimetype='image/png')


if __name__ == '__main__':
    app.run()