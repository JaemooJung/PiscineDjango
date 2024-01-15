def parse_element(line):
    name, properties = line.split(' = ')
    properties = properties.split(', ')
    properties_dict = {prop.split(':')[0]: prop.split(':')[1] for prop in properties}
    return name, properties_dict

def generate_html(elements):
    html = '<html><body><table>'
    
    # Assume the periodic table has 7 rows and 18 columns
    for i in range(7):  # Rows of the periodic table
        html += '<tr>'
        for j in range(18):  # Columns of the periodic table
            element_exists = False
            for element, properties in elements.items():
                # Calculate position in the 2D table
                col = int(properties['position'])
                row = len(properties['electron'].split(' ')) - 1
                
                # Check if the element belongs to the current cell
                if row == i and col == j:
                    element_exists = True
                    html += '<td style="border: 1px solid black; padding:10px">'
                    html += f'<h4>{element}</h4>'
                    html += '<ul>'
                    html += f"<li>Number: {properties['number']}</li>"
                    html += f"<li>Small: {properties['small']}</li>"
                    html += f"<li>Molar: {properties['molar']}</li>"
                    html += f"<li>Electron: {properties['electron']}</li>"
                    html += '</ul></td>'
                    break
            if not element_exists:
                html += '<td style="border: 1px solid black; padding:10px"></td>'
        html += '</tr>'
    html += '</table></body></html>'
    return html

def main():
    with open('./periodic_table.txt', 'r') as file:
        lines = file.readlines()
        elements = {parse_element(line)[0]: parse_element(line)[1] for line in lines}

    html = generate_html(elements)

    with open('periodic_table.html', 'w') as file:
        file.write(html)

if __name__ == '__main__':
    main()
