import os
import logging
import starkbank


class StarkBankAuth:
    
    
    def get_user(self):
        private_key_file = "private_key.pem"
        if not os.path.exists(private_key_file):
            logging.error(f"Private key file not found: {private_key_file}")
            exit(1)

        with open(private_key_file, "r") as file:
            private_key_content = file.read()


        user = starkbank.Project(
            environment="sandbox",
            id="4906907152154624",
            private_key=private_key_content
        )
        return user
        
        