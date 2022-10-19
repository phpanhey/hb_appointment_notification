#  🤖🤖 hb appointment notification 🤖🐍
You are willing to book an appointment at 'BürgerServiceCenter-Mitte' but there's no appointment at all ? All you want is to apply for a new passport. There's a simple fix.
***hb appointment notification*** notifies you when there's a free appointment. Just use the script periodically e.g. crontab.
 ## usage
 ```bash
 python3 hb_appointment_notification.py --loc_nr {loc_nr} --cnc_nr {cnc_nr} --startdate 01.01.22 --enddate 31.12.30 --telegramtoken {telegramtoken} --telegramchatid {telegramchatid}
 ```

 ## explanation specital params loc_nr and cnc_nr

`loc_nr` is the location number e.g. 'BürgerServiceCenter-Mitte' results in loc_nr 535.

`cnc_nr` is the service number e.g. 'Wohnsitz ummelden (Alleinige, Haupt- oder Nebenwohnung)' results in cnc_nr 7329.

Please go to https://termin.bremen.de/termine/ and click the location and service you're searching an appointment in order to find `loc_nr` and`cnc_nr`.


