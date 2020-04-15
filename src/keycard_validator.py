from keycard_generator import BlueKeyGrid, RedKeyGrid, Tile, TileType, load_keygrid
import functools

def add_type_to_dict(type_dict, grid_type):
  type_dict[grid_type] += 1
  return type_dict

types = ['b' if type(load_keygrid(idx)) is BlueKeyGrid else 'r' for idx in range(40)]
result = functools.reduce(add_type_to_dict, types, {'b': 0, 'r': 0})
print(result)