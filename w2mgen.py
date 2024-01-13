import requests

class w2mgen:
    def __init__(self, newEventName = "New Event Name", dateTypes = "DaysOfTheWeek", possibleDates = "0|1|2|3|4|5|6", noEarlierThan = 9, noLaterThan = 5, timeZone = "America/Toronto", dayToSend = "Sun", timeToSend = 9, period = "Weekly"):
        self.newEventName = newEventName
        self.dateTypes = dateTypes
        self.possibleDates = possibleDates
        self.noEarlierThan = noEarlierThan
        self.noLaterThan = noLaterThan
        self.timeZone = timeZone
        self.dayToSend = dayToSend
        self.timeToSend = timeToSend
        self.period = period
        self.link = ""
    
    def generateLink(self):
        payload = {"New Event Name": self.newEventName, "DataTypes": self.dateTypes, "PossibleDates": self.possibleDates, "NoEarlierThan":self.noEarlierThan, "NoLaterThan":self.noLaterThan, "TimeZone":self.timeZone}
        x = requests.post('https://www.when2meet.com/SaveNewEvent.php', data = payload)
        param = x.text[x.text.find("window.location=\'")+17: x.text.find("\'", x.text.find("window.location=\'")+17)]
        self.link = f"www.when2meet.com{param}"
        return (self.link)