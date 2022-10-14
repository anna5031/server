import flask
import werkzeug
 
# Flask Constructor
app = flask.Flask(__name__)
 
# decorator to associate 
# a function with the url
@app.route('/', methods=['GET', 'POST'])
def handle_request():
      # response from the server
  if flask.request.method=='POST':
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    return "Image Uploaded Successfully"
  else:
    return "Oh SHIT PLEASE GOD PLEASE LET ME GO HOME~~~"
 
if __name__ == "__main__":
  app.run(host="0.0.0.0")