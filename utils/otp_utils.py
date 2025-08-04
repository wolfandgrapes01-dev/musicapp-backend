from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import secrets


@dataclass
class OtpDetails:
    otp_code: str = ''    
    create_time: datetime = None
    expiration_time: datetime = None
    message: str = ''

    def __generate_otp(self) -> str:
        return ''.join(str(secrets.randbelow(10)) for _ in range(6))
    
    def generate_otp_details(self):
        # Create otp
        one_time_password = self.__generate_otp()

        # Create current time and expiration time
        create_time = datetime.now(timezone.utc) + timedelta(seconds=5)
        expiration_time = create_time + timedelta(seconds=60)

        # Prepare message
        send_msg = f'Your verification code is: {one_time_password}. Do not share it with anyone.'

        # Update the attributes
        self.otp_code = one_time_password
        self.create_time = create_time
        self.expiration_time = expiration_time
        self.message = send_msg
