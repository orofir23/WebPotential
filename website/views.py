from flask import Blueprint, render_template, request

from website.models import Member, Duty

views = Blueprint('views', __name__)
members = []  # חברי המחלקה
duties = []  # תורנויות


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/add_member')
def add_member():
    return render_template("add_member.html")


@views.route('/show_members')
def show_members():
    return render_template("show_members.html", members=members)


@views.route('/show_members_form', methods=["POST"])
def show_members_form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    kind = request.form.get("kind")
    m_a = request.form.get("m_a")
    job = request.form.get("job")
    departures = request.form.get("departures")

    members.append(Member(first_name, last_name, kind, m_a, job, departures))

    return render_template("show_members.html", members=members)


@views.route('/add_duty')
def add_duty():
    return render_template("add_duty.html")


@views.route('/show_duties')
def show_duties():
    return render_template("show_duties.html", duties=duties)


@views.route('/show_duties_form', methods=["POST"])
def show_duties_form():
    duty_name = request.form.get("duty_name")
    count = request.form.get("count")

    duties.append(Duty(duty_name, count))

    return render_template("show_duties.html", duties=duties)
