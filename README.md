# SAP GUI Automation via Python Scripting

## Tools needed to test things out:
* VS Code - to edit python scripts and run them
* Python Extension for VS Code
* Python installed on your computer
* SAP Scripting Tracker
* win32com python module installed

### This VSCode tutorial can help get you set up with VS Code, Python Extension for VS Code, and Python Installation:
https://code.visualstudio.com/docs/python/python-tutorial 

### SAP Scripting Tracker:
https://tracker.stschnell.de/#download

#### Enable Scripting in application server and presentation server
##### Application Server
* Login to SAP
* Go to tcode `RZ11`
* Param. Name: `sapgui/user_scripting`, click Display
* Ensure `Current Value` is equal to `TRUE`
* If value not `TRUE`
  * Press Change Value button
  * New value: `TRUE`
  * Switch on all servers: Checked
  * Save

##### Presentation Server
* On SAP Logon Pad, click the top left menu button, and select Options...
* Open the Accessibility & Scripting Node
* Select Scripting node
* Ensure the Installation Section says "Scripting is installed"
* Ensure the User Settings section has
  * Enable Scripting - Checked
  * Notify when a script attaches to SAP GUI - Unchecked
  * Notify when a script opens a connection - Unchecked
  * Show native Microsoft Windows dialogs - Unchecked

Additional details about SAP Scripting Tracker can be found in the documentation within the download

### Installing win32com python module
Open command line or terminal
pip install py32com
If it was installed successfully, it should be available to use in your scripts

# Running this script
Pull this repo into your VS Code editor, and follow the directions in https://code.visualstudio.com/docs/python/python-tutorial