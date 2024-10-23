from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# List to store names
names = []

@app.route('/')
def index():
    # Pass the list of names to the template
    return render_template('index.html', names=names)

@app.route('/submit_name', methods=['POST'])
def submit_name():
    # Get the name from the form
    name = request.form.get('name')
    if name:
        # Store the name in the list
        names.append(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
