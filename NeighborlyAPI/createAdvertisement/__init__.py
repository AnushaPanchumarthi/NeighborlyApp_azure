import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://p5mongodblab:d4XEWwWO4VTtVqklcFYBDlmmpKboW285kBm5jSKO1xJJZCASfeKNGIdF6tsB5VsXTJmEXdjFWKaK3Q5PzpxcHA==@p5mongodblab.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@p5mongodblab@"
            client = pymongo.MongoClient(url)
            database = client['p5lab']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )