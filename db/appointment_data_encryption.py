from cryptography.fernet import Fernet

from db.secret_fernet_key import SECRET_FERNET_KEY


class DataEncryptor:

    def __init__(self):
        super().__init__()

        self.fernet = Fernet(SECRET_FERNET_KEY)

    def encrypt_data(self, data_for_encryption: str) -> str:
        return self.fernet.encrypt(data_for_encryption.encode()).decode() if data_for_encryption else None
