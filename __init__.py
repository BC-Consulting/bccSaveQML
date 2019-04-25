# -*- coding: utf-8 -*-
#
# Standard stub (c) GeoProc.com 2019
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
def classFactory(iface):
    # load Plugin class from file bccSaveQML.py
    from .bccSaveQML import bccSaveQML
    return bccSaveQML(iface)
#
#===============================================================================