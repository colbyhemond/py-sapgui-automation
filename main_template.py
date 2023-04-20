import win32com.client

def SAP_OP():

    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    if not type(SapGuiAuto) == win32com.client.CDispatch:
        return
    else:
        print('SAPGUI Initialized')

    application = SapGuiAuto.GetScriptingEngine
    if not type(application) == win32com.client.CDispatch:
        SapGuiAuto = None
        return
    else:
        print('Application Found')

    connection = application.Children(0)
    if not type(connection) == win32com.client.CDispatch:
        application = None
        SapGuiAuto = None
        return
    else:
        print('Connected to Application')

    session = connection.Children(0)
    if not type(session) == win32com.client.CDispatch:
        connection = None
        application = None
        SapGuiAuto = None
        return
    else:
        print('Connected to Session')
    
    ### START OF GUI AUTOMATION - change anything below this line until the END

    # These 4 lines maximize the session window, navigates to tcode SU01, and places the text HELLO in the User field
    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/tbar[0]/okcd").text = "su01"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = "HELLO"

    ### END OF GUI AUTOMATION - change anything above this line until the START

    session = None
    connection = None
    application = None
    SapGuiAuto = None

SAP_OP()