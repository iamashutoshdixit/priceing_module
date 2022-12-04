from flask import Flask, request
from flask_cors import CORS, cross_origin
import models, utils, traceback



app = Flask(__name__)
cors=CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"



@app.route("/")
def index():
    return "Server is up and running!"


@app.route("/fare/")
def get_fare(db=models.session()):
    try:
        args = dict(request.args)
        distance = float(args["distance"])
        duration = float(args["ride_time"])
        
        

        db_dab = db.query(models.BaseDistancePrice).all()
        
        db_dap = db.query(models.DistanceAddition).all()
        

        db_duration  = db.query(models.TimeFactor).all()

        db.close()

        if db_dab == []:
            return {"detail":"no base distance price found, please add first"}, 404
        if db_dap == []:
            return {"detail":"no distance additional price found, please add first"}, 404
        if db_duration == []:
            return {"detail":"no duration price found, please add first"}, 404

        if distance<=0:
            return {"detail":"invalid distance parameter"}, 400
        
        if duration<=0:    
            return {"detail":"invalid duration parameter"}, 400


        db_dap = db_dap[0]
        time_obj = utils.get_duration(db_duration, duration)
        TBP = time_obj.time_multiplier



        db_obj = utils.get_DAB(db_dab, distance)

        if db_obj.distance >= distance:
            fare = utils.calcluate_fare(0, db_obj.fare, db_dap.fare, TBP)
        else:
            add_dist = distance - db_obj.distance
            fare = utils.calcluate_fare(add_dist, db_obj.fare, db_dap.fare, TBP)
        
        fare = round(fare, 2)
        return {"message":"sucessful","fare":fare}, 200

    except Exception as e:
        traceback.print_exc()
        err= str(e)
        return {"detail":err}, 400


# route for updating distance addition price
@app.route("/admin/update/dap/", methods = ["PUT"])
def update_dap(db = models.session()):
    try:
        payload = request.get_json()
        price = payload["price_per_km"]

        if float(price)<0:
            
            return {"detail":"invalid distance addition price"}, 400

        db_dap = db.query(models.DistanceAddition).all()
        
        if db_dap == []:
            new_dap = models.DistanceAddition(distance = 1, fare = float(price))
            db.add(new_dap)
            
        else:
            db_dap[0].fare = float(price)
        db.commit()
        db.close()
        return {"message":"new distance additional price updated sucessfully"}, 201
    
    except Exception as e:
        traceback.print_exc()
        err = str(e)
        return {"detail":err}, 400

# route for updating distance base price
@app.route("/admin/update/dbp/", methods = ["PUT"])
def update_dbp(db = models.session()):
    try:
        payload = request.get_json()
        price = payload["base_price"]
        dist = payload["base_distance"]

        if float(price)<0:
            
            return {"detail":"invalid distance base price"}, 400
        if float(dist)<=0:
            
            return {"detail":"invalid base distance"}, 400

        db_dbp = db.query(models.BaseDistancePrice).filter(
                                                        models.BaseDistancePrice.distance == float(dist)
                                                        ).all()
        
        if db_dbp == []:
            new_dbp = models.DistanceAddition(distance = float(dist), fare = float(price))
            db.add(new_dbp)
            
        else:
            db_dbp[0].fare = float(price)
            db_dbp[0].distance = float(dist)
        db.commit()
        db.close()
        return {"message":"new distance base price updated sucessfully"}, 201
    
    except Exception as e:
        traceback.print_exc()
        err = str(e)
        return {"detail":err}, 400




if __name__ == "__main__":
    app.run(debug=True)