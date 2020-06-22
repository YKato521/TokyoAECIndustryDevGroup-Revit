# -*- coding: utf-8 -*-
from Autodesk.Revit import DB, UI
from rpw import db, ui
from pyrevit import revit
import pickle
import os
from tempfile import gettempdir

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
    tempfile = os.path.join(gettempdir(), "ViewPort")
    try:
        with open(tempfile, "rf") as fp:
            source_point = pickle.load(fp)
    except Exception:
        message = 'を除外します'
        ui.forms.Alert(content=message, title="シート以外が選択されました", exit=True)
    target_vp_reference = uidoc.Selection.PickObject(
        UI.Selection.ObjectType.Element,
        CustomISelectionFilter(DB.Viewport),
        "Select Source Viewport")
    target_vp = doc.GetElement(target_vp_reference.ElementId)
    target_vp_xyz = target_vp.GetBoxCenter()

    with revit.Transaction("Move ViewPort Location"):
        delta = DB.XYZ(
            (source_point[0] - target_vp_xyz.X),
            (source_point[1] - target_vp_xyz.Y),
            (source_point[2] - target_vp_xyz.Z))
        target_vp.Location.Move(delta)


if __name__ == "__main__":
    main()
