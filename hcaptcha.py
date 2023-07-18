import requests

def create_task(token, website_url, website_key):
    task_data = {
        "clientKey": token,
        "task": {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": website_url,
            "websiteKey": website_key,
            "minScore": 0.3
        }
    }
    response = requests.post("https://api.capmonster.cloud/createTask", json=task_data)
    task_id = response.json().get("taskId")
    return task_id

def get_captcha_token(token, task_id):
    task_data = {
        "clientKey": token,
        "taskId": task_id
    }
    response = requests.get("https://api.capmonster.cloud/getTaskResult", json=task_data)
    if "processing" in response.text:
        return get_captcha_token(token, task_id)
    else:
        try:
            return response.json()["solution"]["gRecaptchaResponse"]
        except Exception:
            return get_captcha_token(token, task_id)

def hcaptcha():
    token = ""
    website_url = ""
    website_key = ""
    task_id = create_task(token, website_url, website_key)
    captcha_token = get_captcha_token(token, task_id)
    return captcha_token
