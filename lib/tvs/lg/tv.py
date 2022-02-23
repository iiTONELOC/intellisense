from decouple import config
from .discovery import *
from .connection import *
from .controls import *

IP = config('LG_TV_IP')
KEY = config('LG_TV_KEY')


def app_finder(self, app_name):
    app_manager = ApplicationControl(self.client)
    apps = app_manager.list_apps()
    return ([x for x in apps if app_name in x["title"].lower()][0], app_manager)


def input_helper(self, func):
    # input controls require a connect/disconnect command
    self.inputControls.connect_input()
    func()
    self.inputControls.disconnect_input()


class Remote:
    def __init__(self, tv) -> None:
        super().__init__()
        self.tv = tv

    def turn_off(self):
        system = self.tv.systemControls
        system.power_off()

    def screen_off(self):
        return self.tv.systemControls.screen_off()

    def screen_on(self):
        return self.tv.systemControls.screen_on()

    def launch_app(self, command):
        if len(command.split(' ')) >= 3:
            app, app_manager = app_finder(
                self.tv, command.split('launch')[1].strip())
            return app_manager.launch(app)

    def home_button(self):
        return input_helper(self.tv, lambda: self.tv.inputControls.home())

    def exit_button(self):
        return input_helper(self.tv, lambda: self.tv.inputControls.exit())


class LGTV:
    def __init__(self, name) -> None:
        self.client = WebOSClient(IP)
        self.store = {'client_key': KEY}
        self.connect = lambda: self.client.connect()
        self.register = lambda: self.client.register(self.store)
        self.app_manager = ApplicationControl(self.client)
        self.systemControls = SystemControl(self.client)
        self.inputControls = InputControl(self.client)
        self.tvControls = TvControl(self.client)
        self.name = name
        self.remote = Remote(self)
        # COMMENTED OUT BC THIS TV IS ON A DIFFERENT NETWORK
        # WILL ADD THE CONTROLLER LATER

        # if self.client is not None:
        #     client = self.client
        #     client.connect()
        #     client.register(self.store)
        #     for status in client.register(self.store):
        #         if status == WebOSClient.PROMPTED:
        #             print("Please accept the connection on the TV!")
        #         elif status == WebOSClient.REGISTERED:
        #             print("Registration successful!")
