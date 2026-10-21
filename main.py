import uuid
from datetime import datetime, timezone
import time
random_string = str(uuid.uuid4())
while True:
    now = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    print(f"{now}: {random_string}", flush=True)
    time.sleep(5)
