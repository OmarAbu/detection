
from tkinter import YView
from flask import Flask, flash, redirect, render_template, session, url_for, jsonify
from flask import Flask, request, redirect, render_template
import os
from flask import Flask, request, render_template, redirect, url_for
from flask import send_from_directory
#from keras.models import load_model
# from moleimages import MoleImages
# import tensorflow as tf
import random
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, LargeBinary
import os
from sys import platform


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['UPLOAD_FOLDER'] = '/tmp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "mysecretkey"
db = SQLAlchemy(app)

#database model passed into the argument
class Image(db.Model):
    #key needs to have unique values; in turn they have to have diff id's
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name" ,db.String(100))
    data = db.Column(db.LargeBinary)
    # db.init_app(app)

    # # Creates the logs tables if the db doesnt already exist
    # with app.app_context():
    #     db.create_all()

    #name = db.Column("name" ,db.String(100))
with app.app_context():
        db.create_all()


proper_files=set(['png', 'jpg', 'jpeg', 'gif'])
def correct_file(filename):
    #gets file name after the .
    if any(filename.name.endswith(ext) for ext in proper_files):
        return True
    else:
        return  " issue with filename {filename.name.endswith(ext)}"

def upload_image(file):
    # Get the image file from the request

    img_data = file.read()
    if file is None:
        return "issue no file "
    
    image = Image(name=file.filename, data=img_data )

    db.session.add(image)
    db.session.commit()

# tems
#this wil find the users directory in the path 
    predict="predict"
    #will get the desktop paortion of a users systems 
    desktop = os.path.expanduser("Desktop")
    # you have to get the home eeviornment or the root directories before you can joint any path
    output = os.environ['HOME']
    beg_path=os.path.join(output, desktop)
    #if predict is not in the users desktop than we create one 
    if not os.path.exists("predict"):
        os.mkdir(predict)
    predict_folder =os.path.join(beg_path, predict)
    
    #make sure directory is being made 
    if not  os.path.isdir(predict_folder): 
        flash("creating directory.... ")
        #make the predict_folder to actuallys tore the image
        os.mkdir(predict_folder)
    #actually writes the image to the folder directory 
    with open(os.path.join(predict_folder, image.name), 'wb') as f:
        f.write(image.data)
    return jsonify({'status': 'success'})

#def prediction(file):



@app.route("/",methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return 'Welcome to administrator page'

@app.route("/feedback")
def feedback():
    return render_template('feedback.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    error=None

    if request.method == 'POST':
        #print(request.files['file'])
        file = request.files["file"]
        file.save(file.filename)
        
        
        # check if the post request has the file part
        if 'file' not in request.files:
            return "no file to return "
            #return redirect(request.url)
            #file is the element imported in the html element txt box 
            #with name "pic"
        
        # if user does not select file, browser also
        # submit a empty part without filename
        if file== '':
            #display to user no file wasinputted
   
         
            return " reload, no file was attatched"
        if file and correct_file(file):
     
        
            upload_image(file)
            error=" finished uploading "
            return redirect(url_for('predict'))
    
    return render_template('upload.html')
  
                      

            
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return redirect(url_for('predict', filename = filename))
        #   #if it gets to the render template that means nothing was properly done 
        
       


# @app.route('/image/<int:image_id>', methods=['GET'])
# def get_image(image_id):
#         image = Image.query.filter_by(id=image_id).first()
#         if image:
#             return send_file(
#                 io.BytesIO(image.data),
#                 mimetype='image/jpeg',
#                 as_attachment=True,
#                 attachment_filename=image.name
#             )
#         else:
#             return jsonify({'error': 'image not found'}), 404



@app.route("/predict")
def predict():
    return render_template("predict.html",title="Predict")
    
@app.route('/feedback', methods=['POST'])
def getFeed():
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('feedback')
    print(f'Name: {name}\nEmail: {email}\nFeedback: {feedback}')
    #goes back to home page
    return("/")

#leads to upload page from user 
@app.route('/upload', methods=['GET'])
def up2():
    if request.method=='GET':
        redirect('upload.html')

@app.route('/github-button')
def github():
    redirect('https://github.com')



# @app.route("/prediction/<filename>",methods=["GET","POST"])
# def prediction(filename):
#     #imported process.py
#     x=predict_img(filename) #imported from process file
#     return render_template('output.html',results=x)




if __name__ == '__main__':
    app.debug = True
    app.run()
