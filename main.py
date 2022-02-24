from lib.alfred.alfred import Alfred


def main():
    a = Alfred()  # instantiate Alfred class
    a.greet_user()  # greet user
    a.run()  # method to run Alfred defaults to voice mode


if __name__ == '__main__':
    main()
