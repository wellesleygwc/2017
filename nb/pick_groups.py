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
  'rachela': [DB, SERVER, HTML, CSS, JS],  # Just guessed on secondary preferences
  'rachelw': [CSS, HTML, JS, SERVER, DB],   # Just guessed on prefs 3:5
  'lucyk': [SERVER, HTML, DB, CSS, JS],
  'sophia': [HTML, JS, DB, CSS, SERVER],
  'ruari': [JS, HTML, SERVER, DB, CSS],
  'sarah': [JS, CSS, HTML, SERVER, DB],
  'eloise': [HTML, JS, SERVER, DB, CSS],
  'kriti': [HTML, CSS, JS, DB, SERVER],
  'jademei': [HTML, CSS, SERVER, JS, DB],
  'meghan': [DB, SERVER, HTML, CSS, JS],
  'lucyh': [HTML, CSS, JS, DB, SERVER],
}

MAX_GROUP_SIZE = 2

def pick_groups():
  groups = { SERVER: [], HTML: [], DB: [], CSS: [], JS: [] }
  members = list(member_prefs.keys())
  # random.shuffle(members)
  for member in members:
    for pref in member_prefs[member]:
      if len(groups[pref]) < MAX_GROUP_SIZE:
        groups[pref].append(member)
        break
  for group in groups.keys():
    print("%s: %s" % (group, groups[group]))

pick_groups()
