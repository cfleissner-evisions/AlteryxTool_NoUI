# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk_engine_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import dcm_e_pb2 as dcm__e__pb2
from . import outgoing_metadata_push_pb2 as outgoing__metadata__push__pb2
from . import outgoing_record_packet_push_pb2 as outgoing__record__packet__push__pb2
from . import outgoing_data_push_pb2 as outgoing__data__push__pb2
from . import output_message_data_pb2 as output__message__data__pb2
from . import password_data_pb2 as password__data__pb2
from . import sdk_tool_service_startup_info_pb2 as sdk__tool__service__startup__info__pb2
from . import translate_message_data_pb2 as translate__message__data__pb2
from . import transport_pb2 as transport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18sdk_engine_service.proto\x12\x03sdk\x1a\x0b\x64\x63m_e.proto\x1a\x1coutgoing_metadata_push.proto\x1a!outgoing_record_packet_push.proto\x1a\x18outgoing_data_push.proto\x1a\x19output_message_data.proto\x1a\x13password_data.proto\x1a#sdk_tool_service_startup_info.proto\x1a\x1ctranslate_message_data.proto\x1a\x0ftransport.proto2\x96\x04\n\tSdkEngine\x12V\n!ConfirmSdkEngineServiceConnection\x12\x1e.sdk.SdkToolServiceStartupInfo\x1a\x11.sdk.ReturnStatus\x12\x44\n\x14PushOutgoingMetadata\x12\x19.sdk.OutgoingMetadataPush\x1a\x11.sdk.ReturnStatus\x12L\n\x18PushOutgoingRecordPacket\x12\x1d.sdk.OutgoingRecordPacketPush\x1a\x11.sdk.ReturnStatus\x12<\n\x10PushOutgoingData\x12\x15.sdk.OutgoingDataPush\x1a\x11.sdk.ReturnStatus\x12\x45\n\x10TranslateMessage\x12\x19.sdk.TranslateMessageData\x1a\x16.sdk.TranslatedMessage\x12\x33\n\rOutputMessage\x12\x16.sdk.OutputMessageData\x1a\n.sdk.Empty\x12\x37\n\x0f\x44\x65\x63ryptPassword\x12\x11.sdk.PasswordData\x1a\x11.sdk.PasswordData\x12*\n\x03\x44\x63m\x12\x10.sdk.DcmERequest\x1a\x11.sdk.DcmEResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sdk_engine_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SDKENGINE._serialized_start=270
  _SDKENGINE._serialized_end=804
# @@protoc_insertion_point(module_scope)
