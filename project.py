from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog Application"

# Connect to Database and create database session
engine = create_engine('sqlite:///catalogapp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_sesslicationion['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect/', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps
                                 ('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['email'] = data['email']
    loggedIn = True

    return loggedIn


# JSON APIs to view categories Information
@app.route('/catalog/categories/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[category.serialize for category in categories])


# JSON APIs to view items Information
@app.route('/catalog/items/JSON')
def itemsJSON():
    items = session.query(Item).all()
    return jsonify(items=[item.serialize for item in items])


# JSON APIs to view a specific category's items Information
@app.route('/catalog/<path:category_name>/items/JSON')
def categoryItemsJSON(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category_name=category_name).all()
    return jsonify(items=[item.serialize for item in items])


# JSON APIs to a specific item Information
@app.route('/catalog/<path:category_name>/<path:item_name>/JSON')
def itemDetailsJSON(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name=item_name).one()
    return jsonify(item=[item.serialize])


# Show categories
@app.route('/')
@app.route('/catalog/categories/')
def showCategories():
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template('categories.html', categories=categories)


# Show items of a specific category
@app.route('/catalog/<path:category_name>/items', methods=['GET', 'POST'])
def showCategoryItems(category_name):
    if request.method == 'POST':
        redirect(url_for('showLogin'))
    else:
        category = session.query(Category).filter_by(name=category_name).one()
        items = session.query(Item).filter_by(
                                            category_name=category_name).all()
        return render_template('items.html', category=category, items=items)


# Show a specific item in details
@app.route('/catalog/<path:category_name>/<path:item_name>/')
def showItemDetails(category_name, item_name):
    if request.method == 'POST':
        redirect(url_for('showLogin'))
    else:
        category = session.query(Category).filter_by(name=category_name).one()
        item = session.query(Item).filter_by(name=item_name).one()
        return render_template('showitem.html', category=category, item=item)


# Add a new item
@app.route('/catalog/<path:category_name>/items/new/', methods=['GET', 'POST'])
def addNewItem(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        newItem = Item(name=request.form['name'],
                       description=request.form['description'])
        session.add(newItem)
        session.commit()
        redirect(url_for('showCategoryItems', category_name=category_name))
    else:
        return render_template('newitem.html', category=category)


# Edit an item
@app.route('/catalog/<path:category_name>/<path:item_name>/edit/',
           methods=['GET', 'POST'])
def editItem(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    editeditem = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        if request.form['name']:
            editItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editeditem)
        session.commit()
        return redirect(url_for('showItemDetails', category_name=category_name,
                                item=editedItem))
    else:
        return render_template('edititem.html', category_name=category_name,
                               item=editeditem)


@app.route('/catalog/<path:category_name>/<path:item_name>/delete/',
           methods=['GET', 'POST'])
def deleteItem(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    itemToDelete = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showCategoryItems',
                        category_name=category_name))
    else:
        return render_template('deleteitem.html', category_name=category_name,
                               item=itemToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
