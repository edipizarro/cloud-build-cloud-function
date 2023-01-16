from os import getenv
from random import randint
import json

import functions_framework
from google.cloud import tasks_v2 as tasks
from dotenv import load_dotenv
load_dotenv()

@functions_framework.http
def handler(request):
    request_json = request.get_json(silent=True)
    tasks = int(request.args.get('tasks', 1))
    print(request_json)

    PROJECT_ID = getenv('PROJECT_ID')
    LOCATION = getenv('LOCATION')
    TASK_NAME = getenv('TASK_NAME')
    TASK_URL = getenv('TASK_URL')
    SERVICE_ACCOUNT_EMAIL = getenv('SERVICE_ACCOUNT_EMAIL')

    for current_task in range(tasks):
        create_task(PROJECT_ID, LOCATION, TASK_NAME, TASK_URL, SERVICE_ACCOUNT_EMAIL)

    return {'message': f'{tasks} Tasks sent to Cloud Task.'}
    

def create_task(project, location, queue, task_url, service_account_email):
    payload = {
        'first_number': randint(1, 100),
        'second_number': randint(1, 100)
    }                                   # Create payload
    payload = json.dumps(payload)       # Stringify the json payload
    encoded_payload = payload.encode()  # Convert payload to bytes base64

    # Create task
    ## https://cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient
    client = tasks.CloudTasksClient()
    parent = client.queue_path(project, location, queue)
    ## https://cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_create_task
    task = {
        'http_request': {
            'http_method': tasks.HttpMethod.POST,
            'url': task_url,
            'body': encoded_payload,
            'headers': {
                'Content-Type': 'application/json'
            },
            "oidc_token": {
                "service_account_email": service_account_email,
                # "audience": audience,
            },
        }
    }

    response = client.create_task(request={"parent": parent, "task": task})
    print(response)
    return