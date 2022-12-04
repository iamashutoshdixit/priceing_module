# pricing_module
Instructions
1. Run requirements.txt file in the project folder to install all the dependencies -- ``` pip install -r requirements.txt ```
2. Run main.py file to start the server in at "http://localhost:5000"
# API Routes
1. To get the fare - http://localhost:5000/fare/?distance=3.6&ride_time=3.4, GET
2. To update distance base price -"http://localhost:5000/admin/update/dbp/", PUT 

   sample_payload ->{
    "base_price":10,
    "base_distance":3.5
}
3. To update distance additional price -"http://localhost:5000/admin/update/dap/", PUT
    
    sample_payload ->{
    "price_per_km":10
} 
