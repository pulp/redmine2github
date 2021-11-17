import json
import os
import sys

secrets = json.loads(sys.argv[1])
for key, value in secrets.items():
    print("Setting {key} ...".format(key=key))
    lines = len(value.split("\n"))
    if lines > 1:
        os.system("/bin/bash -c \"echo '{key}<<EOF' >> $GITHUB_ENV\"".format(key=key))
        os.system("/bin/bash -c \"echo '{value}' >> $GITHUB_ENV\"".format(value=value))
        os.system("/bin/bash -c \"echo 'EOF' >> $GITHUB_ENV\"")
    else:
        os.system("/bin/bash -c \"echo '{key}={value}' >> $GITHUB_ENV\"".format(key=key, value=value))
