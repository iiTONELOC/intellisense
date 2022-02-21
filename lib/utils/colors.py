class Colors:

    @staticmethod
    def red(msg):
        return f"\033[91m{msg}\033[00m"

    @staticmethod
    def green(msg):
        return f"\033[92m{msg}\033[00m"

    @staticmethod
    def cyan(msg):
        return f"\033[96m{msg}\033[00m"

    @staticmethod
    def blue(msg):
        return f"\033[94m{msg}\033[00m"

    @staticmethod
    def magenta(msg):
        return f"\033[95m{msg}\033[00m"

    @staticmethod
    def yellow(msg):
        return f"\033[93m{msg}\033[00m"
