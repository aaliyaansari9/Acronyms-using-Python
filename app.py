from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        phrase = request.form['phrase']
        acronym = generate_acronym(phrase)
        return render_template('result.html', acronym=acronym)
    return render_template('index.html') 
def generate_acronym(phrase):
    input = str(phrase)
    text = input.split()
    acronym = ''
    for i in text:
        acronym = acronym + str(i[0]).upper()
    return(acronym)



if __name__=='__main__':
    app.run()