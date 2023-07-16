
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd


# Read the CSV file
df = pd.read_csv('mobile_phones_Data.csv')
X = df.drop('price_range', axis=1)
y = df['price_range']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
numerical_imputer = ('numerical_imputer', SimpleImputer())
#categorical_imputer = ('categorical_imputer', SimpleImputer(strategy='most_frequent'))
trained_model = ('trained_model', LinearDiscriminantAnalysis())


pipeline = Pipeline([
    numerical_imputer,
    trained_model
])
app=FastAPI()

pipeline.fit(X_train, y_train)
pickle.dump(pipeline, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
# 5. Run the API with uvicorn
#    Will run on http://
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload

# 1. Library imports
import uvicorn ##ASGI
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# 2. Create the app object
app = FastAPI()
# 3. Index route, opens automatically on http://
@app.get('/')
def index():

    return {'message': 'Hello, World'}
# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://
@app.get('/Welcome')
def get_name(name: str):

    return {'choose': f'{name}'}
# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:BankNote):
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
    price_range=data['price_range']
    prediction = pipeline.predict([[battery_power,
    blue,
    clock_speed,
    dual_sim,
    fc,
    four_g,
    int_memory,
    m_dep,
    mobile_wt,
    n_cores,
    pc,
    px_height,
    px_width,
    ram,
    sc_h,
    sc_w,
    talk_time,
    three_g,
    touch_screen,
    wifi]])
    return {
        'prediction': prediction[0]
    }
