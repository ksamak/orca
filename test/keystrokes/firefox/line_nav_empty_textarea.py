#!/usr/bin/python

"""Test of line navigation."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Control>Home"))
sequence.append(utils.AssertPresentationAction(
    "1. Top of file",
    ["BRAILLE LINE:  'Before the entry'",
     "     VISIBLE:  'Before the entry', cursor=1",
     "SPEECH OUTPUT: 'Before the entry'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "2. Line Down",
    ["BRAILLE LINE:  'Label:'",
     "     VISIBLE:  'Label:', cursor=1",
     "SPEECH OUTPUT: 'Label'",
     "SPEECH OUTPUT: ':'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "3. Line Down",
    ["BRAILLE LINE:  'Label  $l'",
     "     VISIBLE:  'Label  $l', cursor=7",
     "SPEECH OUTPUT: 'Label entry'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "4. Line Down",
    ["BRAILLE LINE:  'After the entry'",
     "     VISIBLE:  'After the entry', cursor=1",
     "SPEECH OUTPUT: 'After the entry'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "5. Line Up",
    ["BRAILLE LINE:  'Label  $l'",
     "     VISIBLE:  'Label  $l', cursor=7",
     "SPEECH OUTPUT: 'Label entry'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "6. Line Up",
    ["BRAILLE LINE:  'Label:'",
     "     VISIBLE:  'Label:', cursor=1",
     "SPEECH OUTPUT: 'Label'",
     "SPEECH OUTPUT: ':'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "7. Line Up",
    ["BRAILLE LINE:  'Before the entry'",
     "     VISIBLE:  'Before the entry', cursor=1",
     "SPEECH OUTPUT: 'Before the entry'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
