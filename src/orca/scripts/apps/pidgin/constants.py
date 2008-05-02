# Orca
#
# Copyright 2004-2007 Sun Microsystems Inc.
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

"""Custom script for gaim.  This provides the ability for Orca to
monitor both the IM input and IM output text areas at the same time.

The following script specific key sequences are supported:

  Insert-h      -  Toggle whether we prefix chat room messages with
                   the name of the chat room.
  Insert-[1-9]  -  Speak and braille a previous chat room message.
"""

__id__        = "$Id$"
__version__   = "$Revision$"
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2005-2007 Sun Microsystems Inc."
__license__   = "LGPL"

# Whether we prefix chat room messages with the name of the chat room.
#
prefixChatMessage = False

# Whether we announce when a buddy is typing.
#
announceBuddyTyping = False

# Whether we provide chat room specific message histories.
#
chatRoomHistories = False

# Possible ways of how Orca should speak pidgin chat messages.
#
SPEAK_ALL_MESSAGES              = 0
SPEAK_CHANNEL_WITH_FOCUS        = 1
SPEAK_ALL_CHANNELS_WHEN_FOCUSED = 2

# Indicates how pidgin chat messages should be spoken.
#
speakMessages = SPEAK_ALL_MESSAGES

