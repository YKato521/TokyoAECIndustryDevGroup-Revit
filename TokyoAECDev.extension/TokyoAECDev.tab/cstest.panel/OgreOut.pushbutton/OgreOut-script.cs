#region Namespaces
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Autodesk.Revit.ApplicationServices;
using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.DB.ExtensibleStorage;
using Autodesk.Revit.UI;
using Autodesk.Revit.UI.Selection;
#endregion

namespace OgreOut.pushbutton
{
    [Transaction(TransactionMode.Manual)]
    public class Command : IExternalCommand
    {
        public Result Execute(
          ExternalCommandData commandData,
          ref string message,
          ElementSet elements)
        {
            UIApplication uiapp = commandData.Application;
            UIDocument uidoc = uiapp.ActiveUIDocument;
            Application app = uiapp.Application;
            Document doc = uidoc.Document;


            FilteredElementCollector startingViewSettingsCollector = new FilteredElementCollector(doc)
                .OfClass(typeof(StartingViewSettings));

            View startingView = null;

            foreach (StartingViewSettings settings in startingViewSettingsCollector)
            {
                startingView = (View)doc.GetElement(settings.ViewId);
                if (startingView == null)
                {
                    startingView = new FilteredElementCollector(doc).OfClass(typeof(ViewPlan)).FirstElement() as View;
                }
            }

            Guid schemaGuid = new Guid("67DA32DE-E851-4DAD-B5EA-5450897DBFF0");

            FilteredElementCollector dscollector = new FilteredElementCollector(doc)
                .OfClass(typeof(DataStorage));

            Schema createdschema = Schema.Lookup(schemaGuid);

            DataStorage createdDS = null;
            Entity createdEntity = null;

            foreach (DataStorage ds in dscollector)
            {
                Entity entity = ds.GetEntity(createdschema);
                if (entity != null)
                {
                    createdDS = ds;
                    createdEntity = entity;
                }
            }

            if (createdDS != null)
            {
                uidoc.ActiveView = startingView;
                ElementId createdSheetId = createdEntity.Get<ElementId>(
                    "CreatedSheet");
                ElementId createdImageId = createdEntity.Get<ElementId>(
                    "CreatedImage");

                using (Transaction tx = new Transaction(doc))
                {
                    tx.Start("Ogre Out");
                    createdEntity.Clear("CreatedSheet");
                    createdEntity.Clear("CreatedImage");
                    doc.GetElement(createdSheetId).DeleteEntity(createdschema);
                    doc.Delete(createdImageId);
                    doc.Delete(createdSheetId);
                    tx.Commit();
                }
            }
            return Result.Succeeded;
        }
    }
}
