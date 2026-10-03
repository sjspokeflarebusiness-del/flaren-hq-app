import os
from functools import wraps

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "change-this-local-secret-before-deployment"
)

OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "flaren-admin")
OWNER_PASSWORD_HASH = os.environ.get("OWNER_PASSWORD_HASH", "")


def owner_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get("owner_logged_in"):
            return redirect(url_for("owner_login"))
        return view(*args, **kwargs)

    return wrapped_view


@app.route("/")
def public_home():
    return render_template("public_home.html")


@app.route("/owner-login", methods=["GET", "POST"])
def owner_login():
    if session.get("owner_logged_in"):
        return redirect(url_for("owner_dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        correct_username = username == OWNER_USERNAME
        correct_password = bool(OWNER_PASSWORD_HASH) and check_password_hash(
            OWNER_PASSWORD_HASH,
            password
        )

        if correct_username and correct_password:
            session.clear()
            session["owner_logged_in"] = True
            session["owner_username"] = OWNER_USERNAME
            return redirect(url_for("owner_dashboard"))

        flash("Incorrect username or password.", "error")

    return render_template("owner_login.html")


@app.route("/owner")
@owner_required
def owner_dashboard():
    stats = {
        "active_projects": 3,
        "public_services": 2,
        "private_projects": 1,
        "new_leads": 0,
        "pending_work": 0,
        "monthly_revenue": "₹0",
    }

    return render_template(
        "owner_dashboard.html",
        stats=stats,
        owner_username=session.get("owner_username", "flaren-admin"),
    )


@app.route("/owner-logout")
@owner_required
def owner_logout():
    session.clear()
    return redirect(url_for("public_home"))


if __name__ == "__main__":
    app.run(debug=True)