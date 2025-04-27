import os
import secrets
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   send_file, session, url_for)

from datetime import datetime, timedelta
from src.genai import generate_topic_content
from g4f.client import Client

# Initialize the G4F client
client = Client()

current_date = str(datetime.now()).split(" ")[0]
date_obj = datetime.strptime(current_date, "%Y-%m-%d")

one_year_ago = date_obj + timedelta(days=1)  # 365, 450
current_date_info = one_year_ago.strftime("%Y-%m-%d")

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", secrets.token_hex(24))

# metainfo
metainfo = dict()
metainfo['type_model']    = ['gpt-4o','gpt-4o-mini']
metainfo['temp_infos']    = ['0.5','0.6','0.7','0.8','0.9']
metainfo['input_content']      = '' #'Latest Techqnology used in AI & ML'
metainfo['generated_response'] = ''

# User data for Demonstration
USERS               = {"admin": "1234"}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if USERS.get(username) == password:
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials, please try again.", "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("home_form_data", None)  # Clear home form data from the session
    session.pop("page_form_data", None)  # Clear page form data from the session
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

# Define a route for the sectoral page
@app.route('/')
def home():
    if "username" in session:
        content_info = {'input_content'      : metainfo['input_content'],     
                        'generated_response' : metainfo['generated_response']
                        }
        return render_template(
            "home.html",
            username=session["username"],
            form_data=metainfo,
            current_date=current_date,
            content_info  = content_info
        )
    
    return redirect(url_for("login"))

@app.route("/submit_home_form", methods=["POST"])
def submit_home_form():
    # Retrieve form data from home.html
    # type_model,temp_info

    model_type_info  = request.form.get('type_model')
    temp_info        = request.form.get('temp_info')
    
    type_model_list = [model_type_info]
    for cols in ['gpt-4o','gpt-4o-mini']:
        if cols not in type_model_list:
            type_model_list.append(cols)

    temp_info_list = [temp_info]
    for cols in ['0.5','0.6','0.7','0.8','0.9']:
        if cols not in temp_info_list:
            temp_info_list.append(cols)

     
    metainfo['type_model']       = type_model_list
    metainfo['temp_infos']       = temp_info_list
    flash("Form submitted successfully for Home page!", "success")
    return redirect(url_for("home"))


@app.route("/topic_info_update", methods=["POST"])
def topic_info_update():
    # Retrieve form data from home.html
    # print(request.form.get('requested_topic_info'))
    
    

    model_name  = metainfo['type_model'][0]
    temps_info   = float(metainfo['temp_infos'][0])

    print(model_name,temps_info)

    metainfo['input_content']      = request.form.get('requested_topic_info')
    generated_response             = generate_topic_content(client     = client, 
                                                            user_input = metainfo['input_content'], 
                                                            model_name = model_name, 
                                                            temp_info  = temps_info)
    
    # print(generated_response['Headline'])
    # print(generated_response['Content'])
    metainfo['generated_response'] = generated_response

    flash("Form submitted successfully for Home page!", "success")
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)