from flask import Flask, render_template
import mvc.mvc as mvc

app = Flask(__name__)


@app.route("/")
def main_page():
    items = mvc.read_items(30)
    return render_template('index.html', items=items)

@app.route('/news/<slug>', methods=["POST", "GET"])
def news(slug):
    item = mvc.read_item(slug)
    return render_template('news.html', item=item)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
