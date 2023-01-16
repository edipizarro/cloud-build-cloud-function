import functions_framework

@functions_framework.http
def sum_two_numbers(request):
    request_json = request.get_json(silent=True)
    if request_json and 'first_number' in request_json and 'second_number' in request_json:
        first_number = int(request_json['first_number'])
        second_number = int(request_json['second_number'])
    else:
        return {"error", "Malformed json"}, 400
    result = {
        "first_number": first_number,
        "second_number": second_number,
        "result": first_number + second_number
    }
    return result, 200
