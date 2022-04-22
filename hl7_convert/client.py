import json
from hl7apy.parser import parse_message
from hl7apy.parser import Message

class HL7Client(object):
    """
    Hl7 client class
    """

    def hl7_str_to_dict(self, s: str, use_long_name: bool =True) -> dict:
        """Convert an HL7 string to a dictionary
        :param s: The input HL7 string
        :param use_long_name: Whether or not to use the long names
                              (e.g. "patient_name" instead of "pid_5")
        :returns: A dictionary representation of the HL7 message
        """
        s = s.replace("\n", "\r")
        m = parse_message(s)
        return self.hl7_message_to_dict(m, use_long_name=use_long_name)

    def hl7_message_to_dict(self, m: Message, use_long_name: bool =True) -> dict:
        """Convert an HL7 message to a dictionary
        :param m: The HL7 message as returned by :func:`hl7apy.parser.parse_message`
        :param use_long_name: Whether or not to use the long names
                              (e.g. "patient_name" instead of "pid_5")
        :returns: A dictionary representation of the HL7 message
        """
        if m.children:
            d = {}
            for c in m.children:
                name = str(c.name).lower()
                if use_long_name:
                    name = str(c.long_name).lower() if c.long_name else name
                dictified = self.hl7_message_to_dict(c, use_long_name=use_long_name)
                if name in d:
                    if not isinstance(d[name], list):
                        d[name] = [d[name]]
                    d[name].append(dictified)
                else:
                    d[name] = dictified
            return d
        else:
            return m.to_er7()

    def hl7tojsonconvert(self, message: str) -> str:
        res = self.hl7_str_to_dict(message)
        # return json.dumps(res, indent=4)
        return json.dumps(res)


