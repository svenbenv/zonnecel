import numpy as np

from MEcontroller import ArduinoVISADevice, list_devices


# looping in range of 2 to thre 10th range, reaching maximum bit ADC value of the given LED.
class zonnecel_experiment:
    def __init__(self, port):  
        """init, inport class Arduinodevice from arduino_device

        Args:
            poort (string): selected poort
        """
        self.device = ArduinoVISADevice(port= port)  
        self.voltageLED = []
        self.amperage = []

    def scan(self, start, stop, n):
        """run measurement
            plot graph
            determine error

        Args:
            start (int): start ADC value
            stop (int): end ADC value
            n (int): times the measurement repeats

        Returns:
            lists: voltage on LED, current on LED, error voltage, error current
        """
        self.Verror = []
        self.Aerror = []
        for i in range(start, stop):
            Vrepeat = []
            Arepeat = []
            for a in range(0, n):

                self.device.set_output_value(i)
                ivalue1 = int(self.device.get_input_value(channel=1))
                ivalue2 = int(self.device.get_input_value(channel=2))
                iUled = ivalue1 - ivalue2
                U2 = 3.3 * (ivalue2 / 1024)
                Uled = 3.3 * (iUled / 1024)

                IL = U2 / 220
                Vrepeat.append(Uled)
                Arepeat.append(IL)
            meanv = np.mean(Vrepeat)
            meana = np.mean(Arepeat)
            self.Verror.append(np.std(Vrepeat) / np.sqrt(n))
            self.Aerror.append(np.std(Arepeat) / np.sqrt(n))
            self.voltageLED.append(meanv)
            self.amperage.append(meana)

        return self.voltageLED, self.amperage, self.Aerror, self.Verror

    # clear Device

    def close(self):
        self.device.clear()


def information(port):
    """get indenification for slected poort

    Args:
        poort (string): selected poort

    Returns:
        string: information idenificationstring of aruino device (expecting:Arduino VISA firmware v1.0.0 )
    """
    list = ArduinoVISADevice(port=port)
    ID = list.get_identification()
    return ID