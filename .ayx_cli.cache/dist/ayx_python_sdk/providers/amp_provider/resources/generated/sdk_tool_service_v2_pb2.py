# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk_tool_service_v2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import close_outgoing_anchor_pb2 as close__outgoing__anchor__pb2
from . import incoming_connection_complete_pb2 as incoming__connection__complete__pb2
from . import translate_message_data_pb2 as translate__message__data__pb2
from . import outgoing_metadata_push_pb2 as outgoing__metadata__push__pb2
from . import output_message_data_pb2 as output__message__data__pb2
from . import password_data_pb2 as password__data__pb2
from . import plugin_initialization_data_pb2 as plugin__initialization__data__pb2
from . import dcm_e_pb2 as dcm__e__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19sdk_tool_service_v2.proto\x12\x03sdk\x1a\x1b\x63lose_outgoing_anchor.proto\x1a\"incoming_connection_complete.proto\x1a\x1ctranslate_message_data.proto\x1a\x1coutgoing_metadata_push.proto\x1a\x19output_message_data.proto\x1a\x13password_data.proto\x1a plugin_initialization_data.proto\x1a\x0b\x64\x63m_e.proto\"\x94\x03\n\tControlIn\x12\x43\n\x1aplugin_initialization_data\x18\x01 \x01(\x0b\x32\x1d.sdk.PluginInitializationDataH\x00\x12\x34\n\x12translated_message\x18\x02 \x01(\x0b\x32\x16.sdk.TranslatedMessageH\x00\x12/\n\x12\x64\x65\x63rypted_password\x18\x03 \x01(\x0b\x32\x11.sdk.PasswordDataH\x00\x12\x38\n\x0fnotify_complete\x18\x04 \x01(\x0b\x32\x1d.sdk.ControlIn.NotifyCompleteH\x00\x12+\n\x0e\x64\x63m_e_response\x18\x05 \x01(\x0b\x32\x11.sdk.DcmEResponseH\x00\x12G\n\x1cincoming_connection_complete\x18\x06 \x01(\x0b\x32\x1f.sdk.IncomingConnectionCompleteH\x00\x12\x0e\n\x06msg_id\x18\x07 \x01(\t\x1a\x10\n\x0eNotifyCompleteB\t\n\x07payload\"\xf3\x02\n\nControlOut\x12\x36\n\x11outgoing_metadata\x18\x01 \x01(\x0b\x32\x19.sdk.OutgoingMetadataPushH\x00\x12\x30\n\x0eoutput_message\x18\x02 \x01(\x0b\x32\x16.sdk.OutputMessageDataH\x00\x12\x36\n\x11translate_message\x18\x03 \x01(\x0b\x32\x19.sdk.TranslateMessageDataH\x00\x12-\n\x10\x64\x65\x63rypt_password\x18\x04 \x01(\x0b\x32\x11.sdk.PasswordDataH\x00\x12;\n\x10\x63onfirm_complete\x18\x05 \x01(\x0b\x32\x1f.sdk.ControlOut.ConfirmCompleteH\x00\x12)\n\rdcm_e_request\x18\x06 \x01(\x0b\x32\x10.sdk.DcmERequestH\x00\x12\x0e\n\x06msg_id\x18\x07 \x01(\t\x1a\x11\n\x0f\x43onfirmCompleteB\t\n\x07payload\"\xf3\x02\n\x10RecordTransferIn\x12\x41\n\x10incoming_records\x18\x01 \x01(\x0b\x32%.sdk.RecordTransferIn.IncomingRecordsH\x00\x12=\n\x0erecord_request\x18\x02 \x01(\x0b\x32#.sdk.RecordTransferIn.RecordRequestH\x00\x12G\n\x1cincoming_connection_complete\x18\x03 \x01(\x0b\x32\x1f.sdk.IncomingConnectionCompleteH\x00\x1a\x63\n\x0fIncomingRecords\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x14\n\x0c\x65nd_of_chunk\x18\x04 \x01(\x08\x1a$\n\rRecordRequest\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\tB\t\n\x07payload\"\"\n\x0bWantRecords\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\"c\n\x0fOutgoingRecords\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x14\n\x0c\x65nd_of_chunk\x18\x04 \x01(\x08\"\xb5\x01\n\x11RecordTransferOut\x12(\n\x0cwant_records\x18\x01 \x01(\x0b\x32\x10.sdk.WantRecordsH\x00\x12\x30\n\x10outgoing_records\x18\x02 \x01(\x0b\x32\x14.sdk.OutgoingRecordsH\x00\x12\x39\n\x15\x63lose_outgoing_anchor\x18\x03 \x01(\x0b\x32\x18.sdk.CloseOutgoingAnchorH\x00\x42\t\n\x07payload2\x80\x01\n\tSdkToolV2\x12.\n\x07\x43ontrol\x12\x0e.sdk.ControlIn\x1a\x0f.sdk.ControlOut(\x01\x30\x01\x12\x43\n\x0eRecordTransfer\x12\x15.sdk.RecordTransferIn\x1a\x16.sdk.RecordTransferOut(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sdk_tool_service_v2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONTROLIN._serialized_start=255
  _CONTROLIN._serialized_end=659
  _CONTROLIN_NOTIFYCOMPLETE._serialized_start=632
  _CONTROLIN_NOTIFYCOMPLETE._serialized_end=648
  _CONTROLOUT._serialized_start=662
  _CONTROLOUT._serialized_end=1033
  _CONTROLOUT_CONFIRMCOMPLETE._serialized_start=1005
  _CONTROLOUT_CONFIRMCOMPLETE._serialized_end=1022
  _RECORDTRANSFERIN._serialized_start=1036
  _RECORDTRANSFERIN._serialized_end=1407
  _RECORDTRANSFERIN_INCOMINGRECORDS._serialized_start=1259
  _RECORDTRANSFERIN_INCOMINGRECORDS._serialized_end=1358
  _RECORDTRANSFERIN_RECORDREQUEST._serialized_start=1360
  _RECORDTRANSFERIN_RECORDREQUEST._serialized_end=1396
  _WANTRECORDS._serialized_start=1409
  _WANTRECORDS._serialized_end=1443
  _OUTGOINGRECORDS._serialized_start=1445
  _OUTGOINGRECORDS._serialized_end=1544
  _RECORDTRANSFEROUT._serialized_start=1547
  _RECORDTRANSFEROUT._serialized_end=1728
  _SDKTOOLV2._serialized_start=1731
  _SDKTOOLV2._serialized_end=1859
# @@protoc_insertion_point(module_scope)