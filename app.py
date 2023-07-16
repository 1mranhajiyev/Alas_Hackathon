import uvicorn
from fastapi import FastAPI
from mobile_notes import MobileNotes
import numpy as np
import pickle
import pandas as pd

import pickle
from mobile_notes import MobileNotes

# 2. Create the app object
app = FastAPI()
pickle_in = open("pipeline.pkl","rb")
pipeline=pickle.load(pickle_in)
# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')

def predict_mobilenotes(data:MobileNotes):
    data = data.dict()
    battery_power=data['battery_power']
    blue=data['blue']
    clock_speed=data['clock_speed']
    dual_sim=data['dual_sim']
    fc=data['fc']
    four_g=data['four_g']
    int_memory=data['int_memory']
    m_dep = data['m_dep']
    mobile_wt=data['mobile_wt']
    n_cores=data['n_cores']
    pc=data['pc']
    px_height=data['px_height']
    px_width = data['px_width']
    ram=data['ram']
    sc_h  = data['sc_h']
    sc_w=data['sc_w']
    talk_time=data['talk_time']
    three_g=data['three_g']
    touch_screen=data['touch_screen']
    wifi=data['wifi']

    prediction = pipeline.predict([[battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi]])
    if(round(prediction[0])==0):
        prediction="Low Cost"
    elif(round(prediction[0])==1):
        prediction="Medium Cost"
    elif(round(prediction[0])==2):
        prediction="High Cost"
    else:
        prediction="Very High Cost"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
