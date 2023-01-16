# GCP Async

## Available Services
Different services that we can use:
 - Cloud Tasks -> Queue
 - Cloud Functions
 - Cloud Pub/Sub
 - Cloud Scheduler
 - Cloud Run

## To consider
 - Identity and Access Management
 - Cloud Logging
 - Monitoring
 - VPC Service Controls

## Implementation

### Overview
We will use Cloud Task Queues and Cloud Functions.
The Cloud Function will be the service that hosts our methods and makes them available through HTTP calls.
The method of the Cloud Function will be encapsulated and sent to the Cloud Task Queue.
The Cloud Task Queue will process the tasks and run the corresponding Cloud Function.

### Cloud Tasks
 - [Documentation](https://cloud.google.com/tasks/docs/)
 - [Python code examples](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/HEAD/appengine/flexible/tasks/snippets.py)
 - Create service account with roles:
    - `Cloud Tasks Enqueuer`
    - `Service Account User`
 - Create Queue
 - Add created service account as member with role `Cloud Task Enqueuer`
    - Role: Cloud Task Enqueuer

### Cloud Function
 - [Documentation](https://cloud.google.com/functions/docs/)
 - Enable API run.googleapis.com

### Other permissions
 - Enable `Identity and Access Management (IAM) API`
 - Enable `Cloud Resource Manager API`
 - Create Service Account for Cloud build with roles:
   - `Cloud Build Service Account`
   - `Cloud Functions Developer`