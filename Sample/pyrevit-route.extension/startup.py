from pyrevit import routes
from pyrevit import DB
from rpw import db
from pyrevit import routes

api = routes.API('route-sample')


@api.route('/title')
def get_title(doc):
	return routes.make_response(data=doc.Title)

@api.route('/levels')
def get_levels(doc):
	level_list = []
	levels = db.Collector(
		of_category='Levels',
		is_not_type=True).get_elements()
	for level in levels:
		level_dict = {}
		level_dict['name'] = level.name
		level_dict['Elevation']= level.Elevation * 304.8
		level_list.append(level_dict)
	sorted_level_list = sorted(level_list, key=lambda x:x['Elevation'])
	return routes.make_response(data=sorted_level_list)

@api.route('/furniture')
def get_furnitures(doc):
	furnitures = db.Collector(
		of_category='Furniture',
		is_not_type=True).get_elements()
	furniture_dict = {}
	for w in furnitures:
		if w.Symbol.FamilyName in furniture_dict.keys():
			furniture_dict[w.Symbol.FamilyName] += 1 
		else:
			furniture_dict[w.Symbol.FamilyName] = 1
	return routes.make_response(data=furniture_dict)