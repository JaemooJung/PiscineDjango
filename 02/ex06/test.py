import traceback
from page import *

def __test_page():
  # Tr tests
  valid_tr_1 = Tr([Th(Text('foo')), Th(Text('bar'))])
  valid_tr_2 = Tr([Td(Text('foo')), Td(Text('bar'))])
  invalid_tr_1 = Tr([Th(Text('foo')), Td(Text('bar'))])
  invalid_tr_2 = Tr()

  assert Page(valid_tr_1).is_valid() == True
  assert Page(valid_tr_2).is_valid() == True
  assert Page(invalid_tr_1).is_valid() == False
  assert Page(invalid_tr_2).is_valid() == False

  # Table tests
  valid_table_1 = Table([valid_tr_1, valid_tr_2])
  valid_table_2 = Table([valid_tr_1])
  invalid_table_1 = Table([Text('foo')])

  assert Page(valid_table_1).is_valid() == True
  assert Page(valid_table_2).is_valid() == True
  assert Page(invalid_table_1).is_valid() == False

  # Ul tests
  valid_ul_1 = Ul([Li(Text('foo')), Li(Text('bar'))])
  invalid_ul_1 = Ul([Text('foo')])

  assert Page(valid_ul_1).is_valid() == True
  assert Page(invalid_ul_1).is_valid() == False

  # Ol tests
  valid_ol_1 = Ol([Li(Text('foo')), Li(Text('bar'))])
  invalid_ol_1 = Ol([Text('foo')])

  assert Page(valid_ol_1).is_valid() == True
  assert Page(invalid_ol_1).is_valid() == False

  # Li tests
  valid_li_1 = Li(Text('foo'))
  invalid_li_1 = Li()

  assert Page(valid_li_1).is_valid() == True
  assert Page(invalid_li_1).is_valid() == False

  # H1 tests
  valid_h1_1 = H1(Text('foo'))
  invalid_h1_1 = H1()

  assert Page(valid_h1_1).is_valid() == True
  assert Page(invalid_h1_1).is_valid() == False

  # H2 tests
  valid_h2_1 = H2(Text('foo'))
  invalid_h2_1 = H2()

  assert Page(valid_h2_1).is_valid() == True
  assert Page(invalid_h2_1).is_valid() == False

  # P tests
  valid_p_1 = P(Text('foo'))
  invalid_p_1 = P(Li(Text('foo')))

  assert Page(valid_p_1).is_valid() == True
  assert Page(invalid_p_1).is_valid() == False

  # Span tests
  valid_span_1 = Span([Text('foo'), P(Text('bar'))])
  invalid_span_1 = Span([Li(Text('foo')), P()])

  assert Page(valid_span_1).is_valid() == True
  assert Page(invalid_span_1).is_valid() == False

  # Div tests
  valid_div_1 = Div([Text('foo'), valid_span_1])
  invalid_div_1 = Div([Li(Text('foo')), P()])

  assert Page(valid_div_1).is_valid() == True
  assert Page(invalid_div_1).is_valid() == False

  # Body tests
  valid_body_1 = Body([valid_h1_1, valid_div_1])
  invalid_body_1 = Body([valid_h1_1, invalid_div_1])

  assert Page(valid_body_1).is_valid() == True
  assert Page(invalid_body_1).is_valid() == False

  # Head tests
  valid_head_1 = Head(Title(Text('foo')))
  invalid_head_1 = Head(Title())

  assert Page(valid_head_1).is_valid() == True
  assert Page(invalid_head_1).is_valid() == False

  # Html tests
  valid_html_1 = Html([valid_head_1, valid_body_1])
  invalid_html_1 = Html([valid_head_1, invalid_body_1])

  assert Page(valid_html_1).is_valid() == True
  assert Page(invalid_html_1).is_valid() == False


if __name__ == '__main__':
  try:
    print("-------- Validity test start ------------------")
    __test_page()
    print('Page Validity tests : OK.')
    print("-------- Validity test end --------------------")

    print("-------- Render test start ------------------")
    head = Head(Title(Text('Hello ground!')))
    ul = Ul([Li(Text('foo')), Li(Text('bar'))])
    div = Div([Text('foo'), ul])
    h1 = H1(Text('Oh no, not again!'))
    img = Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
    body = Body([h1, img, div])
    html = Html([head, body])
    page = Page(html)
    print(page)
    print("-------- Render test end --------------------")

    print("-------- Write to file test start ------------------")
    page.write_to_file('test.html')
    print("-------- Write to file test end --------------------")

  except Exception as e:
    traceback.print_exc()
    print('Page tests : KO.')
    print(e)