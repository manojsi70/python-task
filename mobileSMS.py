import subprocess

def send_sms(phone_number, message):
    adb_command = f"adb shell service call isms 7 i32 1 s16 \"com.android.mms.service\" s16 \"{phone_number}\" s16 \"null\" s16 \"{message}\" s16 \"null\" s16 \"null\""
    subprocess.run(adb_command, shell=True, check=True)

# Example usage
phone_number = "+917088642875" 
message = "Hello, this is a test message from Python"
send_sms(phone_number, message)
