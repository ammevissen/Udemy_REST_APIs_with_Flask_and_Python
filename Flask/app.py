from flask import Flask, jsonify, request, render_template

app=Flask(__name__)

@app.route('/') #end point of request
def home():
    #return("Hello, world!")
    return render_template('index.html') #flask automatically looks into the templates folder

#POST - used to receive data (from the prespective of the server)
#Get - used to send data back only (from the prespective of the server)

stores=[
    {
        'name': 'My Wonderful Store', 
        'items':[
            {
            'name': 'My Item',
            'price': 15.99
            }
        ]
    }
]
#POST /store date: {name:}
@app.route('/store', methods=['POST'])   #by default is "GET"
def create_store():
    request_data=request.get_json()
    new_store={
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string: name>
@app.route('/store/<string:name>') #http://127.0.0.1:5000/store/some_name    some_name will be passed into the function as "name"
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

#GET /store
@app.route('/store') 
def get_stores():
    return jsonify({'stores': stores})  #json must be a dictionary, not a list

#POST /store/<string:name>/{item:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])   #by default is "GET"
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})  

app.run(port=5000)
