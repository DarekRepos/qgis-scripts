from qgis.core import (
    QgsRasterLayer,
    QgsProject,
    QgsPointXY,
    QgsRaster,
    QgsRasterShader,
    QgsColorRampShader,
    QgsSingleBandPseudoColorRenderer,
    QgsSingleBandColorDataRenderer,
    QgsSingleBandGrayRenderer,
)

from qgis.PyQt.QtGui import (
    QColor,
)

for layer in QgsProject.instance().mapLayers().values():
    print (layer.name())
    if isinstance(layer, QgsVectorLayer):
        layer_type = layer.geometryType()
        if layer_type == QgsWkbTypes.PointGeometry:
            print ("PointGeometry")
    if isinstance(layer, QgsRasterLayer):
        layer.renderer().setOpacity(0.5)
        layer.triggerRepaint()
        print ("raster type")      