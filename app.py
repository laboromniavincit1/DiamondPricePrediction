from flask import Flask, request, render_template ,url_for
import joblib
import pandas as pd
app = Flask(__name__)

__pred = None



@app.route('/predict', methods=['GET','POST'] )
def predict():
    if request.method=='GET':
        return render_template('index.html')
    else:
        carat=float(request.form['carat']),
        depth = float(request.form['depth']),
        table = float(request.form['table']),
        x = float(request.form['x']),
        y = float(request.form['y']),
        z = float(request.form['z']),
        cut = request.form['cut'],
        color= request.form['color'],
        clarity = request.form['clarity']
        carat = carat[0]
        depth = depth[0]
        table = table[0]
        x = x[0]
        y = y[0]
        z = z[0]
        cut = cut[0]
        color = color[0]
        clarity = clarity
        print(clarity)
        print(type(cut))
        categories=[{'Fair':1, 'Good':2,'Very Good':3,'Premium':4,'Ideal':5},
                    {'D':1,'E':2,'F':3,'G':4,'H':5,'I':6,'J':7}, 
                    {'I1':1,'SI2':2,'SI1':3,'VS2':4,'VS1':5,'VVS2':6,'VVS1':7,'IF':8} ]
        cut = categories[0][cut]
        color = categories[1][color]
        clarity = categories[2][clarity]
        feature_names = ['carat', 'depth', 'table', 'x', 'y', 'z', 'cut', 'color', 'clarity']
        data = [[carat , depth , table , x, y, z, cut, color, clarity ]]
        global __model
        print('Loading saved model....')
        __model = joblib.load('model.h5')
        print("Model Loaded......")
        new_data = pd.DataFrame(data, columns=feature_names)
        __pred = __model.predict(new_data)
        return render_template('index.html', final_result = __pred)
    

if __name__ == "__main__":
    print("Server Started for DPP....")
    app.run(debug=True)