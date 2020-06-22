# -*- coding: utf-8 -*-
from Autodesk.Revit import DB, UI
from rpw import db, ui

"""
######################
## Code Sample (C#) ##
######################

UIApplication uiapp = commandData.Application;
UIDocument uidoc = uiapp.ActiveUIDocument;
Application app = uiapp.Application;
Document doc = uidoc.Document;

python
commandData.Application => __revit__

"""

# C#
"""
uiapp = __revit__
uidoc = uiapp.ActiveUIDocument
app = uiapp.Application
doc = uidoc.Document
element_ids = uidoc.Selection.GetElementIds()

sheet_list = []

for el_id in element_ids:
    el = doc.GetElement(el_id)
    if isinstance(el, DB.ViewSheet):
        sheet_list.append(el)
    else:
        message = '{}を除外します'.format(el.Name)
        ui.forms.Alert(content=message, title="シート以外が選択されました", exit=False)
if not sheet_list:
    ui.forms.Alert(content='シートを選択してください', title="選択エラー", exit=True)
else:
    print(sheet_list)
"""
# RPW WrappedElement

elements = ui.Selection()

sheet_list = []

for el in elements:
    if isinstance(el, db.ViewSheet):
        sheet_list.append(el)
    else:
        message = '{}を除外します'.format(el.Name)
        ui.forms.Alert(content=message, title="シート以外が選択されました", exit=False)
if not sheet_list:
    ui.forms.Alert(content='シートを選択してください', title="選択エラー", exit=True)
else:
    print(sheet_list)

# RPW UnwrappedElement
"""
elements = ui.Selection()

sheet_list = []

for rpw_el in elements:
    el = rpw_el.unwrap()
    if isinstance(el, DB.ViewSheet):
        sheet_list.append(el)
    else:
        message = '{}を除外します'.format(el.Name)
        ui.forms.Alert(content=message, title="シート以外が選択されました", exit=False)
if not sheet_list:
    ui.forms.Alert(content='シートを選択してください', title="選択エラー", exit=True)
else:
    print(sheet_list)
"""