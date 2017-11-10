"""
Picks groups of members to work on projects, trying to match the
members' preferences as much as possible.
"""
import random

# The different projects
SERVER='server'
HTML='html'
DB='database'
CSS='css'
JS='JavaScript'

# Each member and their preferred projects, in descending order.
member_prefs = {
  'lucyk': [SERVER, HTML, DB, CSS, JS],
  'eloise': [HTML, JS, SERVER, DB, CSS],
  'sophia': [HTML, JS, DB, CSS, SERVER],
  'sarah': [JS, CSS, HTML, SERVER, DB],
  'kriti': [HTML, CSS, JS, DB, SERVER],
  'lucyh': [HTML, CSS, JS, DB, SERVER],
  'ruari': [JS, HTML, SERVER, DB, CSS],
  'meghan': [DB, SERVER, HTML, CSS, JS],
  'jade': [HTML, CSS, SERVER, JS, DB]
}

MAX_GROUP_SIZE = 2

def pick_groups():
  groups = { SERVER: [], HTML: [], DB: [], CSS: [], JS: [] }
  members = list(member_prefs.keys())
  random.shuffle(members)
  for member in members:
    for pref in member_prefs[member]:
      if len(groups[pref]) < MAX_GROUP_SIZE:
        groups[pref].append(member)
        break
  print(groups)

pick_groups()
