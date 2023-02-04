from typing import Optional

from helpers import _parse_date, format_date
from models import Reservation


class HotelService:
    def __init__(self, *args, **kwargs) -> None:
        self._rooms: set[int] = set()
        self._reservations: list[Reservation] = []

    def add_room(self, room: int) -> None:
        self._rooms.add(room)
    
    def list_rooms(self) -> None:
        print(f'Number of bedrooms in service:\t{len(self._rooms)}')
        print('------------------------------------')
        for room in self._rooms:
            print(room)
    
    def delete_room(self, room: int) -> None:
        if room not in self._rooms:
            print(f'Sorry can\'t delete room {room}; it is not in service now')
            return
        self._rooms.remove(room)

    def reserve_room(self, roomnum: str, start: str, end: str, first: str, last: str) -> None:
        if int(roomnum) not in self._rooms:
            print(f'Sorry; can\'t reserve room {roomnum}; room not in service')
            return
        res = Reservation(
            room=int(roomnum),
            start=_parse_date(start),
            end=_parse_date(end),
            first_name=first,
            last_name=last,
        )
        self._reservations.append(res)
        print(f'Reserving room {roomnum} for {res.name} -- Confirmation #{res.reservation_id}')
        print(f'    (arriving {start}, departing {end})')
    
    def list_reservations(self) -> None:
        print(f'Number of reservations:\t{len(self._reservations)}')
        print('No. Rm. Arrive     Depart     Guest')
        print('------------------------------------------------')
        for res in self._reservations:
            print(f'{res.reservation_id:>3} {res.room} {format_date(res.start)} {format_date(res.end)} {res.name}')

    def delete_reservation(self, res_id: int) -> None:
        res = self._find_reservation_by_id(res_id)
        if not res:
            print(f'Sorry, can\'t cancel reservation; no confirmation number {res_id}')
            return
        self._reservations.remove(res)

    def _find_reservation_by_id(self, res_id: int) -> Optional[Reservation]:
        for res in self._reservations:
            if res.reservation_id == res_id:
                return res
        return None
