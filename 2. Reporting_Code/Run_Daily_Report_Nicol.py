import os
import sys
from git import Repo

# 1. Force Python to find Git (Fixes Step 4 executable issue)
os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = r"C:\Program Files\Git\cmd\git.exe"

# 2. Automatically find the correct project paths relative to this file
# This finds the root folder "GHFM-Daily-Portfolio-Reporting-Automated"
repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ghfm_reporting_dir = repo_path

# 3. Add the code directory to Python's search path so it can find your module
sys.path.append(os.path.join(repo_path, "2. Reporting_Code"))

# 4. Import your automated framework module
from Report_Module_Automated import PortfolioReportingFramework

# 5. Initialize and run the report
reporter = PortfolioReportingFramework(ghfm_reporting_dir, repo_path)
reporter.run_complete_daily_report()


repo = Repo(root_dir)

from Report_Module_Automated import PortfolioReportingFramework
reporter = PortfolioReportingFramework(ghfm_reporting_dir, repo_path)
reporter.run_complete_daily_report()

# today_str = "20260602"
# previous_day_str = "20260601"
# from Report_Module_Automated_Download import PortfolioReportingFrameworkDownload
# reporter = PortfolioReportingFrameworkDownload(today_str, previous_day_str, ghfm_reporting_dir)
# reporter.run_complete_daily_report()

# from Report_Module_Automated_with_Date import PortfolioReportingFramework

# reporter = PortfolioReportingFramework(today_str, previous_day_str, ghfm_reporting_dir, repo_path)
# reporter.run_complete_daily_report()