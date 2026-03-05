from flask import Flask,render_template,request 

app = Flask(__name__)


@app.route('/')

def home_page():
    return render_template('home.html' , language="python" , projectname = "ecommerce" , number =[1,2,3,4,5]);


@app.route('/about')

def about_page():
    return render_template('about.html' , data='FRamEWoRk' , number =9);



@app.route('/contact')

def contact_page():
    print("my age is ")
    return render_template('contact.html');

#craeting the filter /custome

@app.template_filter('double')

def double_number(n):
    return n*2

if __name__ == '__main__':
    app.run(debug=True)

