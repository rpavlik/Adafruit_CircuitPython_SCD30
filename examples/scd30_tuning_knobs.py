# SPDX-FileCopyrightText: 2020 by Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
# pylint:disable=protected-access
import time
import board
import busio
import adafruit_scd30

i2c = busio.I2C(board.SCL, board.SDA)
scd = adafruit_scd30.SCD30(i2c)
# scd.temperature_offset = 5.5
print("Temperature offset:", scd.temperature_offset)

# scd.measurement_interval = 4
print("Measurement interval:", scd.measurement_interval)

# scd.self_calibration_enabled = True
print("Self-calibration enabled:", scd.self_calibration_enabled)

# scd.ambient_pressure = 1100
print("Ambient Pressure:", scd.ambient_pressure)

# scd.altitude = 1600
print("Altitude:", scd.altitude, "meters above sea level")

# scd.forced_recalibration_reference = 409
print("Forced recalibration reference:", scd.forced_recalibration_reference)
print("")
while True:
    data = scd._data_available
    if data:
        print("Data Available!")
        print("CO2:", scd.co2, "PPM")
        print("Temperature:", scd._temperature, "degrees C")
        print("Humidity::", scd._relative_humitidy, "%%rH")
        print("")
        print("Waiting for new data...")
        print("")

    time.sleep(0.5)
