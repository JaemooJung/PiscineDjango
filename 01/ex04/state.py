import sys  # sys 모듈은 스크립트에서 기본적으로 사용 가능합니다.

def find_state(capital_city):
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

    for state, abbrev in states.items():
        if capital_cities.get(abbrev) == capital_city:
            return state
    return "Unknown capital city"

def main():
    args = sys.argv[1:]

    if len(args) == 1:
        print(find_state(args[0]))

if __name__ == "__main__":
    main()