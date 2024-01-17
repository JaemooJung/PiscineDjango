from elements import *
import traceback

class Page:
  _root_element = Elem()

  def __init__(self, root_element):
    if not isinstance(root_element, (Elem, Text)):
      raise Elem.ValidationError
    self._root_element = root_element

  def __str__(self):
    if isinstance(self._root_element, Html):
      return '<!DOCTYPE html>\n' + str(self._root_element)
    else:
      return str(self._root_element)
    
  def write_to_file(self, filename: str):
    with open(filename, 'w') as f:
      f.write(str(self))
    
  def is_valid(self) -> bool:
    return self.__is_elem_valid(self._root_element)
  
  def __is_elem_valid(self, elem: Elem) -> bool:
    elem_classes = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)
    if not (isinstance(elem, elem_classes) or isinstance(elem, Text)):
      return False
    
    # Html must strictly contain a Head, then a Body.
    if isinstance(elem, Html):
      if len(elem.content) != 2:
        return False
      if not isinstance(elem.content[0], Head):
        return False
      if not isinstance(elem.content[1], Body):
        return False
      
    # Head must only contain one Title and only one Title.
    if isinstance(elem, Head):
      if len(elem.content) != 1:
        return False
      if not isinstance(elem.content[0], Title):
        return False

    # Body and Div must only contain the following type of elements: H1, H2, Div, Table, Ul, Ol, Span, or Text.
    if (isinstance(elem, Body) or isinstance(elem, Div)):
      if not all([isinstance(e, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for e in elem.content]):
        return False
    
    # Title, H1, H2, Li, Th, Td must only contain one Text and only this Text.
    if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
      if len(elem.content) != 1:
        return False
      if not isinstance(elem.content[0], Text):
        return False
    
    # P must only contain Text.
    if isinstance(elem, P):
      if not all([isinstance(e, Text) for e in elem.content]):
        return False
    
    # Span must only contain Text or some P
    if isinstance(elem, Span):
      if not all([isinstance(e, (Text, P)) for e in elem.content]):
        return False
    
    # Ul and Ol must contain at least one Li and only some Li.
    if isinstance(elem, (Ul, Ol)):
      if len([e for e in elem.content if isinstance(e, Li)]) < 1:
        return False
      if not all([isinstance(e, Li) for e in elem.content]):
        return False
      
    # Table must only contain Tr and only some Tr.
    if isinstance(elem, Table):
      if not all([isinstance(e, Tr) for e in elem.content]):
        return False
    
    # Tr must contain at least one Th or Td and only some Th or Td. 
    # The Th and the Td must be mutually exclusive.
    if isinstance(elem, Tr):
      if len([e for e in elem.content if isinstance(e, (Th, Td))]) < 1:
        return False
      if not all([isinstance(e, (Th, Td)) for e in elem.content]):
        return False
      if any(isinstance(e, Th) for e in elem.content) and any(isinstance(e, Td) for e in elem.content):
        return False
    
    if isinstance(elem, Elem) and elem.content is not None and len(elem.content) > 0:
      return all([self.__is_elem_valid(e) for e in elem.content])
    
    return True
      