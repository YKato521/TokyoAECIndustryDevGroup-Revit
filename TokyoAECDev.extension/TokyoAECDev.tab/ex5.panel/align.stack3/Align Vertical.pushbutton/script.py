# -*- coding: utf-8 -*-
from Autodesk.Revit import DB, UI
from pyrevit import revit

uiapp = __revit__ # noqa F821
uidoc = uiapp.ActiveUIDocument
app = uiapp.Application
doc = uidoc.Document


class CustomISelectionFilter(UI.Selection.ISelectionFilter):
    def __init__(self, nom_class):
        self.nom_class = nom_class

    def AllowElement(self, e):
        if isinstance(e, self.nom_class):
            return True
        else:
            return False


def main():
    source_vp_reference = uidoc.Selection.PickObject(
        UI.Selection.ObjectType.Element,
        CustomISelectionFilter(DB.Viewport),
        "Select Source Viewport")
    target_vps_reference = uidoc.Selection.PickObjects(
        UI.Selection.ObjectType.Element,
        CustomISelectionFilter(DB.Viewport),
        "Select Target Viewport(s)"
    )
    source_vp = doc.GetElement(source_vp_reference.ElementId)
    source_vp_xyz = source_vp.GetBoxCenter()
    with revit.Transaction("Aign ViewPort - Vertical"):
        for target_vp_reference in target_vps_reference:
            target_vp = doc.GetElement(target_vp_reference.ElementId)
            delta = DB.XYZ(0.0, source_vp_xyz.Y - target_vp.GetBoxCenter().Y, 0.0)
            target_vp.Location.Move(delta)


if __name__ == "__main__":
    main()
