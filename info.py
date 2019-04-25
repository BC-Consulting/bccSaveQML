# -*- coding: utf-8 -*-
#
# Plugin parameters (c) GeoProc.com 2019
#
#    This plugin is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This plugin is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this plugin. If not, see <http://www.gnu.org/licenses/>.
#
#===============================================================================
#V2.0.0 - 23 April 2019
#===============================================================================
#
currVersion   = '2.0.0'                                                         #Current plugin version
currDate      = '23 April 2019'                                                 #Date of publication
inMenu        = "Actions"                                                       #Menu that will host the plugin
MSG_BOX_TITLE = "Save QML"                                                      #Plugin title
AppName       = "bccSaveQML"                                                    #Plugin name
Author        = "GeoProc.com - info at geoproc dot com"                         #Author
resourcesIcon = ":/plugins/bccSaveQML/icon.png"                                 #Icon for the plugin menu
HlpURL        = "http://www.geoproc.com/free/bccSaveQML.html"
Sinfo         = "Save the style of each selected layer in qml files."           #Short info displayed when user hover on the menu
Linfo         = Sinfo                                                           #Info displayed in the Description field of the plugin manager
longDesc      = ("""<h2>bccSaveQML</h2>
<p>%s</p>

<p>Save the style of each selected layer in qml files.<br>
The qml filename is the same as the layer files name.</p>

<p align='right'>For more information click <a href='%s'>here</a></p>
""" % (Linfo, HlpURL))                                                          #Info displayed in the about box
rep           = "zzzzzzzzzz"                                                    #
#
#===============================================================================
#
def Usage(longDesc = ""):
    """ Return legal info message about the plugin """
    #
    import platform
    from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
    #
    L = """<p align='center'>
                         <b>%s</b><br />
                           (c) GeoProc.com 2019<br />&nbsp;<br />
                                Version: %s<br />
                                 %s</p>
    %s
    <hr />
    <font color="#999999">
    <h3>Legalese</h3>
    <p>This plugin is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version.</p>
    <p>This plugin is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
    more details.</p>
    <p>You should have received a copy of the GNU General Public License along
    with this plugin. If not, see [<a href="http://www.gnu.org/licenses/"
    target="blank">http://www.gnu.org/licenses/</a>].</p>
    </font>
    <p>&nbsp;</p>
    <p align="center"><i>Python %s - Qt %s - PyQt %s on %s</i></p>""" % \
    (MSG_BOX_TITLE, str(currVersion), str(currDate), longDesc,
     platform.python_version(), QT_VERSION_STR, PYQT_VERSION_STR,
     platform.system())
    #
    return L
#
#===============================================================================
#
def About(iface):
    """ Show about message """
    #
    from PyQt5.QtWidgets import QMessageBox
    #
    QMessageBox.about(iface, MSG_BOX_TITLE, Usage(longDesc))    
#
#===============================================================================
#
def GetHelp(iface):
    """ Show help page """
    #
    helpfile = "/free/"+ AppName +".html"
    url = "http://www.geoproc.com" + helpfile
    iface.openURL(url, False)
#
#===============================================================================