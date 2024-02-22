# create a simple fastapi
import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate():
    value = 5
    return {
        'value': value
    }


uvicorn.run(api)
