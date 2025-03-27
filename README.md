<!-- Install python env and package from requiremtns.txt -->
    python -m venv myenv
    Window: cd/myenv/Scripts/active
    pip install -r requirements.tx
    if it send an error relate to pip path -> Ctrl + P -> Select Interpreter -> myenv
<!-- Export all package install to requirements.txt -->
    pip freeze > requirements.txt

<!-- Add the path to use the pytest - when it send and error just copy the path, and run in terminal -->
$env:PYTHONPATH="C:\Users\anhvu\OneDrive\Desktop\android_automate"
$env:PYTHONPATH="C:\Users\anhvu\Desktop\android_automate"

<!-- Pytest.mark - use for test only a single function in a test file -->
1/ At the root directory create pytest.ini
    [pytest]
    markers = 
        test_advance_find_element: Find Test in test_automation_base
        test_click_on_element: Click Test in test_automation_base
2/ Run a single function test:
    pytest -m test_advance_find_element



