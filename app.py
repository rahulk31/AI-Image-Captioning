from flask import Flask, render_template, redirect, request
import CaptionIt

# if __name__ == if __name__ == "__main__":
app = Flask(__name__)

@app.route('/')
def hello():
  return render_template("index.html")


@app.route('/', methods = ['POST'])
def marks():
  if request.method == 'POST':
    f = request.files['userfile']
    path = "./static/"+ f.filename
    f.save(path) 

    caption = CaptionIt.caption_this_image(path)
    caption = caption.capitalize()
    result_dic = {
      'image' : path,
      'caption' : caption
    }

  return render_template("index.html", your_result = result_dic)

if __name__ == '__main__':
  app.run(debug = True)


    