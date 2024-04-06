# We are currently in the directory "../exercises"
# There are files called "exercises_1.py" etc until "exercises_53.py"
# Create copy of each file to the directory "../solutions" and rename them to "solutions_1.py" etc until "solutions_53.py"

import shutil
import os

for i in range(16, 54):
    shutil.copy(f"exercise_{i}.py", f"../solutions/solution_{i}.py")
    print(f"exercises_{i}.py copied to solutions_{i}.py")

