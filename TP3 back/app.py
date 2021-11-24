import pickle
from flask import Flask,request
from flask_cors import CORS,cross_origin
app=Flask(__name__)
CORS(app)
cv=pickle.load(open("Cvmodel.sav",'rb'))
lr=pickle.load(open("Lrmodel.sav",'rb'))
#construction des routes(il est constitue d'un end point et de la methode)
@app.route("/api/mail/",methods=["GET"])
#on peut appeler la fontion ci bas comme on veut
def detector():
    mail=request.args.get("mail")
    
    mail2 = cv.transform([mail])
    lab = lr.predict(mail2)
    
    return "Spam" if lab is 1 else "Non Spam"
    
if __name__=="__main__":
    app.run(port=8000,debug=True)

