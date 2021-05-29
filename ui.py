class Window:

    def __init__(self):
        pass

    def get_user_choice(self, items, heading="-----"):
        print(f"\n{heading}")
        choice = None
        while not choice:
            print()
            for id in range(len(items)):
                print(f"  {id+1}. {items[id+1]['name']}")
            choice = input("\nChoose your option: ")
            try:
                choice = int(choice)
                if choice < 1 or choice > len(items):
                    raise ValueError
            except ValueError:
                print("Enter the number from the list below.")
                choice = None
        return choice

    def get_choices_list(self, items, heading="-----"):
        print(f"\n{heading}")
        choices = None
        while not choices:
            for id in range(len(items)):
                print(f"  {id+1}. {items[id+1]['name']}")
            choices = input("\nChoose your options (divided by coma): ").split(",")
            try:
                choices = [int(id) for id in choices]
            except ValueError:
                print("Choose from numbers listed below.")
                choices = None
        return choices
    
    def get_menu_items(self, items):
        id = 0
        menuitems = {}
        for item in items:
            id += 1
            menuitems[id] = {"name": item.name}
        return menuitems
