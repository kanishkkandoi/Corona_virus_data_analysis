from flask import Flask,render_template, request
import pandas as pd
app = Flask(__name__)
 
data=pd.read_csv('country_wise_latest.csv')

#Country-Region

def datap():
    return data["Country/Region"]




def details(Country):
    L=data[data['Country/Region']==Country][['Active','Deaths','Recovered']].values.tolist()
    return L[0]

def details2(Country):
    L=data[data['Country/Region']==Country][["Deaths / 100 Cases", "Recovered / 100 Cases",'Deaths / 100 Recovered']].values.tolist()
    return L[0]

@app.route('/', methods=['POST', 'GET'])
def a():
    return render_template('ide1.html',Name= 'Afghanistan', roles=datap(),data=details('Afghanistan'), data2=details2('Afghanistan'))


@app.route("/info",methods=['POST', 'GET'])
def hello_world():
    if request.method=='POST':
        d=request.form.get('D1')
        
        return render_template('ide1.html',Name= d, roles=datap(),data=details(d), data2=details2(d))
        
if __name__ == '__main__':
    
    app.run(debug=True)