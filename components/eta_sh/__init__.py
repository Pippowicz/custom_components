import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.components import uart, sensor
from esphome.const import (
    CONF_ID,
    CONF_TEMPERATURE,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLUME,
    ICON_GAUGE,
    ICON_THERMOMETER,
    UNIT_CELSIUS,
    UNIT_PERCENT,
)

MULTI_CONF = True
DEPENDENCIES = ['uart']
AUTO_LOAD = ['sensor']

eta_sh_ns = cg.esphome_ns.namespace('eta_sh')

ETA_SH = eta_sh_ns.class_('ETA_SH', cg.Component, uart.UARTDevice)

CONF_BOILER_TEMPERATURE = "boiler_temperature"
CONF_BUFFER_BOTTOM_TEMPERATURE = "buffer_bottom_temperature"
CONF_BUFFER_MIDDLE_TEMPERATURE = "buffer_middle_temperature"
CONF_BUFFER_TOP_TEMPERATURE = "buffer_top_temperature"
CONF_EXHAUST_TEMPERATURE = "exhaust_temperature"
CONF_OUTSIDE_TEMPERATURE = "outside_temperature"
CONF_RETURN_TEMPERATURE = "return_temperature"
CONF_BUFFER_LOAD = "buffer_load"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ETA_SH),
    cv.Optional(CONF_BOILER_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        icon=ICON_THERMOMETER,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    cv.Optional(CONF_BUFFER_BOTTOM_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        icon=ICON_THERMOMETER,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    cv.Optional(CONF_BUFFER_MIDDLE_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        icon=ICON_THERMOMETER,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    cv.Optional(CONF_BUFFER_TOP_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        icon=ICON_THERMOMETER,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    cv.Optional(CONF_EXHAUST_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        icon=ICON_THERMOMETER,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    cv.Optional(CONF_OUTSIDE_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        icon=ICON_THERMOMETER,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    cv.Optional(CONF_RETURN_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        icon=ICON_THERMOMETER,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    cv.Optional(CONF_BUFFER_LOAD): sensor.sensor_schema(
        unit_of_measurement=UNIT_PERCENT,
        icon=ICON_GAUGE,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_VOLUME,
    ),
}).extend(uart.UART_DEVICE_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_BOILER_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_BOILER_TEMPERATURE])
        cg.add(var.set_boiler_temp_sensor(sens))

    if CONF_RETURN_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_RETURN_TEMPERATURE])
        cg.add(var.set_return_temp_sensor(sens))

    if CONF_BUFFER_BOTTOM_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_BUFFER_BOTTOM_TEMPERATURE])
        cg.add(var.set_buffer_bottom_temp_sensor(sens))

    if CONF_BUFFER_MIDDLE_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_BUFFER_MIDDLE_TEMPERATURE])
        cg.add(var.set_buffer_middle_temp_sensor(sens))

    if CONF_BUFFER_TOP_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_BUFFER_TOP_TEMPERATURE])
        cg.add(var.set_buffer_top_temp_sensor(sens))

    if CONF_EXHAUST_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_EXHAUST_TEMPERATURE])
        cg.add(var.set_exhaust_temp_sensor(sens))

    if CONF_OUTSIDE_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_OUTSIDE_TEMPERATURE])
        cg.add(var.set_outside_temp_sensor(sens))

    if CONF_BUFFER_LOAD in config:
        sens = await sensor.new_sensor(config[CONF_BUFFER_LOAD])
        cg.add(var.set_buffer_load_sensor(sens))

