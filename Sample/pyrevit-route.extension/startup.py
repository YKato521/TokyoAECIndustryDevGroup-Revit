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
	furniture_type_dict = {}
	for f in furnitures:
		if f.Symbol.FamilyName in furniture_dict.keys():
			furniture_dict[f.Symbol.FamilyName] += 1 
		else:
			furniture_dict[f.Symbol.FamilyName] = 1
		if f.Symbol.FamilyName + ' - ' + f.name in furniture_type_dict.keys():
			furniture_type_dict[f.Symbol.FamilyName + ' - ' + f.name] += 1
		else:
			furniture_type_dict[f.Symbol.FamilyName + ' - ' + f.name] = 1
		family_dict = {
			'family': furniture_dict,
			'family_type': furniture_type_dict
			}
	return routes.make_response(data=family_dict)