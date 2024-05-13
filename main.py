from machine import Pin, SoftI2C
import time

BH1750_I2C_ADDRESS = 0x23

i2c = SoftI2C(scl=Pin(33, pull=Pin.PULL_UP), sda=Pin(32, pull=Pin.PULL_UP))
print([hex(i) for i in i2c.scan()])

i2c.writeto(BH1750_I2C_ADDRESS, bytearray([0x00]))
print(f"BH1750 sensor found at {BH1750_I2C_ADDRESS:#x}")

def main():
    set_continuous_high_res_mode()

    while True:
        time.sleep_ms(120)

        read_buffer = bytearray(2)
        i2c.readfrom_into(BH1750_I2C_ADDRESS, read_buffer, len(read_buffer))

        raw_lux = (read_buffer[0] << 8 | read_buffer[1])
        lux = round(raw_lux / 1.2, 1)
        print(f"Illuminance: {lux} lx")

        time.sleep_ms(500)

def set_continuous_high_res_mode():
    write_buffer = bytearray([0x10])
    i2c.writeto(BH1750_I2C_ADDRESS, write_buffer)

main()
