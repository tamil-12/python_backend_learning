from flask import Flask

app = Flask(__name__)


@app.route("/")
def initial_route():
    return "Welcome to home page"


@app.route("/get-details/<int:student_id>", methods=["GET"])
def get_student_details(student_id):
    return f"Details of student with ID {student_id}"


if __name__ == "__main__":
    app.run(debug=True)
