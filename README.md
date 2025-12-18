# Introduction
https://robotframework.org/
https://robotframework.org/robotframework/
https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
https://robotframework.org/robotframework/latest/libraries/BuiltIn.html

# Git Branch Naming Convention
Branch Name: master
Repo Link: https://github.com/SampreetPattanshetti/saucedemo_ui_automation

# Getting Started
TODO: Install Python and set up python environment. (.evnv)
1. VS code extension
    1.1 Install Python
    1.2 Install RobotCode - Robot Framework Support
2. View -> Command Palette -> Search for Python Create Environment -> Create the Python Enviromnet
3. Create environment in the project directory.
4. Activate the .evnv in your terminal C:\Users\USER\saucedemo_ui_automation\.venv\Scripts\activate.bat (just paste it and enter)
5. Install Requirements.txt (pip install -r requirements.txt)
6. Download Chrome webdriver from here - https://googlechromelabs.github.io/chrome-for-testing/ based on your chrome version.
7. Unzip and add the downloaded webdriver and keep webdriver.exe in the environment -> scripts folder

Step 6 and 7 are not needed.

# Changes needed before running the scripts
1. Add username and password in the constants file, and don't push it to branch.
2. Get the Bearer token from UI.
3. If the test cases fail due to the presence of exisiting test data, the test data to be updated. This could be caused by recent data modifications or newly introduced changes.

# Build and Test
TODO: Open the terminal and select python from the environment created above. Below are the RobotFramework commands to run the testcases.
1. For Test cases file: robot path/to/your/testfile.robot
2. For Test cases from file: robot -t "Test case Name" path/to/your/testfile.robot
3. For Test cases with tag from file: robot -i "Tag Name" path/to/your/testfile.robot
4. For Test cases parallel run: pabot path/to/your/testfile.robot
5. For parallel re-run failed cases and store in the output dir mentioned: pabot --rerunfailed output.xml --outputdir output-path testscases-path.robot
6. Specify output dir: robot --outdir output-path testcases-path.robot

# Present installed/working versions
python                          3.14.2
selenium                        4.39.0
requests                        2.32.5
robotframework                  7.4
robotframework-assertion-engine 3.0.3
robotframework-browser          19.12.3
robotframework-databaselibrary  2.4.0
mysql-connector-python          9.5.0
robotframework-pabot            5.1.0
robotframework-pythonlibcore    4.4.1
robotframework-requests         0.9.7
robotframework-seleniumlibrary  6.8.0
robotframework-stacktrace       0.4.1
robotframework-datadriver       1.11.2
cryptography                    46.0.3