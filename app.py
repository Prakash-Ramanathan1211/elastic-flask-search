from flask import Flask, render_template, redirect, url_for, request, flash
from elasticsearch import Elasticsearch
import pprint
import os,json

from flask.helpers import flash


app = Flask(__name__)

es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()
path_to_json = 'files/'

app.secret_key = 'enjaamiTale$eFennelda$S'

def search_item(query_word):
    result = []

    for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
        with open(path_to_json + file_name) as json_file:
            
            data = json.load(json_file)
            
            es.index(index=file_name, id=file_name, body=data)

            body = {

                "query": {
                    "multi_match" : {
                        "query" : str(query_word)
                        
                    }
                },
                "highlight" : {
                    "pre_tags" : [
                        "<b style='color:orange'>"],
                    "post_tags" : [
                        "</b>"
                    ],
                    # "tags_schema" : "styled",
                    "fields":{
                        "*":{}
                    }
                }
            }

            res = es.search(index=file_name, body=body)
            
            if len(res['hits']['hits']) != 0:
                high = "<h5>"
                temp=res['hits']['hits'][0]['highlight']
                for v in list(temp.values())[0]:
                    high += v
                print(high)
                # pprint.pprint(res['hits']['hits'])
                high += "...</h4>"
                result.append(
                    {
                        "location" : file_name,
                        "text" : high
                })
                # print(file_name)
    return result


@app.route('/', methods = ["POST","GET"])
def search():
    if request.method == 'POST':
        query_word = request.form.get('query_word')
        result = search_item(query_word)
        # if len(result) != 0 :
        #     for name in result:
        #         flash(name)
        return render_template("index.html", result = result)
        # return str(result)
    return render_template("index.html")




if __name__ == '__main__': app.run(debug=True)