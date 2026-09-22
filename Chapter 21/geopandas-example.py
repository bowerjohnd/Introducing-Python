# 21-4 Map from geopandas and matplotlib

# book informs that geopandas relies on the following pip installs:
#       numpy, pandas, shapely, fiona, pyproj, and six
# book example geopandas.datasets deprecated, need to pip install and import geodatasets

import geopandas
from geodatasets import get_path
import matplotlib.pyplot as plt

#world_file = geopandas.datasets.get_path('naturalearth_lowres')    # deprecated

world_file = get_path('naturalearth.land')
world = geopandas.read_file(world_file)


#cities_file = geopandas.datasets.get_path('naturalearth_cities')   # deprecated

cities_file = get_path('naturalearth.cities')
cities = geopandas.read_file(cities_file)


base = world.plot(color='orchid')
cities.plot(ax=base, color='black', markersize=2)

plt.show()