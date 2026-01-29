import entities

# defining game data
def create_game_data():
    """Creates and returns the initial game data including rooms, items, and characters."""

    # Create rooms
    kitchen = entities.Room(
        "Kitchen",
        "The small kitchen was warmly lit, the aroma of freshly brewed tea wafting through the air. The quiet trickling sound of water fills the room, the mingling with the hum of the fridge. The countertops are cluttered with various utensils and the remnants of dinner are submerged in suds. There is an entrance to the east, leading to the lounge.",
    )
    lounge = entities.Room(
        "Lounge",
        "The lounge is a cozy and inviting place furnished with a couch, bean bags, a lamp casting dancing shadows, various bookshelfs lining the walls, and a console beneath the TV. There are wooden doors on all sides, one to the north for the storage room, the main entrance to the garden is to the east, the entrance leading back to the kitchen is to the west, and two on the south leading to the 2 bedrooms.",
    )
    master_bedroom = entities.Room(
        "Master Bedroom",
        "The master bedroom is a peaceful sanctuary with a large bed flanked by nightstands on both sides, the closet stands on the opposite wall while the dresser lines the remaining wall. The room is dark, the lamp by the bed cool to the touch. There is a door to the north leading back to the lounge.",
    )
    kids_bedroom = entities.Room(
        "Kids Bedroom",
        "The bedroom is a safe haven boasting a bunk bed and a single on either walls. The walls are lined with posters save for the wall beside the door, hosting the closet. The desk, acting as a divider between the beds, is tidy, schoolbags place in either sides. There is moonlight filtering through the window located above the desk, onlooking the garden. The rustling leaves provide the only sound. There is a door to the north leading back to the lounge.",
    )
    storage_room = entities.Room(
        "Storage Room",
        "The storage room is a cramped and dimly lit walkway filled with shelves stocked with various household items, boxes piled haphazardly in corners, and random tools tucked away. The air is thick with dust, and a small flickering light bulb hangs from the ceiling, casting long shadows on the walls, adding to the eerie atmosphere. There is a door to the south leading back to the lounge and a mesh panel door leading to the garden. The mesh panel door tucked beside one of the shelves is swaying with the wind is to the north.",
    )
    garden = entities.Room(
        "Garden",
        "The garden is spacious with a well-maintained lawn and potted plants lining the boundary walls. A few garden chairs and a table are arranged under the awning. There is the main entrance to the west leading back inside whereas the main gate is on the east boundary.",
    )

    # Adding neighbors
    kitchen.add_neighbor("East", lounge)
    master_bedroom.add_neighbor("North", lounge)
    kids_bedroom.add_neighbor("North", lounge)
    storage_room.add_neighbor("South", lounge)
    garden.add_neighbor("West", lounge)
    lounge.add_neighbor("West", kitchen)
    lounge.add_neighbor("South West", master_bedroom)
    lounge.add_neighbor("South East", kids_bedroom)
    lounge.add_neighbor("North", storage_room)
    lounge.add_neighbor("East", garden)