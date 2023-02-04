from hotel_service import HotelService

INPUT_COMMAND_FILE = 'commands.txt'

hotel = HotelService()

with open(INPUT_COMMAND_FILE, 'r') as fp:
    for line in fp:
        line = line.strip()
        key = line[:2].upper()
        if key == 'PL':
            line = line.split('PL ')[1]
            print(line)
        elif key == '**':
            pass # ignore, just a comment
        elif key == 'NB':
            room = int(line.split()[1])
            hotel.add_room(room)
        elif key == 'LB': 
            hotel.list_rooms()
        elif key == 'DB':
            room = int(line.split()[1])
            hotel.delete_room(room)
