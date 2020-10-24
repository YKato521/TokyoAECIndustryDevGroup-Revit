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
    """
    def select_by_name(self):
        select_dict = {}
        selection = Selection()
        els = selection.get()
        for el in els:
            if el.Symbol.FamilyName not in select_dict.keys():
                select_dict[el.Symbol.FamilyName] = [el.Id]
            else:
                select_dict[el.Symbol.FamilyName].append(el.Id)
        form = SelectFromList("Select By FamilyName", select_dict, exit_on_close=True)
        if form is not None:
            selection.set(form)
    
    def select_by_param(self):
        select_dict = {}
        param_list = []
        selection = Selection()
        els = selection.get()
        for el in els:
            param = _(el).get('Comments')
            
            #try:
            #    param = el.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).AsString()
            #except:
            #    param = None
            
            if param not in select_dict.keys():
                select_dict[param] = [el.Id]
            else:
                if select_dict[param]:
                    select_dict[param].append(el.Id)
                else:
                    select_dict[param] = [el.Id]
        form = SelectFromList("Select By Comments", select_dict, exit_on_close=True)
        if form is not None:
            selection.set(form)
    """