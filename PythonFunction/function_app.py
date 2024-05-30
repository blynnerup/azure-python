import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.function_name('FirstHTTPFunction')
@app.route(route="myroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Starting first function.')
    return func.HttpResponse(
        "This is a message from the function!",
        status_code=200
    )

@app.function_name('SecondHTTPFunction')
@app.route(route="mypost", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Starting second function.')

    name = req.params.get('name')
    if name:
        message = f"Hello, {name}, so glad this works!"
    else:
        message = "Hello, stranger"

    d = req.get_body()
    new_msg = json.loads(d)
    logging.info(new_msg)

    return func.HttpResponse(
        new_msg['test'],
        status_code=200
    )

@app.function_name('FailsWithoutBody')
@app.route(route='failbody', auth_level=func.AuthLevel.ANONYMOUS)
def fail_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Starting failure function')

    body_content = req.get_body()
    logging.info(body_content)
    if not body_content:
        try:
            body_content = req.get_json()
        except:
            logging.info('failed')
            return func.HttpResponse(
                'No data',
                status_code=400
            )
    
    return func.HttpResponse(
        'Ok',
        status_code=200
    )
  