import sys

def find_capital(state_name):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    state_code = states.get(state_name)
    if state_code:
        return capital_cities[state_code]
    else:
        return "Unknown state"

def main():
    args = sys.argv[1:]

    if len(args) == 1:
        print(find_capital(args[0]))

if __name__ == "__main__":
    main()