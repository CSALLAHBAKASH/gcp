import functions_framework
from flask import Request  # Import the Request object type

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function."""
    if isinstance(request, dict): # Check if it is a dictionary for local testing
        request = Request.from_values(json=request)  # Create a mock request object

    request_json = request.get_json(silent=True)
    request_args = request.args

    name = "World"

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']

    return 'Hello {}!'.format(name)


# # For local testing ONLY (remove before deploying!)
# if __name__ == '__main__':
#     print(hello_http({"name": "Developer"}))

# gcloud functions deploy hello_http --runtime python39 --trigger-http --source . --region us-central1 --allow-unauthenticated

# curl -X POST -H "Content-Type: application/json" -d '{"name": "Developer"}' https://us-central1-massive-tensor-452009-d2.cloudfunctions.net/hello_http
# curl https://us-central1-massive-tensor-452009-d2.cloudfunctions.net/hello_http?name=Tester