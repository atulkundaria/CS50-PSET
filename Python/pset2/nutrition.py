fruits = {
	"apple": "130",
	"avocado": "50",
	"banana": "110",
	"cantaloupe": "50",
	"grapefruit": "60",
	"grapes": "90",
	"honeydew melon": "50",
	"kiwifruit": "90",
	"lemon": "90",
	"lime": "20",
	"nectraine": "60",
	"orange": "80",
	"peach": "60",
	"pear": "100",
	"pineapple": "50",
	"plums": "70",
	"straberries": "50",
	"sweet cherries": "100",
	"tengerine": "50",
	"watermelon": "80",
}

fruit = input("Item: ").strip()
fruit = fruit.lower()

if fruit in fruits:
	print(f"Calories: {fruits[fruit]}")