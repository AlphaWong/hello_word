from sanic import Sanic
from sanic.response import json
from services import times

app = Sanic()


@app.route("/ping")
async def ping(request):
    return json({"success": True})


@app.route("times/now")
async def time(request):
    return json({"success": True, "time": times.current()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
