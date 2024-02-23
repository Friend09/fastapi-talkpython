# create a simple fastapi
import fastapi
import uvicorn
from typing import Optional

api = fastapi.FastAPI()


# landing page
@api.get("/")
def index():
    body = (
        '<html>'
        "<body style='padding: 10px;'>"
        '<h1>Welcome to the API</h1>'
        '<div>'
        "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>"
        '</div>'
        '</body>'
        '</html>'
    )
    return fastapi.responses.HTMLResponse(content=body)

@api.get('/api/calculate')
def calculate(x: int, y:int, z: Optional[int]=None):
    if z == 0:
        return fastapi.responses.JSONResponse(content={"error": "Error Zero value for Z not allowed"}, status_code=400)

    value = x+y

    if z is not None:
        value /= z

    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }

uvicorn.run(api, host="0.0.0.0", port=8000)
