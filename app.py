import requests
import json

class TrainStatusTracker:
    def __init__(self):
        # Demo API endpoint placeholder
        self.api_url = "https://api.example.com/train-status"

    def fetch_train_status(self, train_number):
        """
        Simulated API call for live train status.
        Replace this logic with real API integration if available.
        """
        print(f"Fetching live status for Train No: {train_number}")

        # Simulated response data
        response_data = {
            "train_number": train_number,
            "train_name": "Mumbai Express",
            "source": "CSMT",
            "destination": "Thane",
            "current_station": "Dadar",
            "next_station": "Kurla",
            "delay": "0 Minutes",
            "status": "Running On Time"
        }

        return response_data

    def display_status(self, data):
        print("\n===== LIVE TRAIN STATUS =====")
        print(f"Train Number   : {data['train_number']}")
        print(f"Train Name     : {data['train_name']}")
        print(f"Source         : {data['source']}")
        print(f"Destination    : {data['destination']}")
        print(f"Current Station: {data['current_station']}")
        print(f"Next Station   : {data['next_station']}")
        print(f"Delay          : {data['delay']}")
        print(f"Status         : {data['status']}")
        print("==============================")

def main():
    tracker = TrainStatusTracker()
    train_number = input("Enter Train Number: ")
    status = tracker.fetch_train_status(train_number)
    tracker.display_status(status)

if __name__ == "__main__":
    main()
