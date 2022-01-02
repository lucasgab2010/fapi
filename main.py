from fapi import FastAP

app = FastAPI()

@app.get("/")
def mensaje():
    return {"hello":"word"}
