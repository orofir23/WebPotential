from flask import Blueprint, render_template, request

from website.models import Member

views = Blueprint('views', __name__)
members = []  # חברי המחלקה


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/add_member')
def add_member():
    return render_template("add_member.html")


@views.route('/show_members', methods=["POST"])
def show_members():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    kind = request.form.get("kind")
    m_a = request.form.get("m_a")
    job = request.form.get("job")
    departures = request.form.get("departures")

    m = Member(first_name, last_name, kind, m_a, job, departures)
    txt = m.str()

    members.append(Member(first_name, last_name, kind, m_a, job, departures))

    return render_template("show_members.html", members=members)
