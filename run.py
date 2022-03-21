import pytest
import os

pytest.main(["cihui100/test_case/",'--alluredir','temp','-n 2'])



# pytest.main(['-vs',"test_run.py"])
os.system('allure generate temp --clean -o report/html')