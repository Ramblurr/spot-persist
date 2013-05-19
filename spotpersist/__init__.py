import json

def parse_json(handle):
    """
    Parse an open file handle (.read()-able interfaces)

    Returns metadata dictionary and list of message dicts
    """
    data = json.load(handle)
    try:
        metadata = data['response']['feedMessageResponse']['feed']
        messages = data['response']['feedMessageResponse']['messages']['message']
        return metadata, messages
    except KeyError:
        return None

def parse_xml(handle):
    raise Exception("parse_xml is not yet implemented")
