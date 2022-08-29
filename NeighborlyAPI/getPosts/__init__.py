import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://p5mongodblab:d4XEWwWO4VTtVqklcFYBDlmmpKboW285kBm5jSKO1xJJZCASfeKNGIdF6tsB5VsXTJmEXdjFWKaK3Q5PzpxcHA==@p5mongodblab.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@p5mongodblab@"
        client = pymongo.MongoClient(url)
        database = client['p5lab']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)