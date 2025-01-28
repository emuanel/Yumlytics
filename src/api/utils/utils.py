import requests

from config import settings

def check_task_existance(document_id: str) -> bool:
    r = requests.get(
        f"{settings.flower_url}/api/task/info/{document_id}",
        auth=(settings.flower_user, settings.flower_password),
    )
    if str(r.status_code) == "404":
        return False
    else:
        return True
