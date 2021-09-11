#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "216ACD94-C70D-42CE-80F1-FA90A0D7F747",
  "name": "Fictional",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1630601285901,
  "passages": [
    {
      "name": "West of House",
      "tags": "",
      "id": "1",
      "text": "This is an open field west of a grey house, with a boarded front door.\n\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[WEST->Forest]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is an open field west of a grey house, with a boarded front door. You may go North, South or West."
    },
    {
      "name": "North of House",
      "tags": "",
      "id": "2",
      "text": "You are facing the north side of a grey house. There is no door here, and all the windows are barred.\n\n[[WEST->West of House]]\n[[EAST->East of House]]\n[[NORTH->Forest]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
          "original": "[[WEST->West of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Forest",
          "original": "[[NORTH->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the north side of a grey house. There is no door here, and all the windows are barred. You may go North, East or West."
    },
    {
      "name": "South of House",
      "tags": "",
      "id": "3",
      "text": "You are facing the south side of a grey house. There is no door here, and all the windows are barred.\n\n[[WEST->West of House]]\n[[EAST->East of House]]\n[[SOUTH->Forest]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
          "original": "[[WEST->West of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the south side of a grey house. There is no door here, and all the windows are barred. You may go East, South or West."
    },
    {
      "name": "Forest",
      "tags": "",
      "id": "4",
      "text": "This is a forest, with trees in all directions around you.\n\n[[NORTH->Sunlit Forest]]\n[[EAST->Forest]]\n[[SOUTH->Forest]]\n[[WEST->Forest]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Sunlit Forest",
          "original": "[[NORTH->Sunlit Forest]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Forest",
          "original": "[[EAST->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a forest, with trees in all directions around you. You may go North, East, South or West."
    },
    {
      "name": "East of House",
      "tags": "",
      "id": "5",
      "text": "You are behind the grey house. A path leads into the forest to the east. In one corner of the house there is a dirty window which is slightly ajar.\n\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[EAST->Sunlit Forest]]\n[[WEST->Kitchen]]\n[[ENTER->Kitchen]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Sunlit Forest",
          "original": "[[EAST->Sunlit Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Kitchen",
          "original": "[[WEST->Kitchen]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "Kitchen",
          "original": "[[ENTER->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are behind the grey house. An overgrown path leads into the forest to the east. In one corner of the house there is a dirty window which is slightly ajar. You may go North, East, South, West or Enter."
    },
    {
      "name": "Sunlit Forest",
      "tags": "",
      "id": "6",
      "text": "This is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here.\n\n[[NORTH->Forest]]\n[[SOUTH->Forest]]\n[[EAST->Forest]]\n[[WEST->East of House]]\n[[UP->Tree]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Forest",
          "original": "[[NORTH->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Forest",
          "original": "[[EAST->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "East of House",
          "original": "[[WEST->East of House]]"
        },
        {
          "linkText": "UP",
          "passageName": "Tree",
          "original": "[[UP->Tree]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here. You may go North, East, South, West or Up."
    },
    {
      "name": "Kitchen",
      "tags": "",
      "id": "7",
	  "score":20,
      "text": "You are in the dirty kitchen of the grey house. A moldy table seems to have been not used for some time. A dimly lit hallway leads to the west and a dark staircase can be seen leading upward. To the east is a small window which is open.\n\n[[EAST->East of House]]\n[[UPSTAIRS->Upstairs]]\n[[HALLWAY->Living Room]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        },
        {
          "linkText": "UPSTAIRS",
          "passageName": "Upstairs",
          "original": "[[UPSTAIRS->Upstairs]]"
        },
        {
          "linkText": "HALLWAY",
          "passageName": "Living Room",
          "original": "[[HALLWAY->Living Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are in the dirty kitchen of the grey house. A moldy table seems to have been not used for some time. A dimly lit hallway leads to the west and a dark staircase can be seen leading upward. To the east is a small window which is open. You may go East, Upstairs or through the Hallway."
    },
    {
      "name": "Tree",
      "tags": "",
      "id": "8",
	  "score":10,
      "text": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest.\n\n[[DOWN->Sunlit Forest]]",
      "links": [
        {
          "linkText": "DOWN",
          "passageName": "Sunlit Forest",
          "original": "[[DOWN->Sunlit Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest. You may go Down."
    },
    {
      "name": "Upstairs",
      "tags": "",
      "id": "9",
	  "score":-10,
      "text": "You are upstairs in the grey house. It is very dark and you think you can hear floor boards creaking as if something was creeping around.\n\n[[DOWN->Kitchen]]",
      "links": [
        {
          "linkText": "DOWNSTAIRS",
          "passageName": "Kitchen",
          "original": "[[DOWNSTAIRS->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are upstairs in the grey house. It is very dark and you think you can hear floor boards creaking as if something was creeping around. You may go Downstairs"
    },
    {
     "name": "Living Room",
      "tags": "",
      "id": "10",
      "text": "You are in the living room of the grey house. It is dim as the windows are boarded up. You can see that spiders have taken over. Even the busted tv the blocked entry way are covered in webs. there is a busted doorway to stairs that go down into darkness. You may go East or Doorway.\n\n[[EAST->Kitchen]]\n[[DOORWAY->Doorway]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "Kitchen",
          "original": "[[EAST->Kitchen]]"
        },
        {
           "linkText": "DOORWAY",
          "passageName": "Doorway",
          "original": "[[DOORWAY->Doorway]]" 
        }
      ],
      "hooks": [],
      "cleanText": "You are in the living room of the grey house. It is dim as the windows are boarded up. You can see that spiders have taken over. Even the busted tv the blocked entry way are covered in webs. there is a busted doorway to stairs that go down into darkness. You may go East or Doorway."
    },
    {
      "name": "Doorway",
      "tags": "",
      "id": "11",
	  "score":-1,
      "text": "You are at the busted door with a set of scratched up stairs leading into the darkness of the basement. You can hear something big and scary living down there. You are advised to go Back but may go Downstairs. \n\n[[DOWNSTAIRS->Basement]]\n[[BACK->Living Room]]",
      "links": [
        {
          "linkText": "DOWNSTAIRS",
          "passageName": "Basement",
          "original": "[[DOWNSTAIRS->Basement]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Living Room",
          "original": "[[BACK->Living Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at the busted door with a set of scratched up stairs leading into the darkness of the basement. You can hear something big and scary living down there. You are advised to go Back but may go Downstairs"
    },
    {
      "name": "Basement",
      "tags": "",
      "id": "12",
	  "score":-20,
      "text": "You did not take heed and have been eaten. You only have the option to Quit",
      "links": [],
      "hooks": [],
      "cleanText": "You did not take heed and have been eaten. You only have the option to Quit"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		#print("Moves: " + str(moves) + ", Score: " + str(score))
		print("Moves: {}, Score: {}".format(moves, score))
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "West of House"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves = moves + 1 
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")