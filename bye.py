from ray import serve
import requests

# 1: Define a Ray Serve deployment.
@serve.deployment(route_prefix="/")
class MyModelDeployment:
    def __init__(self, msg: str):
        # Initialize model state: could be very large neural net weights.
        self._msg = msg

    def __call__(self, request):
        return {"result": self._msg}


# 2: Deploy the model.
serve.start(http_options={"host": "0.0.0.0", "location": "EveryNode"})
serve.run(MyModelDeployment.bind(msg="Bye!"))

# 3: Query the deployment and print the result.
print(requests.get("http://localhost:8000/").json())