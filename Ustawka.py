##Example=name
##Folder=folder

# Import required modules
import glob, os
from qgis.core import (
  QgsApplication,
  QgsDataSourceUri,
  QgsCategorizedSymbolRenderer,
  QgsClassificationRange,
  QgsPointXY,
  QgsProject,
  QgsExpression,
  QgsField,
  QgsFields,
  QgsFeature,
  QgsFeatureRequest,
  QgsFeatureRenderer,
  QgsGeometry,
  QgsGraduatedSymbolRenderer,
  QgsMarkerSymbol,
  QgsMessageLog,
  QgsRectangle,
  QgsRendererCategory,
  QgsRendererRange,
  QgsSymbol,
  QgsVectorDataProvider,
  QgsVectorLayer,
  QgsVectorFileWriter,
  QgsWkbTypes,
  QgsSpatialIndex,
  QgsVectorLayerUtils
)

from qgis.core.additions.edit import edit



#vlayer = QgsVectorLayer("D:/Projekty/QGIS_MPZP/MPZP/klasyfikacja-akustyczna/wadowicki/mpzp_Kalwaria_Zebrzydowska.shp", "mpzp_Kalwaria_Zebrzydowska", "ogr")
#if not vlayer.isValid():
#    print("Layer failed to load!")
#else:
#    for field in vlayer.fields():
#        print(field.name(), field.typeName())
        

vlayer = iface.activeLayer()
features = vlayer.getFeatures()

        
        
# Set the origin field
origin_field = 'oznaczenie'
# Set the target field
target_field = 'ozn'
print(target_field)

# Get index of target field
idx = vlayer.fields().indexFromName(target_field)
print(idx)

        # Iterate through each feature
for feat in vlayer.getFeatures():
    if feat.attribute(idx) == None:
        print(feat.attribute(idx))
            # Copy values from origin field to target field
        vlayer.changeAttributeValue(feat.id(), idx, feat[origin_field])		
