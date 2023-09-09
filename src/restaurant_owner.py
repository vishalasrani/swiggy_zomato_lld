from ipartner import IPartner


class RestaurantOwner(IPartner):

    def __init__(self, name):
        super().__init__(name)

    def get_owner_name(self):
        return self._name
