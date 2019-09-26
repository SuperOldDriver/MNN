# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Gather(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGather(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Gather()
        x.Init(buf, n + offset)
        return x

    # Gather
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Gather
    def Tindices(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Gather
    def Tparams(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Gather
    def ValidateIndices(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Gather
    def Axis(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def GatherStart(builder): builder.StartObject(4)
def GatherAddTindices(builder, Tindices): builder.PrependInt32Slot(0, Tindices, 0)
def GatherAddTparams(builder, Tparams): builder.PrependInt32Slot(1, Tparams, 0)
def GatherAddValidateIndices(builder, validateIndices): builder.PrependBoolSlot(2, validateIndices, 0)
def GatherAddAxis(builder, axis): builder.PrependInt32Slot(3, axis, 0)
def GatherEnd(builder): return builder.EndObject()