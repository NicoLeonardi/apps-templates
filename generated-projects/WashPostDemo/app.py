from chalice import Chalice

app = Chalice(app_name='washpost-demo')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.schedule('rate(1 hour)')
def every_hour(event):
    print(event.to_dict())
