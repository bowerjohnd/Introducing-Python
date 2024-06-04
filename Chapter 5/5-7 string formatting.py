setup = 'a duck goes into a bar...'
print(setup.strip('.'))

print(setup.capitalize())
print(setup.title())
print(setup)
print(setup.upper())
print(setup.lower())
print(setup.swapcase())

print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))

# old style

print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

print('%d%%' % 100)

actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" % actor)

print("Our cat %s weights %s pounds" % (cat, weight))

thing = 'woodchuck'
print('%s' % thing)
print('%12s' % thing)
print('%+12s' % thing)
print('%-12s' % thing)
print('%.3s' % thing)
print('%12.3s' % thing)
print('%-12.3s' % thing)

thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12f' % thing)
print('%.3f' % thing)
print('%12.3f' % thing)
print('%-12.3f' % thing)

thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)

# new style

thing = 'woodchuck'
print('{}'.format(thing))

place = 'lake'
print('The {} is in the {}.'.format(thing, place))
print('The {1} is in the {0}.'.format(place, thing))
print('The {thing} is in the {place}'.format(thing='duck', place='bathtub'))

d = {'thing':'duck', 'place':'bathtub'}
print('The {0[thing]} is in the {0[place]}.'.format(d))

thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing,place))
print('The {:10s} is at the {:10s}'.format(thing,place))
print('The {:<10s} is at the {:<10s}'.format(thing,place))
print('The {:^10s} is at the {:^10s}'.format(thing,place))
print('The {:>10s} is at the {:>10s}'.format(thing,place))
print('The {:!^10s} is at the {:!^10s}'.format(thing,place))

# newest style

thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')

print(f'The {thing.capitalize()} is in the {place.rjust(20)}')

print(f'The {thing:>20} is in the {place:.^20}')

print(f'{thing[-4:] =}, {place.title() =}')

print(f'{thing = :>4.4}')