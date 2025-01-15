import os
import logging
import starkbank


class StarkBankAuth:
    
    def __init__(self, private_key_file="private_key.pem", environment="sandbox", project_id="4906907152154624"):
        self.private_key_file = private_key_file
        self.environment = environment
        self.project_id = project_id

    def check_private_key_file(self):
        if not os.path.exists(self.private_key_file):
            logging.error(f"Private key file not found: {self.private_key_file}")
            exit(1)

    def read_private_key_file(self):
        with open(self.private_key_file, "r") as file:
            return file.read()

    def create_user(self, private_key_content):
        return starkbank.Project(
            environment=self.environment,
            id=self.project_id,
            private_key=private_key_content
        )

    def get_user(self):
        self.check_private_key_file()
        private_key_content = self.read_private_key_file()
        return self.create_user(private_key_content)