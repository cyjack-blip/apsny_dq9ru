from flask import Flask, render_template, send_from_directory, request
import mvc.mvc as mvc
from mvc.lib import *
from flask_paginate import Pagination, get_page_parameter


app = Flask(__name__)
app.jinja_env.filters['embed'] = lambda u: get_embed_html_object(u)
app.jinja_env.filters['embed_cover'] = lambda u: get_ebbed_object_cover(u)


@app.route("/", defaults={'page_id': 1}, methods=["POST", "GET"])
@app.route('/index/', defaults={'page_id': 1}, methods=["POST", "GET"])
@app.route('/index/<page_id>/', methods=["POST", "GET"])
def main_page(page_id):
    per_page = 20
    mongo = mvc.Mongo()
    items = mongo.read_items(int(page_id), per_page)
    total = mongo.get_total_items()
    pagination = Pagination(page=page_id, total=total, per_page=per_page, href="/index/{0}/", css_framework='materialize')
    pagination = pagination.links.replace('pagination', 'uk-pagination uk-margin-medium-top').replace('disabled', 'uk-disabled').replace('active', 'uk-active')
    return render_template('index.html', items=items, pagination=pagination)


@app.route('/robots.txt')
@app.route('/yandex_521dd2dc8230be44.html')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/news/<slug>/', methods=["POST", "GET"])
def news(slug):
    item = mvc.read_item(slug)
    return render_template('news.html', item=item)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
