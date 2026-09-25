from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/jobs")
def jobs():
    # TODO: replace with a real job listing page/query.
    return render_template("index.html")


@main.route("/post-job")
def post_job():
    # TODO: replace with a real "post a job" form for employers.
    return render_template("index.html")


@main.route("/applicants")
def applicants():
    # TODO: replace with a real applicants list for the logged-in employer.
    return render_template("index.html")


@main.route("/pricing")
def pricing():
    # TODO: replace with a real pricing page.
    return render_template("index.html")