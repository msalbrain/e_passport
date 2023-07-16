

app = FastAPI()




@app.post("/signup_new_traveller")
async def add_new_user(
        image: UploadFile = File(...),
        nin: str = Form(...),
        firstname: str = Form("default value  for second"),
):
    return



