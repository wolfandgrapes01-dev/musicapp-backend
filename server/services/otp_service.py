from datetime import datetime
import boto3

from utils.otp_utils import OtpDetails

def create_new_otp() -> OtpDetails:
    one_detail = OtpDetails()
    one_detail.generate_otp_details()
    return one_detail

def check_rate_limit(req_create_time: datetime, otp_exp_time: datetime) -> bool:
    return req_create_time < otp_exp_time

def send_otp_sms(phone_number: str, message: str):


    try:
        sns = boto3.client(
            'sns',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            region_name=REGION_NAME
        )
        
        response = sns.publish(
            PhoneNumber = phone_number,
            Message = message,
            MessageAttributes={
                "AWS.SNS.SMS.SMSType": {"DataType": "String", "StringValue": "Transactional"}
            }
        )
        
        print("OTP sent successfully:", response)
        return response

    except Exception as e:
        print("Failed to send SMS:", str(e))
        return None