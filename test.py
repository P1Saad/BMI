from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles 
from fastapi.middleware.cors import CORSMiddleware

# from swagger_ui_bundle import swagger_ui_path
# import pydantic
app = FastAPI(docs_url=None)#,redoc_url=None

app.mount(
    "/swagger-static",
    StaticFiles(directory="C:\MyLibraries\SwaggerUI\dist"),
    name="swagger-static"
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
def Hi():
    return {"message": "Merhaba python 10"}

@app.get("/calculate_bmi")
def calculate_bmi(weight: float,height: float):
    bmi=weight/(height**2)
    if bmi <18.5:
        m ="Low"
    elif 18.5 <= bmi <25:
        m="Normal"
    elif 25<=bmi<30:
        m ="Heigh"
    else:
        m="Danger"
    return {"Your BMI":bmi,"Message":m}

@app.get("/docs",include_in_schema=False)
async def docs():
    return get_swagger_ui_html(
        # openapi_url="/openapi.json",
        openapi_url=app.openapi_url,
        title="API Documentation",
        swagger_js_url="/swagger-static/swagger-ui-bundle.js",
        swagger_css_url="/swagger-static/swagger-ui.css"
    )

#uvicorn test:app --reload --port 8001