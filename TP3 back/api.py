 # -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pickle
from flask import Flask,request
app=Flask(__name__)
cv=pickle.load(open("Cvmodel.sav",'rb'))
lr=pickle.load(open("Lrmodel.sav",'rb'))
#construction des routes(il est constitue d'un end point et de la methode)
@app.route("/api/8paramdetector/",methods=["POST","GET"])
#on peut appeler la fontion ci bas comme on veut
def detector():
    mail=request.args.get("mail")
    
    mail2 = cv.transform([mail])
    lab = lr.predict(mail2)
    print("Spam" if lab is 1 else "Non Spam")
    
if __name__=="__main__":
    app.run(port=8000,debug=True)
