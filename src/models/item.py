class Item :
    def __init__(self , item_id , description , category , date_found , location_found , status):
        self.item_id = item_id
        self.description = description
        self.category = category
        self.date_found = date_found
        self.location_found = location_found
        self.status = status

    def __str__(self):
        return(
            f'item id : {self.item_id}\n'
            f'item description : {self.description}\n'
            f'category of the item : {self.category}\n'
            f'item was found on : {self.date_found}\n'
            f'item was found in : {self.location_found}\n'
            f'status of the item : {self.status}'
        )
        