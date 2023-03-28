from flask import Flask,render_template,request,session,redirect
app = Flask(__name__)
app.secret_key = 'secret'



@app.route('/')
def index():
    if not 'count' in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/counts', methods=['POST'])
def counts():
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.pop('count')
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/plus2', methods=['POST'])
def plus2():
    session['count'] += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)