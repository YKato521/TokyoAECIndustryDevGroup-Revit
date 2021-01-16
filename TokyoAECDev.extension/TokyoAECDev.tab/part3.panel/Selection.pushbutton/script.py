from Autodesk.Revit.DB import BuiltInParameter
from Autodesk.Revit.UI.Selection import ObjectType
from rpw import uidoc
from revitron import Selection, _
# from selection_engine import selectionEngine
"""
sel_engine = selectionEngine()

def main():
    if not __shiftclick__:
        sel_engine.select_by_name()
    else:
        sel_engine.select_by_param()
"""

if __name__ == "__main__":
    # main()
    uidoc.Selection.PickObject(ObjectType.Element)