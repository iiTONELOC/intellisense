import os
program_paths = {
    "onenote": "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE",
    "web": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
}


def os_query_handler(query):
    print("OS HANDLER", query)

    prog = query.split('launch', 1)[1].strip() if 'launch' in query \
        else query.split('open', 1)[1]

    if prog == False:
        prog = ''

    if 'onenote' in prog:
        start_file('onenote')
    if 'web browser' in prog:
        start_file('web')
    if 'settings' in prog:
        launch_sys_program('settings')


def start_file(program_name):
    os.startfile(program_paths[program_name])


def launch_sys_program(program_name):
    if program_name == "settings":
        print("Launching settings...")
        os.system("start ms-settings:")
