import json

# DynamoDB
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

from flask import (Flask, render_template, request, 
                   make_response, url_for, redirect)


app = Flask(__name__)
application = app

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource("dynamodb", region_name='us-east-1')

def get_emotions():
    table = dynamodb.Table('therapme-userData')

    try:
        response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return json.loads(json.dumps(response, indent=4, cls=DecimalEncoder)) 

@app.route('/')
def index():
    # load json data
    with open("./data/steps.json", 'r') as j:
        step_data = json.load(j)

    return render_template(
        'index.html',
        step_data = step_data["activities-steps"],
        emotions_data = get_emotions()["Items"]
    )

if __name__ == '__main__':
    # must set debug=False before public hosting
    app.run(debug=True, host='0.0.0.0', port=8000)

