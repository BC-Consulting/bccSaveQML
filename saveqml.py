import os

from PyQt5 import uic
from PyQt5 import Qt, QtWidgets

from qgis.core import QgsProject

from .info import About as iAbout


# This loads your .ui file so that PyQt can populate your plugin with the elements
#  from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'saveqml.ui'))


class SaveQmlDlg(QtWidgets.QDialog, FORM_CLASS):

    def __init__(self, parent=None):
        """Constructor."""
        super(SaveQmlDlg, self).__init__(parent)
        self.setupUi(self)

        # What we need from QGIS
        self.mainW = parent
        self.mapLayers = QgsProject.instance().mapLayers().values()

        # Setup our signals
        self.pbnClose.clicked.connect(self.reject)
        self.pbnAbout.clicked.connect(self.about)
        self.pbnApplyStyle.clicked.connect(self.DoIt)
        self.pbnSelectAllLayers.clicked.connect(self.SelAll)

        self.loadMapLayers()

    #----------------------------------------------------------------------------
    def about( self ):
        """ Info about this plugin """
        #
        iAbout(self.mainW)

    #----------------------------------------------------------------------------
    def DoIt( self ):
        """ Save style in qml for all selected layers """
        #
        n = 0
        selected = self.lvMapLayers.selectedIndexes()
        layer = None
        for i in selected:
            layername = i.data()
            #Find the layer in the TOC
            for layer in self.mapLayers:
                if layername == layer.name():
                    #Found
                    if self.saveQML( layer ):
                        n += 1
                    break
        QtWidgets.QMessageBox.information(self.mainW,u"bccSaveQML",
                                                   "Created %i qml files." % n )

    #----------------------------------------------------------------------------
    def saveQML( self, theLayer ):
        """  Save the layer style to a qml file
             theLayer: the layer object

             Returns True on success, False on failure
        """
        #
        try:
            layerName = self.getFilenameFromLayer( theLayer )
            if layerName == "":
                return False
            #
            layerQMLName = os.path.splitext( layerName )[ 0 ] + ".qml"
            _ , flg = theLayer.saveNamedStyle( layerQMLName )
            if flg:
                return True
            else:
                return False
        except:
            return False

    #----------------------------------------------------------------------------
    def getFilenameFromLayer( self, theLayer ):
        """  Return the physical filename from a layer
             theLayer: the layer object

             Returns the filename
        """
        #
        try:
            source = theLayer.source()
            source = str(source)
            source = source.split("|")[0]
            if not os.path.isfile(source):
                return ""
            return source
        except:
            return ""

    #----------------------------------------------------------------------------
    def loadMapLayers( self ):
        """ Create a list of map layers to show in the dialog """
        #
        layersNameList = []
        n = len( self.mapLayers )
        for Lay in self.mapLayers:
            layersNameList.append( Lay.name() )
        layersNameList.sort()
        #
        self.lvMapLayers.setModel( Qt.QStringListModel( layersNameList, self ) )
        self.lvMapLayers.setSelectionMode( Qt.QAbstractItemView.ExtendedSelection )
        self.lvMapLayers.setEditTriggers( Qt.QAbstractItemView.NoEditTriggers )
        self.label.setText( "Layers (%i):" % n )
        #
        if self.lvMapLayers.model().rowCount() == 0:
            self.pbnSelectAllLayers.setEnabled( False )

    #----------------------------------------------------------------------------
    def SelAll( self):
        """ Select all layers in the list """
        #
        self.lvMapLayers.selectAll()
        self.pbnSelectAllLayers.setEnabled( True )
        self.pbnApplyStyle.setEnabled( True )
#==============================================================================