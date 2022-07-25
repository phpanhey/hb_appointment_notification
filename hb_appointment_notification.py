import requests
from requests.structures import CaseInsensitiveDict


def main():
    cookie = extract_cookie()
    appointment_markup = get_appointment_markup(cookie)
    if appointment_available(appointment_markup):
        print("ich schicke ne benachrichtigung")
    else: 
        print("kein Termin")



def extract_cookie():
    url = "https://termin.bremen.de/termine/select2?md=5"
    session = requests.Session()
    response = session.get(url)
    return session.cookies.get_dict()["TVWebSession"]


def get_appointment_markup(cookie):
    url = "https://termin.bremen.de/termine/suggest?loc=535&mdt=0&cnc-7022=1&filter_date_from=25.07.2022&filter_date_to=29.07.2022&suggest_filter=Filtern"
    headers = CaseInsensitiveDict()
    headers["Cookie"] = f"TVWebSession={cookie}"
    resp = requests.get(url, headers=headers)
    return resp.text


def appointment_available(appointment_markup):
    return "Kein freier Termin verfügbar" not in appointment_markup


if __name__ == "__main__":
    main()
