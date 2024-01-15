import sys

def find_location(query):
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

    query = query.strip()
    if query == '':
        return None
    for state, abbrev in states.items():
        if state.lower() == query.lower():
            capital = capital_cities[abbrev]
            return f"{capital} is the capital of {state}"
    for abbrev, capital in capital_cities.items():
        if capital.lower() == query.lower():
            for state, state_abbrev in states.items():
                if state_abbrev == abbrev:
                    return f"{capital} is the capital of {state}"
    return f"{query} is neither a capital city nor a state"

def main():
    if len(sys.argv) != 2:
        return
    input_str = sys.argv[1]
    if ',,' in input_str:
        return
    queries = input_str.split(',')
    for query in queries:
        result = find_location(query)
        if result:
            print(result)

if __name__ == "__main__":
    main()