#
# General:
#      This file is pary of .NET Bridge
#
# Copyright:
#      2010 Jonathan Shore
#      2017 Jonathan Shore and Contributors
#
# License:
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at:
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

from pydotnet.clr.CLRMessage import CLRMessage
from pydotnet.core.io import *



class CLRObjectRefArray (CLRMessage):
    """
    Class for object-ref arrays
    """

    def __init__(self, v = []):
        super().__init__ (CLRMessage.TypeObjectArray, v)


    def serialize (self, sock: BinarySocketWriter):
        """
        Serialize message
        """
        super().serialize(sock)
        sock.writeInt32(len(self.value))
        for v in self.value:
            msg = CLRMessage.createByValue(v)
            msg.serialize(sock)


    def deserialize (self, sock: BinarySocketReader):
        """
        Deserialize message (called after magic & type read)
        """
        super().deserialize(sock)

        vlen = sock.readInt32()
        msgs = [CLRMessage.read(sock) for i in range(0,vlen)]
        self.value = [msg.toValue() for msg in msgs]


