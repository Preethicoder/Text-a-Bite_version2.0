import json
import time

import requests
from dateutil.parser import isoparse

from gemini import get_nutrition

# Dictionary to store the latest timestamp for each user
latest_timestamps = {}
USER_DATA_FILE = "user_data.json"


def load_user_data():
    """Load user_data from a JSON file."""
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary
        return {}
    except json.JSONDecodeError:
        # Handle JSON parsing errors
        print("Error: Invalid JSON in the file. Starting with empty user data.")
        return {}


def send_subscribe_message(user_id):
    """Send a subscription welcome message."""
    message = "Welcome! Send a text in the format 'Track | Display qty measure food' to get nutritional info."
    send_an_sms(message, user_id)


def save_user_data(user_data):
    """Save user_data to a JSON file."""
    try:
        with open(USER_DATA_FILE, "w") as file:
            json.dump(user_data, file, indent=4)
    except Exception as e:
        print(f"Error saving user_data to file: {e}")


def send_an_sms(text, user_id):
    """Send an SMS to the specified user."""
    url = "http://hackathons.masterschool.com:3030/sms/send"
    headers = {"Content-Type": "application/json"}
    payload = {
        "phoneNumber": user_id,
        "message": text,
        "sender": ""
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Message sent successfully to {user_id}")
        else:
            print(f"Failed to send message to {user_id}. Status code: {response.status_code}")
        return response
    except Exception as e:
        print(f"An error occurred while sending message to {user_id}: {e}")
        return None


def fetch_data():
    """Fetch new messages and process them."""
    global latest_timestamps
    url = "http://hackathons.masterschool.com:3030/team/getMessages/Text-a-Bite"
    headers = {"Content-Type": "application/json"}

    # Load existing user_data from file
    user_data = load_user_data()

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()

            # Log the raw response for debugging
            # print("API Response:", data)

            # Dictionary to store new messages
            new_messages = {}

            for user_id, messages in data.items():
                # Get the latest timestamp for this user
                last_timestamp = latest_timestamps.get(user_id, None)
                print("last_timestamp", last_timestamp)
                if last_timestamp:
                    try:
                        last_timestamp = isoparse(last_timestamp)
                    except ValueError as e:
                        print(f"Error parsing last timestamp for user {user_id}: {e}")
                        last_timestamp = None  # If parsing fails, reset to None

                # Filter messages for this user based on the timestamp
                if last_timestamp is not None:
                    new_messages[user_id] = [
                        msg for msg in messages
                        if isoparse(msg["receivedAt"]) > last_timestamp
                    ]
                else:
                    # Initialize last_timestamp with the most recent message's receivedAt
                    if messages:
                        latest_message = max(messages, key=lambda x: isoparse(x["receivedAt"]))
                        last_timestamp = isoparse(latest_message["receivedAt"])
                        latest_timestamps[user_id] = last_timestamp.isoformat()
                        new_messages[user_id] = []

                # Update the latest timestamp for this user if new messages exist
                if new_messages[user_id]:
                    latest_timestamps[user_id] = max(
                        isoparse(msg["receivedAt"]) for msg in new_messages[user_id]
                    ).isoformat()
            print("med", new_messages)

            for user_id, messages in new_messages.items():
                for message in messages:
                    text = message['text']
                    if "SUBSCRIBE" in text:
                        send_subscribe_message(text, user_id)
                    elif "Track" in text:
                        if user_id not in user_data:
                            user_data[user_id] = {
                                "phone_number": user_id,
                                "messages": [],  # Store multiple messages
                                "track": True,
                            }
                        # Only add the message if it is not already in the list
                        if message not in user_data[user_id]["messages"]:
                            user_data[user_id]["messages"].append(message)
                        nutrition_value = get_nutrition(text)
                        message = nutrition_value +"\n" + "Calorie of given food is added to Track\n"
                        send_an_sms(nutrition_value, user_id)
                    elif "Display" in text:
                        if user_id in user_data:
                            food_data = [message['text'] for message in user_data[user_id].get("messages", [])]
                            nutrition_value = get_nutrition(food_data, True)
                            send_an_sms(nutrition_value, user_id)
                        else:
                            print(f"No data found for user ID: {user_id}")
                            return []
                    else:
                        nutrition_value = get_nutrition(text)
                        send_an_sms(nutrition_value, user_id)
            # Save the updated user_data to a JSON file
            save_user_data(user_data)

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error during data fetch: {e}")


def main():
    """Main loop to fetch and process messages periodically."""
    while True:
        fetch_data()
        time.sleep(10)


if __name__ == "__main__":
    main()
