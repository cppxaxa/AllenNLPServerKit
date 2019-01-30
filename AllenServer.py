from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from allennlp.predictors.predictor import Predictor

app = Flask(__name__)
api = Api(app)

predictor = Predictor.from_path("bidaf-model-2017.09.15-charpad.tar.gz")

parser = reqparse.RequestParser()
parser.add_argument('question')
parser.add_argument('passage')

class MachineComprehension(Resource):
    def get(self):
        return { 'message' : 'helloWorld' }

    def post(self):
        args = parser.parse_args()
        result = predictor.predict(
                    passage=args['passage'],
                    question=args['question']
                )
        #result = { 'best_span_str': 'Hello World 1 ' + str(args['question']) + ' End' }
        return result, 201
    

api.add_resource(MachineComprehension, '/service')

if __name__ == '__main__':
    app.run(host="AllenServer", port=5003)