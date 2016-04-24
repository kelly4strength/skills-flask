
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index_page():
    """Show form to fill in for applicants."""

    return render_template("application-form.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    # return render_template("index.html")

@app.route('/application', methods=["POST"])
def application_form():
	"""Show that application was accepted."""

	first_name = request.form.get("firstname")
	last_name = request.form.get("lastname")
	salary_requirement = request.form.get("salaryrequirement")
	position = request.form.get("position")

	return render_template("application-response.html",
		firstname=first_name, 
		lastname=last_name, 
		salaryrequirement=salary_requirement, 
		position=position,
		)

if __name__ == "__main__":
    app.run(debug=True)
