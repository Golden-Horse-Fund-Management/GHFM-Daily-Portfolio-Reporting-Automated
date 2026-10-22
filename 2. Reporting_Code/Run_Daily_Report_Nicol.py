import os
import sys


# 1. Force Python to find Git (Fixes Step 4 executable issue)
os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = r"C:\Program Files\Git\cmd\git.exe"

from git import Repo

# 2. Automatically find the correct project paths relative to this file
# This finds the root folder "GHFM-Daily-Portfolio-Reporting-Automated"
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..")) 

# Define all possible path variables your code framework might look for
repo_path = root_dir
ghfm_reporting_dir = root_dir

# 3. Add the code directory to Python's search path so it can find your module
sys.path.append(os.path.join(root_dir, "2. Reporting_Code"))

# 4. Import your automated framework module
from Report_Module_Automated import PortfolioReportingFramework

# 5. Initialize and run the report
reporter = PortfolioReportingFramework(ghfm_reporting_dir, repo_path)
reporter.run_complete_daily_report()
