import requests
import datetime


pincode = "452001"
age = 23
no_of_days = 3

present = datetime.datetime.today()
date_list = [present + datetime.timedelta(days= i) for i in range(no_of_days)]
date_str = [i.strftime("%d-%m-%Y") for i in date_list]

for inp_date in date_str:
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={inp_date}"
    response = requests.get(url)
    if response.ok:
        resp_json = response.json()
        if resp_json["sessions"]:
            print(f"Available on: {inp_date}")
            for session in resp_json["sessions"]:
                if session["min_age_limit"] <= age:
                    print("Hospital name: ",session["name"])
                    print("Area: ", session["block_name"])
                    print("Capacity: ", session["available_capacity"])
                    print("Fee Type: ", session["fee_type"])
                    print("Address: ", session["address"])
                    if session["vaccine"] != "":
                        print("Vaccine type: ", session["vaccine"])
                    print("\n\n\n")

        else:
            print(f"No available slots on {inp_date}")



