from bottle import route, run, response
from services import times


@route("/ping", method="GET")
def ping():
    return {"success": True}


@route("/times/now", method="GET")
def time():
    return {"success": True, "time": times.current()}


@route("/users/<name>")
def user(name="n/a"):
    return {"success": True, "message": "hello {name}".format(name=name)}


if __name__ == "__main__":
    run(host="0.0.0.0", port=4000, debug=True)
