def parse_element(line):
    name, properties = line.split(' = ')
    properties = properties.split(', ')
    properties_dict = {prop.split(':')[0]: prop.split(':')[1] for prop in properties}
    return name, properties_dict

def generate_html(elements):
    # 2D array to store elements
    element_grid = [['' for _ in range(18)] for _ in range(7)]
    
    # Fill the grid with elements
    for element, properties in elements.items():
        col = int(properties['position'])
        row = len(properties['electron'].split(' ')) - 1
        element_grid[row][col] = {'element': element, 'properties': properties}
    
    html = []
    
    html.append('''<!DOCTYPE html>
        <html lang=\'en\'>   
        <head>
        <meta charset="utf-8">
        <title>preiodic table</title>
        </head>
        <body>
        <table>''')
    
    # Generate HTML from the grid
    for row in element_grid:
        html.append('<tr>')
        for cell in row:
            html.append('<td style="border: 1px solid black; padding:10px">')
            if cell:
                html.append(f'<h4>{cell["element"]}</h4>')
                html.append('<ul>')
                html.append(f"<li>Number: {cell['properties']['number']}</li>")
                html.append(f"<li>Small: {cell['properties']['small']}</li>")
                html.append(f"<li>Molar: {cell['properties']['molar']}</li>")
                html.append(f"<li>Electron: {cell['properties']['electron']}</li>")
                html.append('</ul>')
            html.append('</td>')
        html.append('</tr>')
    html.append('</table></body></html>')
    return ''.join(html)

def main():
    with open('./periodic_table.txt', 'r') as file:
        lines = file.readlines()
        elements = {}
        for line in lines:
            name, properties = parse_element(line)
            elements[name] = properties

    html = generate_html(elements)

    with open('periodic_table.html', 'w') as file:
        file.write(html)

if __name__ == '__main__':
    main()
