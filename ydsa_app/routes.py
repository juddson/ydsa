from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from .extensions import db
from .models import Subscriber
from .forms import JoinForm

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return render_template("index.html", active_page="home")

@bp.route("/join", methods=["GET", "POST"])
def join():
    form = JoinForm()
    if form.validate_on_submit():
        # honeypot check
        if form.website.data:
            flash("Submission blocked.", "error")
            return redirect(url_for("main.join"))

        sub = Subscriber(
            name=form.name.data.strip(),
            email=form.email.data.strip().lower(),
            wants_newsletter=bool(form.wants_newsletter.data),
            consent_ts=datetime.utcnow() if form.wants_newsletter.data else None,
            source="website",
        )
        try:
            db.session.add(sub)
            db.session.commit()
            flash("Thanks for joining! We’ll be in touch soon.", "success")
        except IntegrityError:
            db.session.rollback()
            # already exists: update preferences, don’t throw error
            existing = Subscriber.query.filter_by(email=sub.email).first()
            if existing:
                existing.name = sub.name  # allow name updates
                existing.wants_newsletter = sub.wants_newsletter
                if sub.wants_newsletter and not existing.consent_ts:
                    existing.consent_ts = datetime.utcnow()
                db.session.commit()
                flash("Welcome back! Your preferences were updated.", "success")
        return redirect(url_for("main.join"))
    return render_template("join.html", form=form, active_page="join")

@bp.route("/about")
def about():
    return render_template("about.html", active_page="about")
