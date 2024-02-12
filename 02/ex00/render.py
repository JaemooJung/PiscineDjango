#!/usr/bin/python3
import os
import sys
import re
import settings

def main():
    if (len(sys.argv) != 2):
        return print("wrong argument count")
    path = sys.argv[1]
    regex = re.compile(".*\.template")
    if not regex.match(path):
        return print("wrong extension, (required: .template)")
    if not os.path.isfile(path):
        return print(f"does not exit file... : {path}")
    with open(path, "r") as f:
        template = "".join(f.readlines())
    try:
      file = template.format(
          title=settings.title,
          first_name=settings.first_name,
          last_name=settings.last_name,
          age=settings.age, 
          profession=settings.profession,
          mobile=settings.mobile,
          email=settings.email
      )
    except Exception as e:
      return print(f"Error: {e}")
    regex = re.compile("(\.template)")
    path = "".join([path[0:regex.search(path).start()], ".html"])
    with open(path, "w") as f:
        f.write(file)

if __name__ == '__main__':
    main()
