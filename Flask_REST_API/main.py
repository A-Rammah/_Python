from flask import Flask #, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

# names = {"Abdalla": {"age": 28, "gender": "male"},
#          "Alaa": {"age": 27, "gender": "female"},
#          "Homer": {"age": 29, "gender": "male"},
#          }

# class HelloWorld(Resource):
#     def get(self, name):
#         return names[name]
    
#     def post(self):
#         return {"respone": "posted"}

# api.add_resource(HelloWorld, "/helloworld/<string:name>")
# api.add_resource(HelloWorld, "/helloworld")

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=str, help="Likes on the video", required=True)

videos ={}

def abort_if_exists(video_id):
    if videos[video_id]:
        abort(f"Video {videos[video_id].name} already exists!")
        return

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        print(args)
        # check here if exists

        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)