# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugin_initialization_data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import incoming_anchor_pb2 as incoming__anchor__pb2
from . import outgoing_anchor_pb2 as outgoing__anchor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n plugin_initialization_data.proto\x12\x03sdk\x1a\x15incoming_anchor.proto\x1a\x15outgoing_anchor.proto\"\xb3\x02\n\x18PluginInitializationData\x12\x11\n\tconfigXml\x18\x01 \x01(\t\x12,\n\x0fincomingAnchors\x18\x02 \x03(\x0b\x32\x13.sdk.IncomingAnchor\x12,\n\x0foutgoingAnchors\x18\x03 \x03(\x0b\x32\x13.sdk.OutgoingAnchor\x12K\n\x0f\x65ngineConstants\x18\x04 \x03(\x0b\x32\x32.sdk.PluginInitializationData.EngineConstantsEntry\x12#\n\nupdateMode\x18\x05 \x01(\x0e\x32\x0f.sdk.UpdateMode\x1a\x36\n\x14\x45ngineConstantsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*3\n\nUpdateMode\x12\n\n\x06UM_Run\x10\x00\x12\x0b\n\x07UM_Full\x10\x01\x12\x0c\n\x08UM_Quick\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugin_initialization_data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLUGININITIALIZATIONDATA_ENGINECONSTANTSENTRY._options = None
  _PLUGININITIALIZATIONDATA_ENGINECONSTANTSENTRY._serialized_options = b'8\001'
  _UPDATEMODE._serialized_start=397
  _UPDATEMODE._serialized_end=448
  _PLUGININITIALIZATIONDATA._serialized_start=88
  _PLUGININITIALIZATIONDATA._serialized_end=395
  _PLUGININITIALIZATIONDATA_ENGINECONSTANTSENTRY._serialized_start=341
  _PLUGININITIALIZATIONDATA_ENGINECONSTANTSENTRY._serialized_end=395
# @@protoc_insertion_point(module_scope)
