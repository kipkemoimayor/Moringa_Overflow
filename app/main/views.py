from . import main
from flask import render_template
import markdown2

@main.route("/")
def index():
    title="Welcome to Moringa flow"

    return render_template("index.html",title=title)

@main.route('/review/<int:id>')
def single_review(id):
    review=Review.query.get(id)
    if review is None:
    abort(404)
    format_review = markdown2.markdown(review.Overflow_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)
