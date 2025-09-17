# In Python, annptatins are used by coding tools to help write rigorous well formed code
# e.g. code completion, code hint/lints all use annotations
# annotations can work with any 'language engine' to help with code sanity

# NB annotation do NOT actually enforce the return type
def writeText(t) -> str:
    return (t, f'we received a value {t} which is of type {type(t)}')

print(writeText('hello'), type(writeText('Hello')))

# the set object
s = {1, 4,5,6,'a', 7,'a', 5, True}
s.add(9)
s.remove(7)
print(s, type(s))
