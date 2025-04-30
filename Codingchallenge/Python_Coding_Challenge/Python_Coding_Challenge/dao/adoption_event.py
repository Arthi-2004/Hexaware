from dao.iadoptable import IAdoptable

class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def register_participant(self, participant: IAdoptable):
        self.participants.append(participant)

    def host_event(self):
        print("Adoption Event is now live!")
        for participant in self.participants:
            try:
                participant.adopt()
            except Exception as e:
                print(f"Error during adoption: {str(e)}")
