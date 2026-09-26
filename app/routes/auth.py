from flask import Blueprint, render_template

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)



@auth_bp.get("/register")
def signup():
    return render_template("auth/register.html")


@auth_bp.get("/login")
def login():
    return render_template("auth/loginn.html")


@auth_bp.get("/employerregister")
def emregister():
    return render_template("auth/emregister.html")

@auth_bp.get("/employerlogin")
def emlogin():
    return render_template("auth/emlogin.html")

@auth_bp.get("/seekerdashboard")
def seekerdashboard():
    # TODO: replace this stub data with a real Supabase/DB lookup for the
    # logged-in user. It's here so the template has everything it needs
    # and doesn't crash with "undefined variable" errors.
    seeker = {"name": "Job Seeker", "profile_completion": 40}
    stages = ["Applied", "Screening", "Interview", "Offer"]
    return render_template(
        "auth/seeker_dashboard.html",
        seeker=seeker,
        applications=[],
        saved=[],
        stages=stages,
        pipeline_counts={},
    )

@auth_bp.get("/employerdashboard")
def employerdashboard():
    # TODO: replace this stub data with a real Supabase/DB lookup for the
    # logged-in employer.
    employer = {"company": "Your Company", "initials": "YC", "color": "#6C5CF5"}
    return render_template(
        "auth/employer_dashboard.html",
        employer=employer,
        my_jobs=[],
        total_apps=0,
        total_views=0,
        shortlisted=0,
    )
    

@auth_bp.get("/plans")
def employerplans():
    return render_template("auth/employer_plans.html")