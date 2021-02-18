#region Namespaces
using Autodesk.Revit.ApplicationServices;
using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.DB.ExtensibleStorage;
using Autodesk.Revit.UI;
using System;
using System.IO;
using System.Reflection;

#endregion

namespace OgreCall.pushbutton
{
    [Transaction(TransactionMode.Manual)]
    public class Command : IExternalCommand
    {
        [Obsolete]
        public Result Execute(
          ExternalCommandData commandData,
          ref string message,
          ElementSet elements)
        {
            UIApplication uiapp = commandData.Application;
            UIDocument uidoc = uiapp.ActiveUIDocument;
            Application app = uiapp.Application;
            Document doc = uidoc.Document;

            string Path = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            string ImageFileName = "GitHub\\TokyoAECIndustryDevGroup-Revit\\TokyoAECDev.extension\\TokyoAECDev.tab\\cstest.panel\\OgreCall.pushbutton\\Image\\Ogre.jpg";

            string ImagePath = Path + "\\" + ImageFileName;

            ImagePlacementOptions Opt = new ImagePlacementOptions();

            // Create View

            ViewSheet vs = null;

            using (Transaction tx = new Transaction(doc))
            {
                tx.Start("Create View");
                vs = ViewSheet.Create(doc, ElementId.InvalidElementId);
                vs.Name = "Ogre";
                ImageType IT = ImageType.Create(doc, ImagePath);
                ImageInstance ImageonSheet =  ImageInstance.Create(doc, vs, IT.Id, Opt);

                Guid schemaGuid = new Guid("67DA32DE-E851-4DAD-B5EA-5450897DBFF0");
                Schema schema = Schema.Lookup(schemaGuid);

                if (schema == null)
                {
                    SchemaBuilder schemaBuilder = new SchemaBuilder(schemaGuid);

                    schemaBuilder.SetReadAccessLevel(AccessLevel.Public);
                    schemaBuilder.SetWriteAccessLevel(AccessLevel.Public);
                    schemaBuilder.SetVendorId("TokyoAECIndustryDevGroup");
                    schemaBuilder.SetSchemaName("OgreSample");
                    schemaBuilder.SetDocumentation("Sheet & ImageInstance ElementId");
                    FieldBuilder sheetBuilder = schemaBuilder.AddSimpleField("CreatedSheet", typeof(ElementId));
                    sheetBuilder.SetDocumentation("Sheet ElementId");

                    FieldBuilder imageBuilder = schemaBuilder.AddSimpleField("CreatedImage", typeof(ElementId));
                    imageBuilder.SetDocumentation("Sheet ElementId");

                    schema = schemaBuilder.Finish();
                }

                DataStorage createdData = DataStorage.Create(vs.Document);
                Entity entity = new Entity(schema);
                Field sheetfield =  schema.GetField("CreatedSheet");
                entity.Set<ElementId>(sheetfield, vs.Id, DisplayUnitType.DUT_UNDEFINED);
                Field imagefield = schema.GetField("CreatedImage");
                entity.Set<ElementId>(imagefield, ImageonSheet.Id, DisplayUnitType.DUT_UNDEFINED);
                createdData.SetEntity(entity);
                tx.Commit();
            }

            if(vs != null)
            {
                uidoc.ActiveView = (View)vs;
            }

            return Result.Succeeded;
        }
    }
}
