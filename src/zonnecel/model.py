import math

import numpy

from zonnecel.controller import ArduinoVISADevice, list_devices


# In this class an experiment is done n times and errors and averages are calculated.
class DiodeExperiment:
    """In this class the port is chosen and the mean values and standard deviations of I and U are calculated and put in lists."""

    def __init__(self, start, stop, n):
        """Gives all initial variables and lists needed in this class.

        Args:
            start (int): Initial value of voltage.
            stop (int): Final value of voltage.
            n (int): The experiment from initial to final value is repeated n times.
            seperate_U_LED (list): List of all voltage values in one run.
            seperate_I_LED (list): List of all current values in one run.
            average_U_list (list): list of average voltage values after experiment is repeated n times.
            average_I_list (list): list of average curent values after experiment is repeated n times.
            U_error (list): list of standard deviations of voltage values.
            I_error (list): list of standard deviations of current values.
        """

        self.start = start
        self.stop = stop
        # The experiment is repeated n times:
        self.n = n
        self.separate_U_LED = []
        self.separate_I_LED = []
        self.average_U_list = []
        self.average_I_list = []
        self.U_error = []
        self.I_error = []

    def scan(self, chosen_port):

        """Calculates averages and standard deviations of voltages and currents (in SI-units) by repeating experiment n times.

        Returns:
            average_U_list: List of average voltages.
            average_I_list: List of average currents.
            error_U: Standard deviations of average voltages.
            error_I: Standard deviations of average currents.
        """
        print(list_devices())
        port = chosen_port
        device = ArduinoVISADevice(port=port)

        voltage_range = int(((self.stop - self.start) * 1023) / 3.3)
        for i in numpy.linspace(self.start, self.stop, voltage_range):

            self.separate_U_LED = []
            self.separate_I_LED = []

            for j in range(0, self.n):

                device.set_output_value(value=i)
                U1 = device.get_input_voltage(channel=1)
                U_resistance_volt = device.get_input_voltage(channel=2)
                U_LED_volt = U1 - U_resistance_volt
                I_LED_ampere = U_resistance_volt / 220
                # These formulae follow out of Ohm's law.
                self.separate_U_LED.append(U_LED_volt)
                self.separate_I_LED.append(I_LED_ampere)

            average_U = numpy.mean(self.separate_U_LED)
            self.average_U_list.append(average_U)
            error_U = numpy.std(self.separate_U_LED) / math.sqrt(self.n)
            self.U_error.append(error_U)
            average_I = numpy.mean(self.separate_I_LED)
            self.average_I_list.append(average_I)
            error_I = numpy.std(self.separate_I_LED) / math.sqrt(self.n)
            self.I_error.append(error_I)

        device.turn_off_device()

        return self.average_U_list, self.average_I_list, error_U, error_I


def info(chosen_port):
    """Gives information about chosen device.

    Args:
        chosen_port (string): This is the chosen device.
    """
    port = chosen_port
    device = ArduinoVISADevice(port=port)
    print(device.get_identification())