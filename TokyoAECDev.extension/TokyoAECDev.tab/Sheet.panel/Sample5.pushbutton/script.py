# -*- coding: utf-8 -*-
from Autodesk.Revit import DB
from rpw import db, ui, doc
from pyrevit import revit
from System.Collections.Generic import List

# RPW WrappedElement


def get_sheet_order_dict():
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
    return sheet_order_dict


def sheet_selection():
    sheet_list = []

    elements = ui.Selection()    
    for el in elements:
        if isinstance(el, db.ViewSheet):
            sheet_list.append(el)
        else:
            message = '{}を除外します'.format(el.Name)
            ui.forms.Alert(content=message, title="シート以外が選択されました", exit=False)
    if not sheet_list:
        ui.forms.Alert(content='シートを選択してください', title="選択エラー", exit=True)
    return sheet_list


def get_sheet_number(sheet, new_sheet, sheet_order_dict):
    sheet_num = sheet.SheetNumber
    sheet_category = sheet_num[:2]
    new_sheet_order = int(sheet_order_dict[str(sheet_category)]) + 1
    if new_sheet_order < 10:
        new_sheet_number = str(sheet_category) + '0' + str(new_sheet_order)
    else:
        new_sheet_number = str(sheet_category) + str(new_sheet_order)
    new_sheet.SheetNumber = new_sheet_number
    sheet_order_dict[str(sheet_category)] = new_sheet_number
    return sheet_order_dict


def create_new_sheet(sheet, sheet_order_dict):
    source_param_dict = {}

    with db.Transaction('Create Sheet'):
        new_sheet = DB.ViewSheet.Create(
            doc,
            DB.ElementId.InvalidElementId
        )
        new_sheet.Name = 'Test'
        sheet_order_dict = get_sheet_number(sheet, new_sheet, sheet_order_dict)
        
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
    return sheet_order_dict, new_sheet


def duplicate_sheet_contents(sheet, new_sheet):
    copy_element_ids = []

    elements_on_sheet = db.Collector(
        view=sheet.Id,
        is_not_type=True
    ).get_elements()
    for element in elements_on_sheet:
        if isinstance(element.unwrap(), DB.Viewport):
            related_view = doc.GetElement(element.ViewId)
            if related_view.ViewType == DB.ViewType.Legend:
                new_view_id = related_view.Id
            else:
                with db.Transaction('Duplicate View'):
                    new_view_id = related_view.Duplicate(DB.ViewDuplicateOption.WithDetailing)

            with db.Transaction('Change View Port Type'):
                nvport = DB.Viewport.Create(
                        doc,
                        new_sheet.Id,
                        new_view_id,
                        element.GetBoxCenter())
                if nvport.GetTypeId() != element.GetTypeId():
                    nvport.ChangeTypeId(element.GetTypeId())

        else:
            copy_element_ids.append(element.Id)
    if copy_element_ids:
        with revit.Transaction('Copy View Contents'):
            new_contents = DB.ElementTransformUtils.CopyElements(
                sheet.unwrap(),
                List[DB.ElementId](copy_element_ids),
                new_sheet,
                None,
                None
            )
    return new_contents


def main():
    sheet_order_dict = get_sheet_order_dict()
    sheet_list = sheet_selection()

    with revit.TransactionGroup('Create Sheet'):
        for sheet in sheet_list:

            sheet_order_dict, new_sheet = create_new_sheet(sheet, sheet_order_dict)
            duplicate_sheet_contents(sheet, new_sheet)
            

if __name__ == "__main__":
    main()
