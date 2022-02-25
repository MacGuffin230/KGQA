from flask import Flask, render_template
from flask import request
from service.question_service import question_service_instance

app = Flask("RuohaiKG")


def start_server():
    app.run()


@app.route("/web_index")
def web_index():
    answer = {
        "content": "",
        "question": ""
    }
    return render_template("index.html", answer=answer)


@app.route("/web_answer", methods=["GET", "POST"])
def web_answer():
    question = request.form["question"]
    answer_str = question_service_instance.get_answer(question)
    answer = {
        "question": question,
        "content": answer_str
    }
    return render_template("index.html", answer=answer)


@app.route("/")
def index():
    return render_template("qa_robot.html")


@app.route("/get_answer")
def get_answer():
    question = request.args.get("question")
    answer_str = question_service_instance.get_answer(question)

    return answer_str
