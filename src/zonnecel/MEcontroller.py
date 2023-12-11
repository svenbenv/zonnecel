import pyvisa


class ArduinoVISADevice:
    def __init__(self, port):
        """connect arduino

        Args:
            poort (poort name): select poort 
        """
        rm = pyvisa.ResourceManager("@py")

        self.device = rm.open_resource(
        port, read_termination="\r\n", write_termination="\n"
        )
        self.device.query("*IDN?")

    def get_identification(self):
        """ get indentification from arduino

        Arguments:
            self (self): get indentification from arduino
        
        Returns:
            ID: Idenification of pyvisa device (expecting :Arduino VISA firmware v1.0.0)

        """
        ID = self.device.query("*IDN?")
        return ID

    def set_output_value(self, value):
        """input ADC value up 0 up to 1024

        Args:
            value (int): give ADC value on channel 0 arduino device
        """
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        """inquery input value on channel 0

        Returns:
            int: input ADC value on drduino device
        """
        value = self.device.query(f"OUT:CH0?")
        return value

    def get_input_value(self,channel):
        """measure in put value on channel 1/2

        Args:
            channel (int): select which channel to get output from

        Returns:
            int : measured output value on channel 1/2
        """
        value = self.device.query(f"MEAS:CH{channel}?")
        return value 

    def get_input_voltage(self, channel): 
        """convert measured output ADC value on channel 1/2 into voltage

        Args:
            channel (int): select which channel to get output from

        Returns:
            float: measured output value on channel 1/2
        """
        value = 3.3 * (int(self.device.query(f"MEAS:CH{channel}?"))/1024)
        return value
    def clear(self):
        """
        close arduinoPyvisa dive
        """
        self.device.close()

def list_devices():
    """inquire available poorts

    Returns:
        string: available poorts
    """
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return ports

#x = ArduinoVISADevice("ASRL7::INSTR")