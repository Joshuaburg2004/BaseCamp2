class PasswordManager:
    def __init__(self, old_passwords=[]) -> None:
        self.old_passwords = old_passwords

    def get_password(self):
        old_passwords = self.old_passwords
        current_password = old_passwords[len(old_passwords) - 1]
        return current_password

    def set_password(self, password):
        old_passwords = self.old_passwords
        if password in old_passwords:
            return
        old_passwords.append(password)
        self.old_passwords = old_passwords
        return

    def is_correct(self, string=''):
        current_password = self.get_password()
        if string == current_password:
            return True
        return False


def main():
    passwords = PasswordManager(['hello', 'my', 'name', 'is', 'Joshua'])
    passwords.get_password()
    passwords.set_password('No')
    passwords.is_correct('No')


if __name__ == '__main__':
    main()
