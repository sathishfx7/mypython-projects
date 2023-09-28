from flask import Flask,request,render_template
import pickle
App=Flask("HousePricePredictionApp")
@App.route("/",methods=['GET', 'POST'])
def firstpage():
    return render_template("index.html")

@App.route("/predicthouseprice",methods=['GET', 'POST'])
def predicthouseprice():
    try:
        mymodel=pickle.load(open(r"C:\Users\91735\OneDrive\Desktop\House Price Prediction Project-2\Code File\Model.sav","rb"))
        modelinput=[int(request.values[i]) for i in "a,b,c,d,e,f,g,h".split(",")]
        predictedprice=mymodel.predict([modelinput])
        return "Predicted price is {}".format(int(predictedprice[0]))
    except:
        return "Kindly Check the inputs"

@App.route("/showpredictedprice",methods=['GET', 'POST'])
def showpredprice():
    data=dict()
    mymodel=pickle.load(open(r"C:\Users\91735\OneDrive\Desktop\House Price Prediction Project-2\Code File\Model.sav","rb"))
    modelinput=[1 if request.values[i]=="yes" else 0 if request.values[i]=="no" else int(request.values[i])  for i in "area,bedrooms,bathrooms,mainroad,guestroom,hotwaterheating,airconditioning,parking,prefarea".split(",")]
    for i in "area,bedrooms,bathrooms,mainroad,guestroom,hotwaterheating,airconditioning,parking,prefarea".split(","):
        if request.values[i]=="yes":
            data[i]=1
        elif request.values[i]=="no":
            data[i]=0
        else:
            data[i]=int(request.values[i])
    predictedprice=mymodel.predict([modelinput])
    data["price"]=int(predictedprice[0])
    return render_template("Result.html",data=data)

if __name__=="__main__":
    App.run(debug=True)