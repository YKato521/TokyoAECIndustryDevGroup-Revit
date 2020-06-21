# -*- coding: utf-8 -*-
from pyrevit import revit
import sheet_duplicate


def main():
    sheet_order_dict = sheet_duplicate.get_sheet_order_dict()
    sheet_list = sheet_duplicate.sheet_selection()

    with revit.TransactionGroup('Create Sheet'):
        for sheet in sheet_list:
            sheet_order_dict, new_sheet = sheet_duplicate.create_new_sheet(
                sheet,
                sheet_order_dict)
            sheet_duplicate.duplicate_sheet_contents(
                sheet,
                new_sheet)


if __name__ == "__main__":
    main()
