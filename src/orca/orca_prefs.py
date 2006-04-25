# Orca
#
# Copyright 2004-2006 Sun Microsystems Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

"""Common utilities to manage the writing of the user preferences file."""

import os
import commands
import pprint
import settings

from orca_i18n import _  # for gettext support

def _createDir(dirname):
    """Creates the given directory if it doesn't already exist.
    """
    try:
        os.chdir(dirname)
    except:
        os.mkdir(dirname)

def _writePreferencesPreamble(prefs):
    """Writes the preamble to the user-settings.py file."""

    prefs.writelines("# user-settings.py - custom Orca settings\n")
    prefs.writelines("# Generated by orca-setup.  DO NOT EDIT THIS FILE!!!\n")
    prefs.writelines("# If you want permanent customizations that will not\n")
    prefs.writelines("# be overwritten, edit orca-customizations.py.\n")
    prefs.writelines("#\n")
    prefs.writelines("import re\n")
    prefs.writelines("\n")
    prefs.writelines("import orca.debug\n")
    prefs.writelines("import orca.settings\n")
    prefs.writelines("import orca.acss\n")
    prefs.writelines("\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_OFF\n")
    prefs.writelines("orca.debug.debugLevel = orca.debug.LEVEL_SEVERE\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_WARNING\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_INFO\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_CONFIGURATION\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_FINE\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_FINER\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_FINEST\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_ALL\n")
    prefs.writelines("\n")
    prefs.writelines("#orca.debug.eventDebugLevel = orca.debug.LEVEL_OFF\n")
    prefs.writelines("#orca.debug.eventDebugFilter =  None\n")
    prefs.writelines("#orca.debug.eventDebugFilter = re.compile('[\S]*focus|[\S]*activ')\n")
    prefs.writelines("#orca.debug.eventDebugFilter = re.compile('nomatch')\n")
    prefs.writelines("#orca.debug.eventDebugFilter = re.compile('[\S]*:accessible-name')\n")

    prefs.writelines("\n")
    prefs.writelines("#orca.debug.debugFile = open('debug.out', 'w', 0)\n")
    prefs.writelines("\n")

def _writePreferencesPostamble(prefs):
    """Writes the postamble to the user-settings.py file."""
    prefs.writelines("\ntry:\n")
    prefs.writelines("    __import__(\"orca-customizations\")\n")
    prefs.writelines("except ImportError:\n")
    prefs.writelines("    pass\n")

def _enableAccessibility():
    """Enables the GNOME accessibility flag.  Users need to log out and
    then back in for this to take effect.

    Returns True if an action was taken (i.e., accessibility was not
    set prior to this call).
    """

    alreadyEnabled = commands.getoutput(\
        "gconftool-2 --get /desktop/gnome/interface/accessibility")
    if alreadyEnabled != "true":
        os.system("gconftool-2 --type bool --set " \
                  + "/desktop/gnome/interface/accessibility true")

    return not alreadyEnabled

def _getSpeechServerFactoryString(factory):
    """Returns a string that represents the speech server factory passed in.

    Arguments:
    - factory: the speech server factory

    Returns a string suitable for the preferences file.
    """

    if not factory:
        return None
    elif isinstance(factory, basestring):
        return "'%s'" % factory
    else:
        return "'%s'" % factory.__name__

def _getSpeechServerString(server):
    """Returns a string that represents the speech server passed in.

    Arguments:
    - server: a speech server

    Returns a string suitable for the preferences file.
    """
    if not server:
        return None
    else:
        return repr(server.getInfo())

def _getVoicesString(voices):
    """Returns a string that represents the list of voices passed in.

    Arguments:
    - voices: a list of ACSS instances.

    Returns a string suitable for the preferences file.
    """

    voicesStr = "{\n"
    for voice in voices:
        voicesStr += "'%s' : orca.acss.ACSS(" % voice
        voicesStr += pprint.pformat(voices[voice]) + "),\n"
    voicesStr += "}"

    return voicesStr

def _getVerbosityString(verbosityLevel):
    """Returns a string that represents the verbosity level passed in."""
    if verbosityLevel == settings.VERBOSITY_LEVEL_BRIEF:
        return "orca.settings.VERBOSITY_LEVEL_BRIEF"
    elif verbosityLevel == settings.VERBOSITY_LEVEL_VERBOSE:
        return "orca.settings.VERBOSITY_LEVEL_VERBOSE"
    else:
        return "orca.settings.VERBOSITY_LEVEL_VERBOSE"

def _getBrailleRolenameStyleString(rolenameStyle):
    """Returns a string that represents the rolename style passed in."""
    if rolenameStyle == settings.BRAILLE_ROLENAME_STYLE_SHORT:
        return "orca.settings.BRAILLE_ROLENAME_STYLE_SHORT"
    elif rolenameStyle == settings.BRAILLE_ROLENAME_STYLE_LONG:
        return "orca.settings.BRAILLE_ROLENAME_STYLE_LONG"
    else:
        return "orca.settings.BRAILLE_ROLENAME_STYLE_LONG"

def readPreferences():
    """Returns a dictionary containing the names and values of the
    customizable features of Orca."""

    prefsDict = {}
    for key in settings.userCustomizableSettings:
        if settings.__dict__.has_key(key):
            prefsDict[key] = settings.__dict__[key]

    return prefsDict

def writePreferences(prefsDict):
    """Creates the directory and files to hold user preferences.  Note
    that callers of this method may want to consider using an ordered
    dictionary so that the keys are output in a deterministic order.

    Arguments:
    - prefsDict: a dictionary where the keys are orca preferences
    names and the values are the values for the preferences.

    Returns True if accessibility was enabled as a result of this
    call."""

    # Set up ~/.orca
    #
    orcaDir = os.path.join(os.environ["HOME"], ".orca")
    _createDir(orcaDir)

    # Set up ~/.orca/orca-scripts as a Python package
    #
    orcaScriptDir = os.path.join(orcaDir, "orca-scripts")
    _createDir(orcaScriptDir)
    initFile = os.path.join(orcaScriptDir, "__init__.py")
    if not os.path.exists(initFile):
        os.close(os.open(initFile, os.O_CREAT, 0700))

    # Write ~/.orca/user-settings.py
    #
    prefs = open(os.path.join(orcaDir, "user-settings.py"), "w")
    _writePreferencesPreamble(prefs)
    for key in settings.userCustomizableSettings:
        if prefsDict.has_key(key):
            if key == "voices":
                value = _getVoicesString(prefsDict[key])
            elif key == "speechServerInfo":
                value = _getSpeechServerString(prefsDict[key])
            elif key == "speechServerFactory":
                value = _getSpeechServerFactoryString(prefsDict[key])
            elif key.endswith("VerbosityLevel"):
                value = _getVerbosityString(prefsDict[key])
            elif key == "brailleRolenameStyle":
                value = _getBrailleRolenameStyleString(prefsDict[key])
            else:
                value = prefsDict[key]
            prefs.writelines("orca.settings.%s = %s\n" % (key, value))
    _writePreferencesPostamble(prefs)
    prefs.close()

    # Return True if this caused accessibility to be enabled
    # as a result of this call.
    #
    return _enableAccessibility()
