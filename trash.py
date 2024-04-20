# import sqlalchemy
# from flask import jsonify

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
# db = SQLAlchemy(app)

# class dbLocations(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nm_525 = db.Column(db.Integer, nullable=False) 
#     nm_680 = db.Column(db.Integer, nullable=False) 
#     nm_740 = db.Column(db.Integer, nullable=False) 
#     nm_980 = db.Column(db.Integer, nullable=False) 
#     nm_1450 = db.Column(db.Integer, nullable=False) 
#     nm_525_amb = db.Column(db.Integer, nullable=False) 
#     nm_680_amb = db.Column(db.Integer, nullable=False) 
#     nm_740_amb = db.Column(db.Integer, nullable=False) 
#     nm_980_amb = db.Column(db.Integer, nullable=False) 
#     nm_1450_amb = db.Column(db.Integer, nullable=False) 
#     longitude = db.Column(db.Integer, nullable=False) 
#     latitude = db.Column(db.Integer, nullable=False) 
#     tree_pos = db.Column(db.String, nullable=False) 

# def read_data():
#     try:
#         # Query all users from the database
#         Locations = dbLocations.query.all()
        
#         # Convert the users to a list of dictionaries
#         users_data = []
#         for location in Locations:
#             location_data = {
#                 "nm_525": location.nm_525,
#                 "nm_680": location.nm_680,
#                 "nm_740": location.nm_740,
#                 "nm_980": location.nm_980,
#                 "nm_1450": location.nm_1450,
#                 "nm_525_amb": location.nm_525_amb,
#                 "nm_680_amb": location.nm_680_amb,
#                 "nm_740_amb": location.nm_740_amb,
#                 "nm_980_amb": location.nm_980_amb,
#                 "nm_1450_amb": location.nm_1450_amb,
#                 "longitude": location.longitude,
#                 "latitude": location.latitude,
#                 "tree_pos": location.tree_pos
#             }
#             users_data.append(location_data)
        
#         # Return the users data as JSON
#         return (jsonify(users_data), 200)
#     except Exception as e:
#         print("Error reading data:", e)
#         return f"Error: {str(e)}", 403