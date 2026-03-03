f=open("/tmp/bettan_stats.json", "r")

import json
stats = json.load(f)

type(stats)
print(stats)

logged_in= stats["logged_in"]["users"]
