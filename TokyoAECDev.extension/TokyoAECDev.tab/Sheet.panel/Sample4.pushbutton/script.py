# -*- coding: utf-8 -*-
from Autodesk.Revit import DB, UI
from rpw import db, ui
from System.Collections.Generic import List

# RPW WrappedElement

from rpw import doc

sheet_order_dict = {}

rpw_sheets = (
    db.Collector(
        of_class=DB.ViewSheet,
        is_not_type=True)
    .get_elements())
for sheet in rpw_sheets:
    sheet_category = sheet.SheetNumber[:2]
    sheet_order = sheet.SheetNumber[-2:]
    if str(sheet_category) in sheet_order_dict.keys() and sheet_order >= sheet_order_dict[str(sheet_category)]:
        sheet_order_dict[str(sheet_category)] = sheet_order
    elif str(sheet_category) not in sheet_order_dict.keys():
        sheet_order_dict[str(sheet_category)] = sheet_order

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

for sheet in sheet_list:

    source_param_dict = {}

    sheet_num = sheet.SheetNumber
    sheet_category = sheet_num[:2]

    with db.Transaction('Create Sheet'):
        new_sheet = DB.ViewSheet.Create(
            doc,
            DB.ElementId.InvalidElementId
        )
        new_sheet.Name = 'Test'
        new_sheet_order = int(sheet_order_dict[str(sheet_category)]) + 1
        if new_sheet_order < 10:
            new_sheet_number = str(sheet_category) + '0' + str(new_sheet_order)
        else:
            new_sheet_number = str(sheet_category) + str(new_sheet_order)
        new_sheet.SheetNumber = new_sheet_number
        sheet_order_dict[str(sheet_category)] = new_sheet_number
        for param in sheet.GetOrderedParameters():
            if not param.IsReadOnly:
                if param.StorageType == DB.StorageType.String:
                    try:
                        source_param_dict[param.Id] = param.AsString().encode('utf-8')
                    except Exception:
                        pass
                elif param.StorageType == DB.StorageType.Integer:
                    source_param_dict[param.Id] = param.AsInteger()
        for param in new_sheet.GetOrderedParameters():
            if (
                param.Definition.BuiltInParameter != DB.BuiltInParameter.SHEET_NUMBER
                and  param.Definition.BuiltInParameter != DB.BuiltInParameter.SHEET_NAME
                and param.Id in source_param_dict):
                if param.StorageType == DB.StorageType.String:
                    try:
                        param.Set(source_param_dict[param.Id].decode('utf-8'))
                    except Exception:
                        pass
                elif param.StorageType == DB.StorageType.Integer:
                    param.Set(source_param_dict[param.Id])

    copy_element_ids = []

    elements_on_sheet = db.Collector(
        view=sheet.Id,
        is_not_type=True
    ).get_elements()
    for element in elements_on_sheet:
        if not isinstance(element.unwrap(), DB.Viewport):
            copy_element_ids.append(element.Id)
    if copy_element_ids:
        with db.Transaction('Copy View Contents'):
            DB.ElementTransformUtils.CopyElements(
                sheet.unwrap(),
                List[DB.ElementId](copy_element_ids),
                new_sheet,
                None,
                None
            )
