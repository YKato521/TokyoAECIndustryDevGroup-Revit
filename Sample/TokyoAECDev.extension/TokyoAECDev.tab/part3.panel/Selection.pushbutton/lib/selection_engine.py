from Autodesk.Revit.DB import BuiltInParameter
from revitron import Selection, _
from rpw.ui.forms import SelectFromList


class selectionEngine(object):
    # Part1
    """
    def select_by_name(self):
        table_list = []
        selection = Selection()
        els = selection.get()
        for el in els:
            if 'table' in el.Symbol.FamilyName.lower():
                table_list.append(el.Id)
        selection.set(table_list)
    
    def select_by_param(self):
        param_list = []
        selection = Selection()
        els = selection.get()
        for el in els:
            param = _(el).get('Comments')
            try:
                par = el.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).AsString()
            except:
                par = None
            # print(param, par)
            if 'change' in param.lower():
                param_list.append(el.Id)
        selection.set(param_list)
    """

    # Part2
    def select_by_name(self):
        select_dict = {}
        select_list = []
        selection = Selection()
        els = selection.get()
        for el in els:
            if el.Symbol.FamilyName not in select_dict.keys():
                select_dict[el.Symbol.FamilyName] = el
        form = SelectFromList("Select By FamilyName", select_dict, exit_on_close=True)
        for el in els:
            if el.Symbol.Id == form.Symbol.Id:
                select_list.append(el.Id)      
        selection.set(select_list)
    
    def select_by_param(self):
        param_list = []
        selection = Selection()
        els = selection.get()
        for el in els:
            param = _(el).get('Comments')
            try:
                par = el.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).AsString()
            except:
                par = None
            # print(param, par)
        for el in els:
            if el.Symbol.FamilyName not in select_dict.keys():
                select_dict[el.Symbol.FamilyName] = el
        form = SelectFromList("Select By FamilyName", select_dict, exit_on_close=True)
            if 'change' in param.lower():
                param_list.append(el.Id)
        selection.set(param_list)
