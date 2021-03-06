#!/usr/bin/python

"""Test of sayAll."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Add"))
sequence.append(utils.AssertPresentationAction(
    "1. KP_Add to do a SayAll",
    ["SPEECH OUTPUT: 'On weaponry:'",
     "SPEECH OUTPUT: 'NOBODY expects the Spanish Inquisition! Our chief weapon is surprise. Surprise and fear. Fear and surprise. Our two weapons are fear and surprise. And ruthless efficiency. Our three weapons are fear, surprise, and ruthless efficiency. And an almost fanatical devotion to the Pope. Our four. No. Amongst our weapons. Amongst our weaponry, are such elements as fear, surprise. I'll come in again. NOBODY expects the Spanish Inquisition! Amongst our weaponry are such diverse elements as: fear, surprise, ruthless efficiency, an almost fanatical devotion to the Pope, and nice red uniforms - Oh damn!'",
     "SPEECH OUTPUT: 'On old ladies:'",
     "SPEECH OUTPUT: 'Now old lady, you have one last chance. Confess the heinous sin of heresy, reject the works of the ungodly. Two last chances. And you shall be free. Three last chances. You have three last chances, the nature of which I have divulged in my previous utterance.'",
     "SPEECH OUTPUT: 'On castle decor:'",
     "SPEECH OUTPUT: 'Hm! She is made of harder stuff! Cardinal Fang! Fetch the COMFY CHAIR!'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
