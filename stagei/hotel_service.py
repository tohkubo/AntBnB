from models import Room


class Hotel:
    def __init__(self, *args, **kwargs) -> None:
        self._rooms: list[Room] = []

    def add_room(self, room: int) -> None:
        self._rooms.append(Room(room))
    
    def list_rooms(self) -> None:
        print(f'Number of bedrooms in service:  {len(self._rooms)}')
        print('------------------------------------')
        for room in self._rooms:
            print(room.number)
