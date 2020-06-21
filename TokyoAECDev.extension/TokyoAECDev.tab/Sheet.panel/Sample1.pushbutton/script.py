from Autodesk.Revit import DB
from rpw import db

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
def colection_original():   
    uiapp = __revit__
    uidoc = uiapp.ActiveUIDocument
    app = uiapp.Application
    doc = uidoc.Document

    sheets = (
        DB.FilteredElementCollector(doc)
        .OfClass(DB.ViewSheet)
        .WhereElementIsNotElementType()
        .ToElements())
    for sheet in sheets:
        print(sheet)
        print(sheet.Name)


# RPW UnwrappedElement
def collection_unwrapped():
    sheets = db.Collector(of_class='ViewSheet', is_not_type=True)
    for sheet in sheets:
        print(sheet)
        print(sheet.Name)


# RPW WrappedElement
def collection_wrapped():
    sheets = db.Collector(of_class='ViewSheet', is_not_type=True).get_elements()
    for sheet in sheets:
        print(sheet)
        print(sheet.name)


# RPW db.ViewSheet
def collection_view():
    sheets = db.ViewSheet.collect()
    for sheet in sheets:
        print(sheet)
        print(sheet.Name)


def main():
    # colection_original()
    collection_unwrapped()
    # collection_wrapped()
    # collection_view()


if __name__ == "__main__":
    main()
