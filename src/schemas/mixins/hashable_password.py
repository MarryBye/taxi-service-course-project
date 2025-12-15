from src.utils.crypto import CryptoUtil

class WithHashablePassword:
    def hash_password(self) -> None:
        if not self.password is None:
            self.password = CryptoUtil.hash_password(self.password)