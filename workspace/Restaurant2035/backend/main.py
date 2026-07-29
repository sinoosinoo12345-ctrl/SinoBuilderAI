from fastapi import FastAPI

app = FastAPI(title='Sino Builder API')

@app.get('/')
def root():
    return {'status':'running'}
