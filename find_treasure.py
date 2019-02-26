def can_get_treasure(starting_room, locked_doors={}, keys={}, visited=set()):
        
    visited.add(starting_room)
    queue = collections.deque([starting_room])
    while queue:
        room = queue.popleft()
        if room.treasure: return True
        if room.key: keys[id(room.key)] = room.key
        for door in room.doors:
            if door.unlocked:
                other_room = door.get_other_room(room)
                if other_room not in visited:
                    visited.add(other_room)
                    queue.append(other_room)
            elif id(door) not in locked_doors:
                locked_doors[id(door)] = door
        
    for door_id in locked_doors:
        for key_id in keys:
            if locked_doors[door_id].can_open(keys[key_id]):
                locked_doors[door_id].unlocked = True
                room = locked_doors[door_id].get_other_room()
                del locked_doors[door_id]
                del keys[key_id]
                return can_get_treasure(room, locked_doors, keys, visited)
    return False