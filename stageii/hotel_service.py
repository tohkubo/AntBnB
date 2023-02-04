class HotelService:
    def __init__(self, *args, **kwargs) -> None:
        self._rooms: set[int] = set()

    def add_room(self, room: int) -> None:
        self._rooms.add(room)
    
    def list_rooms(self) -> None:
        print(f'Number of bedrooms in service: {len(self._rooms)}')
        print('------------------------------------')
        for room in self._rooms:
            print(room)
    
    def delete_room(self, room: int) -> None:
        if room not in self._rooms:
            print(f'Sorry can\'t delete room {room}; it is not in service now')
            return
        self._rooms.remove(room)