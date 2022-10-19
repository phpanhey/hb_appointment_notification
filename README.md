#  hb appointment notification
checks if there's an appointment (hb buergerservice) in a specific time.
 
 ## usage
 ```bash
 python3 hb_appointment_notification.py --loc_nr {loc_nr} --cnc_nr {cnc_nr} --startdate 01.01.22 --enddate 31.12.30 --telegramtoken {telegramtoken} --telegramchatid {telegramchatid}
 ```

 ## explanation specital params loc_nr and cnc_nr

`loc_nr` is the location number e.g. 'BürgerServiceCenter-Mitte' results in loc_nr 535.

`cnc_nr` is the service number e.g. 'Wohnsitz ummelden (Alleinige, Haupt- oder Nebenwohnung)' results in cnc_nr 7329.

Please go to https://termin.bremen.de/termine/ and click the location and service you're searching an appointment in order to find `loc_nr` and`cnc_nr`.


