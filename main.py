import slack
import os
import time
import schedule

client = slack.WebClient(token=os.environ['slack_token'])


def message_me():
  print("done")
  client.chat_postMessage(
      channel='#general',
      text="Send a weekly notification every Wednesday at 12:00.")


# Call the function immediately
message_me()

# Schedule the message for Wednesdays at 15:16
schedule.every().wednesday.at("15:16").do(message_me)
print("Script is running")

while True:
  schedule.run_pending()
  time.sleep(10)
