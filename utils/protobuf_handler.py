import json
from google.protobuf.json_format import MessageToJson

# Note: In a real scenario, you would import the generated _pb2 classes
# Example: from .protos import player_data_pb2

class ProtobufHandler:
    @staticmethod
    def decode_to_json(pb_message_class, binary_data):
        """
        Decodes binary protobuf data into a JSON string using a provided message class.
        """
        try:
            message = pb_message_class()
            message.ParseFromString(binary_data)
            return json.loads(MessageToJson(message))
        except Exception as e:
            return {"error": "Decoding failed", "details": str(e)}