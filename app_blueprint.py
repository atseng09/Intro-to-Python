from flask import Blueprint, render_template

app_blueprint = Blueprint('app_blueprint',__name__)

@app_blueprint.route("/")
def home():
    return render_template("homepage.html")

def root():
   markers=[
   {
   'lat':0,
   'lon':0,
   'popup':'This is the middle of the map.'
    }
   ]
   return render_template('index.html',markers=markers )


# @app_blueprint.route('/about')
# def about():
#     return "About"
