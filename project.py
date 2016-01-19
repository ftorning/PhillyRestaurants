from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem, User

app = Flask(__name__)

#File Uploads
from werkzeug import secure_filename
import os

#OAuth
from flask import session as login_session
import random, string

# from oauth2client.client import flow_from_clientsecrets
# from oauth2client.client import AccessTokenCredentials
# from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
#import db_helper

# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
# APPLICATION_NAME = "Philly Restaurants App"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

engine = create_engine('sqlite:///phillyrestaurants.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#API Endpoints (GET Request)

#JSON
#@app.route('/restaurants/<int:restaurant_id>/JSON/')
#def restaurantMenuJSON(restaurant_id):
#    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
#    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
#    return jsonify(MenuItems=[i.serialize for i in items])

#@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/JSON/')
#def restaurantItemJSON(restaurant_id, menu_id):
#    item = session.query(MenuItem).filter_by(id = menu_id).one()
#    return jsonify(MenuItem=[item.serialize])

#Google Auth
#@app.route('/gconnect', methods = ['POST'])
#def gconnect():
    # Validate state token
#    if request.args.get('state') != login_session['state']:
#        response = make_response(json.dumps('Invalid state parameter.'), 401)
#        response.headers['Content-Type'] = 'application/json'
#        return response
    # Obtain authorization code
#    code = request.data.decode('utf-8')

#    try:
        # Upgrade the authorization code into a credentials object
#        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
#        oauth_flow.redirect_uri = 'postmessage'
#        credentials = oauth_flow.step2_exchange(code)
#    except FlowExchangeError:
#        response = make_response(json.dumps('Failed to upgrade the'
#                                            'authorization code.'), 401)
#        response.headers['Content-Type'] = 'application/json'
#        return response

    # Check that the access token is valid.
#    access_token = credentials.access_token
#    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
#           % access_token)
#    h = httplib2.Http()
#    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
#    if result.get('error') is not None:
#         response = make_response(json.dumps(result.get('error')), 500)
#         response.headers['Content-Type'] = 'application/json'

#     # Verify that the access token is used for the intended user.
#     gplus_id = credentials.id_token['sub']
#     if result['user_id'] != gplus_id:
#         response = make_response(json.dumps("Token's user ID doesn't match "
#                                             "given user ID."), 401)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     # Verify that the access token is valid for this app.
#     if result['issued_to'] != CLIENT_ID:
#         response = make_response(json.dumps("Token's client ID does not "
#                                             "match app's."), 401)
#         print "Token's client ID does not match app's."
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     stored_credentials = login_session.get('credentials')
#     stored_gplus_id = login_session.get('gplus_id')
#     if stored_credentials is not None and gplus_id == stored_gplus_id:
#         response = make_response(json.dumps('Current user is already '
#                                             'connected.'), 200)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     # Store the access token in the session for later use.
#     login_session['provider'] = 'google'
#     login_session['credentials'] = credentials.access_token
#     login_session['gplus_id'] = gplus_id
#     # replace full crediential object
#     credentials = AccessTokenCredentials(login_session['credentials'],
#                                          'user-agent-value')

#     # Get user info
#     userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
#     params = {'access_token': credentials.access_token, 'alt': 'json'}
#     answer = requests.get(userinfo_url, params=params)

#     data = answer.json()

#     login_session['username'] = data['name']
#     login_session['image'] = data['picture']
#     login_session['email'] = data['email']

#     # see if user exists, if it doesn't make a new one
#     #user_id = db_helper.get_user_id(login_session['email'])
#     #if not user_id:
#     #    user_id = db_helper.create_user(login_session)
#     #login_session['user_id'] = user_id

#     output = ''
#     output += '<h1>Welcome, '
#     output += login_session['username']
#     output += '!</h1>'
#     output += '<img src="'
#     output += login_session['image']
#     output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
#     flash("You are now logged in as %s" % login_session['username'])
#     print "done!"
#     return output

# # DISCONNECT - Revoke a current user's token and reset their login_session
# @app.route('/gdisconnect')
# def gdisconnect():
#     # Only disconnect a connected user.
#     credentials = AccessTokenCredentials(login_session['credentials'],
#                                          'user-agent-value')
#     if credentials is None:
#         response = make_response(json.dumps('Current user not '
#                                             'connected.'), 401)
#         response.headers['Content-Type'] = 'application/json'
#         return response
#     access_token = credentials.access_token
#     url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
#     h = httplib2.Http()
#     result = h.request(url, 'GET')[0]
#     reason = h.request(url, 'GET')[1]
#     if result['status'] == '200':
#         # Reset the user's sesson.
#         del login_session['credentials']
#         del login_session['gplus_id']

#         response = make_response(json.dumps('Successfully disconnected.'), 200)
#        response.headers['Content-Type'] = 'application/json'
#        return response
#    else:
#        # For whatever reason, the given token was invalid.
#        response = make_response(json.dumps('Failed to revoke token for given '
#                                            'user. reason: '
#                                            '{reason}'.format(reason=reason),
#                                 400))
#        response.headers['Content-Type'] = 'application/json'
#        return response

# @app.route('/login/')
# def showLogin():
#     state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
#     login_session['state'] = state
#     #return "The current session state is %s" % login_session['state']
#     return render_template('login.html', STATE=state)

# File Uploading
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return filename

#Main rsetaurant page and adding new restaurant
@app.route('/')
@app.route('/restaurants/')
def restaurantList():
    restaurants = session.query(Restaurant).order_by(Restaurant.name).all()
    return render_template('restaurantlist.html', restaurants=restaurants)

@app.route('/restaurants/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST' :
        newRestaurant = Restaurant(name = request.form['name'], logo = request.form['logo'], interior = request.form['interior'], link = request.form['link'], neighborhood = request.form['neighborhood'], street = request.form['street'], city = request.form['city'], state = request.form['state'], zipcode = request.form['zipcode'], foodtype =request.form['foodtype'])
        session.add(newRestaurant)
        session.commit()
        flash('New restaurant created!')
        return redirect(url_for('restaurantList'))
    else :
        return render_template('newrestaurant.html')

# #Restaurant specific page with editing restaurant, adding menu item, editing menu item
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    apps = session.query(MenuItem).filter_by(restaurant_id=restaurant.id, course = "Appetizer")
    appscount = apps.count()
    entrees = session.query(MenuItem).filter_by(restaurant_id=restaurant.id, course = "Entree")
    entreescount = entrees.count()
    desserts = session.query(MenuItem).filter_by(restaurant_id=restaurant.id, course = "Dessert")
    dessertscount = desserts.count()
    brunches = session.query(MenuItem).filter_by(restaurant_id=restaurant.id, course = "Brunch")
    brunchescount = brunches.count()
    return render_template('restaurantmenu.html', restaurant=restaurant, apps=apps, entrees=entrees, desserts=desserts, brunches=brunches, appscount=appscount, entreescount=entreescount, dessertscount=dessertscount, brunchescount=brunchescount) 

# @app.route('/restaurants/<int:restaurant_id>/deleterestaurant/', methods=['GET', 'POST'])
# def deleteMenuItem(restaurant_id):
#     #if 'username' not in login_session:
#     #    return redirect('/login/')
#     itemToDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     if request.method == 'POST' :
#         deleteRestaurant = Restaurant(name = request.form['name'], logo = request.form['logo'], interior = request.form['interior'], link = request.form['link'], neighborhood = request.form['neighborhood'], street = request.form['street'], city = request.form['city'], state = request.form['state'], zipcode = request.form['zipcode'], foodtype =request.form['foodtype'])
#         session.delete(deleteRestaurant)
#         session.commit()
#         flash('%s restaurant deleted!' % restaurant.name)
#         return redirect(url_for('restaurantList', restaurant_id = restaurant_id))
#     else :
#         return render_template('deletemenuitem.html', restaurant_id = restaurant_id, item = itemToDelete)

@app.route('/restaurants/<int:restaurant_id>/editrestaurant/', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST' :
        if request.form['name']:
            editedrestaurant.name = request.form['name']
        if request.form['logo']:
            editedrestaurant.logo = request.form['logo']
        if request.form['interior']:
            editedrestaurant.interior = request.form['interior']
        if request.form['link']:
            editedrestaurant.link = request.form['link'] 
        if request.form['neighborhood']:
            editedrestaurant.neighborhood = request.form['neighborhood'] 
        if request.form['street']:
            editedrestaurant.street = request.form['street'] 
        if request.form['city']:
            editedrestaurant.city = request.form['city'] 
        if request.form['state']:
            editedrestaurant.state = request.form['state'] 
        if request.form['zipcode']:
            editedrestaurant.zipcode = request.form['zipcode'] 
        if request.form['foodtype']:
            editedrestaurant.foodtype = request.form['foodtype']
        session.add(editedRestaurant)
        session.commit()
        flash ("%s restaurant edited!" % restaurant.name)
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editrestaurant.html', restaurant_id = restaurant_id, i = editedRestaurant)

@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
#    if 'username' not in login_session:
#        return redirect('/login/')
    if request.method == 'POST' :
        newItem = MenuItem(name = request.form['name'], description = request.form['description'], price = request.form['price'], course = request.form['course'], restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        flash('New menu item created!')
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else :
        return render_template('newmenuitem.html', restaurant_id = restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
#   if 'username' not in login_session:
#       return redirect('/login/')
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST' :
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()
        flash('Menu item edited!')
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else :
        return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id, i = editedItem)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
#    if 'username' not in login_session:
#        return redirect('/login/')
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST' :
        #deleteItem = MenuItem(name = request.form['name'], description = request.form['description'], price = request.form['price'], restaurant_id = restaurant_id)
        session.delete(itemToDelete)
        session.commit()
        flash('Menu item deleted!')
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else :
        return render_template('deletemenuitem.html', restaurant_id = restaurant_id, item = itemToDelete)
    
# def createUser(login_session):
#     newUser = User(name = login_session['username'], email = login_session['email'], picture = login_session['image'])
#     session.add(newUser)
#     session.commit()
#     user = session.query(User).filter_by(email = login_session['email']).one()
#     return user.id

# def getUserInfo(user_id):
#     user = session.query(User).filter_by(id = user_id).one()
#     return user

# def getUserID(email):
#     try:
#         user = session.query(User).filter_by(email = email).one()
#         return user.id
#     except:
#         None

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)