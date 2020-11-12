from flask import g, Flask, session, request, render_template, redirect, url_for
import time

app = Flask(__name__)
app.secret_key = "snällafungera"

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

a = []

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    global a

    if request.method == 'POST':
        index = int(request.form.get("index"))
        if index <= 50:
            start = float(request.form.get("start"))
            total_time = float(request.form.get("total"))

            if total_time != start:
                a.append(total_time)
                print(total_time)
                pass



            return redirect(f"http://127.0.0.1:5000/page1/{start}/{index+1}")

        else:

            with open("values.txt", "w") as file:
                file.truncate(0)
                b = [str(i) + '\n' for i in a]
                file.writelines(b)
            print("Done")
            return "".join(str(a))


@app.route('/page1/<start>/<index>', methods=['GET', 'POST'])
def page1(start, index):
    return render_template("index.html", timefunc=time.time, start=float(start), index=index)


@app.route("/")
def start():
    return redirect(f"http://127.0.0.1:5000/page1/0/0")


if __name__ == "__main__":
    app.run(debug=True)
