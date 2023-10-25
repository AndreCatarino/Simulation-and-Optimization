from dataclasses import dataclass


@dataclass
class ExampleDailyOutsideTemperature:
    """Outside temperature in degrees Celsius"""

    value = [
        9.05,
        8.38,
        7.61,
        6.85,
        6.41,
        5.66,
        5.77,
        5.02,
        4.97,
        5.15,
        7.26,
        8.06,
        8.47,
        8.59,
        8.86,
        8.87,
        8.86,
        8.71,
        8.36,
        8.11,
        7.87,
        7.7,
        7.98,
        7.62,
    ]
    temperatura_entrada_agua = [x * 0.9 for x in value]

    # temperatura_saida_agua = 50

    # def temperatura_entrada_no_banho(self, potencia):
    #    return [value * potencia for value in self.value]


@dataclass
class ExampleBoilerTemperature:
    """Boiler temperature in degrees Celsius"""

    value = [
        9.05,
        8.38,
        7.61,
        6.85,
        6.41,
        5.66,
        5.77,
        5.02,
        4.97,
        5.15,
        7.26,
        8.06,
        8.47,
        8.59,
        8.86,
        8.87,
        8.86,
        8.71,
        8.36,
        8.11,
        7.87,
        7.7,
        7.98,
        7.62,
    ]

    temperature = [x * 2 for x in value]


@dataclass
class ExampleDailyEnergyCost:
    """Energy cost in eur per kWh"""

    value = [
        0.5266399999999999,
        0.45166399999999995,
        0.34220000000000006,
        0.32719999999999994,
        0.3608,
        0.45879199999999987,
        0.4177600000000001,
        0.43716800000000006,
        0.4400000000000001,
        0.44004800000000005,
        0.440016,
        0.4400000000000001,
        0.4400000000000001,
        0.4412,
        0.4412,
        0.44480000000000003,
        0.44160000000000005,
        0.44160000000000005,
        0.45439999999999997,
        0.45439999999999997,
        0.4512,
        0.4400000000000001,
        0.428208,
        0.49184000000000005,
    ]


@dataclass
class ExampleBoilerPressure:
    value = [
        0.5266399999999999,
        0.45166399999999995,
        0.34220000000000006,
        0.32719999999999994,
        0.3608,
        0.45879199999999987,
        0.4177600000000001,
        0.43716800000000006,
        0.4400000000000001,
        0.44004800000000005,
        0.440016,
        0.4400000000000001,
        0.4400000000000001,
        0.4412,
        0.4412,
        0.44480000000000003,
        0.44160000000000005,
        0.44160000000000005,
        0.45439999999999997,
        0.45439999999999997,
        0.4512,
        0.4400000000000001,
        0.428208,
        0.49184000000000005,
    ]

    pressure = [x * 4.3 for x in value]


TEMPERATURA_IDEAL = 40