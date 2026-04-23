import os
from datetime import datetime

# Create output folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Generate timestamp
now = datetime.utcnow()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
readable  = now.strftime("%A, %d %B %Y at %H:%M:%S UTC")

# File content
content = f"""Hello from GitHub Actions!
==========================================
Generated on : {readable}
File name    : log_{timestamp}.txt
Status       : Automation is working!
==========================================
"""

# Write the file
filename = f"outputs/log_{timestamp}.txt"
with open(filename, "w") as f:
    f.write(content)

print(f"✅ File created: {filename}")
print(content)
