from Autodesk.Revit.DB import BuiltInParameter, FamilyInstance
from revitron import Selection, DOC, _
from rpw.ui.forms import SelectFromList
from pyrevit.forms import select_parameters


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
    # Part3
    def select_by_name(self):
        select_dict = {}
        selection = Selection()
        els = selection.get()
        for el in els:
            if isinstance(el, FamilyInstance):
                if el.Symbol.FamilyName not in select_dict.keys():
                    select_dict[el.Symbol.FamilyName] = [el.Id]
                else:
                    select_dict[el.Symbol.FamilyName].append(el.Id)
            elif DOC.GetElement(el.GetTypeId()):
                el_name = DOC.GetElement(el.GetTypeId()).FamilyName
                if el_name not in select_dict.keys():
                    select_dict[el_name] = [el.Id]
                else:
                    select_dict[el_name].append(el.Id)

        form = SelectFromList("Select By FamilyName", select_dict, exit_on_close=True)
        if form is not None:
            selection.set(form)
    
    def select_by_param(self):
        category_dict = {}
        select_dict = {}
        param_list = []
        selection = Selection()
        els = selection.get()
        for el in els:
            if isinstance(el, FamilyInstance):
                if el.Category.Name not in category_dict.keys():
                    category_dict[el.Category.Name] = [el]
                else:
                    category_dict[el.Category.Name].append(el)
        selected_cat_els = SelectFromList("Select By Category", category_dict, exit_on_close=True)
        for selected_el in selected_cat_els:
            for param in  selected_el.GetOrderedParameters():
                if param.Definition.Name not in param_list:
                    param_list.append(param.Definition.Name)
        param_name = SelectFromList("Select By Parameter", param_list, exit_on_close=True)
        """
        select_parameters(
            el,
            title='Select Parameters',
            multiple=True,
            include_instance=True,
            include_type=False)
        """
        for el in selected_cat_els:
            param = _(el).get(param_name)
            if param not in select_dict.keys():
                select_dict[param] = [el.Id]
            else:
                if select_dict[param]:
                    select_dict[param].append(el.Id)
                else:
                    select_dict[param] = [el.Id]
        form = SelectFromList("Select By {}".format(param_name), select_dict, exit_on_close=True)
        if form is not None:
            selection.set(form)

