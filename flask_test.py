# pip install flask
# pip install xmltodict
import json

from flask import Flask
from flask import Flask, make_response, jsonify, request, render_template
#--------------------------------- 웹 크롤링 관련
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup
from urllib import parse
import pandas as pd


import xmltodict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("test_form.html")

#http://192.168.0.44:8888/get_test?user_id=kim&user_pw=1111
@app.route('/get_test', methods=['get'])
def get_test():
    #search_str = request.form.get('search_str')
    vid = request.args.get("user_id")
    vpw = request.args.get("user_pw")
    print(vid, vpw)
    #------select vname from emp where userid=:vid & userpw=:vpw;
    vname = "SMITH"
    return render_template("test_result.html", MYNAME=vname)

#http://192.168.0.44:8888/post_test
@app.route('/post_test', methods=['post'])
def post_test():
    #search_str = request.form.get('search_str')
    vid = request.form.get("user_id")
    vpw = request.form.get("user_pw")
    print(vid, vpw)
    #------select vname from emp where userid=:vid & userpw=:vpw;
    vname = "SMITH"
    return render_template("test_result.html", MYNAME=vname)

#http://192.168.0.44:8888/post_test
@app.route('/ajax_post_test', methods=['post'])
def ajax_post_test():
    #datas = request.get_data()   # user_id=kim&user_pw=111
    # print(datas)

    vid = request.form.get("user_id")
    vpw = request.form.get("user_pw")
    print(vid, vpw)

    #------select vname from emp where userid=:vid & userpw=:vpw;
    vlist = [{"ENAME":"SMITH",  "SAL":1000},
             {"ENAME":"ALLEN",  "SAL":2000}
             ]
    vlist_str = json.dumps(vlist)
    return vlist_str


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=7777)

