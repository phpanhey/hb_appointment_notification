import requests
import argparse
from requests.structures import CaseInsensitiveDict


def main():

    args = parse_args()
    cookie = extract_cookie()
    appointment_markup = get_appointment_markup(cookie,args["startdate"],args["enddate"])
    if appointment_available(appointment_markup):
        print("ich schicke ne benachrichtigung")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--startdate", required=True)
    parser.add_argument("--enddate", required=True)
    parser.add_argument("--telegramtoken", required=True)
    parser.add_argument("--telegramchatid", required=True)
    return vars(parser.parse_args())
    
def extract_cookie():
    url = "https://termin.bremen.de/termine/select2?md=5"
    session = requests.Session()
    session.get(url)
    return session.cookies.get_dict()["TVWebSession"]


def get_appointment_markup(cookie,startdate,enddate):
    url = f"https://termin.bremen.de/termine/suggest?loc=535&mdt=0&cnc-7022=1&filter_date_from={startdate}&filter_date_to={enddate}&suggest_filter=Filtern"
    headers = CaseInsensitiveDict()
    headers["Cookie"] = f"TVWebSession={cookie}"
    resp = requests.get(url, headers=headers)
    return resp.text


def appointment_available(appointment_markup):
    return "Kein freier Termin verfügbar" not in appointment_markup

def telegram_bot_send_text(message):
    bot_token = get_credentials("telegram")["bot_token"]
    bot_chatID = get_credentials("telegram")["bot_chat_id"]
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + message
    )
    response = requests.get(send_text)
    return response.json()


if __name__ == "__main__":
    main()
