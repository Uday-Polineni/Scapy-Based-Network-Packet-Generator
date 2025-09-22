#!C:\Program Files\Python312\python.exe

import sys
import os

# Output HTTP headers
print("Content-type: text/plain\n")

# Print Python executable
print("Python executable: ", sys.executable)

# Print Python version
print("Python version: ", sys.version)

# Print installed modules
try:
    import pkg_resources
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    print("Installed packages: ")
    for package, version in installed_packages.items():
        print(f"{package}=={version}")
except ImportError:
    print("pkg_resources module is not available to list installed packages.")

# Print environment variables
print("\nEnvironment Variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")
