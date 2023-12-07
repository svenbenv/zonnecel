try:
    from nsp2visasim import sim_pyvisa as pyvisa
except ModuleNotFoundError:
    import pyvisa

# In this class the arduino device is defined and binary voltages are converted to voltages in units of volts
class ArduinoVISADevice:

    """In this class, the Arduino is read and the voltages are calculated."""

    def __init__(self, port):
        """The initial function of the class where the used port is defined and read.

        Args:
            port (string): The port in which the cable is plugged in.
        """
        rm = pyvisa.ResourceManager("@py")
        self.ports = rm.list_resources()
        self.port = port
        self.device = rm.open_resource(
            port, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):

        """Shows which port is used.

        Returns:
            *IDN: The port the cable is plugged in.
        """

        return self.device.query("*IDN?")

    def set_output_value(self, value):

        """An initial value for channel 0 is given.

        Args:
            value (float): A voltage for channel 0.
        """
        self.binary_value = int((value * 1023) / 3.3)
        self.device.query(f"OUT:CH0 {self.binary_value}")

        return

    def get_output_value(self):

        """The input value for channel 0 is measured/calculated.

        Returns:
            output_value: The voltage measured in channel 0.
        """
        output_value = int(self.device.query(f"OUT:CH0?"))

        return output_value

    def get_input_voltage(self, channel):

        """Converts binary voltages to a voltage in units of volts.

        Args:
            channel (int): An available channel.

        Returns:
            input_voltage: Calculates voltage for given channel.
        """

        self.input_voltage = int(self.device.query(f"MEAS:CH{channel}?")) * (3.3 / 1024)

        return self.input_voltage

    def turn_off_device(self):

        """The device is turned off by setting the voltage of channel 0 to 0 volts."""

        self.device.query(f"OUT:CH0 {0}")


# All useable ports are shown
def list_devices():

    """Lists available ports.

    Returns:
        ports: A list of ports available.
    """
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return ports