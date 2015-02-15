from flask import Flask, request, jsonify, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Finalmoon090@localhost/ufosightings'


class Sighting(db.Model):
    __tablename__ = 'sightings'
    id = db.Column(db.Integer, primary_key=True)
    sighted_at = db.Column(db.Integer)
    reported_at = db.Column(db.Integer)
    location = db.Column(db.String(100))
    shape = db.Column(db.String(10))
    duration = db.Column(db.String(10))
    description = db.Column(db.Text)
    lat = db.Column(db.Float(6))
    lng = db.Column(db.Float(6))


"""
Taken from:  https://gist.github.com/1094140
"""




def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function

@app.route('/sightings/', methods=['GET', 'POST'])
@jsonp
def sightings():
    lim = request.args.get('limit', 10)
    off = request.args.get('offset', 0)
    radius = request.args.get('radius', 10)
    location = request.args.get('location', ',')
    lat, lng = location.split(',')


    if lat and lng and radius:
        query = "SELECT id,  location, ( 3959 * acos( cos( radians( %(latitude)s ) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians( %(longitude)s ) ) + sin( radians( %(latitude)s ) ) * sin( radians( lat ) ) ) ) AS distance FROM sightings HAVING distance < %(radius)s ORDER BY distance LIMIT %(limit)s" % {"latitude": lat, "longitude": lng, "radius": radius, "limit": lim}
        results = Sighting.query.from_statement(query).all()

    else:
        results = Sighting.query.limit(lim).offset(off).all()

    json_results = []
    for result in results:
        d = {'sighted_at': result.sighted_at,
             'reported_at': result.reported_at,
             'location': result.location,
             'shape': result.shape,
             'duration': result.duration,
             'description': result.description,
             'lat': result.lat,
             'lng': result.lng}

        json_results.append(d)
    
    return jsonify(items=json_results)
            

@app.route('/sightings/<int:sighting_id>', methods=['GET', 'POST'])
def sightings2(sighting_id):

    result = Sighting.query.filter_by(id=sighting_id).first()


    json_result = {'sighted_at': result.sighted_at,
             'reported_at': result.reported_at,
             'location': result.location,
             'shape': result.shape,
             'duration': result.duration,
             'description': result.description,
             'lat': result.lat,
             'lng': result.lng}

    return jsonify(items=json_result)

if __name__ == '__main__': 
    app.run(debug=True)
