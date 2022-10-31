import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import (
    CONF_ID,
    CONF_MODEL,
    CONF_TIME,
    CONF_VERSION,
)
from .. import (
    vbus_ns,
    VBus,
    CONF_VBUS_ID,
    CONF_DELTASOL_C,
    CONF_DELTASOL_CS2,
    CONF_DELTASOL_BS_PLUS,
)

DeltaSol_C = vbus_ns.class_('DeltaSol_C_tsensor', cg.Component)
DeltaSol_CS2 = vbus_ns.class_('DeltaSol_CS2_tsensor', cg.Component)
DeltaSol_BS_Plus = vbus_ns.class_('DeltaSol_BS_Plus_tsensor', cg.Component)

CONFIG_SCHEMA = cv.typed_schema(
    {
        CONF_DELTASOL_C: cv.COMPONENT_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(DeltaSol_C),
                cv.GenerateID(CONF_VBUS_ID): cv.use_id(VBus),
                cv.Optional(CONF_TIME): text_sensor.text_sensor_schema(text_sensor.TextSensor),
            }
        ),

        CONF_DELTASOL_CS2: cv.COMPONENT_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(DeltaSol_CS2),
                cv.GenerateID(CONF_VBUS_ID): cv.use_id(VBus),
                cv.Optional(CONF_VERSION): text_sensor.text_sensor_schema(text_sensor.TextSensor),
            }
        ),

        CONF_DELTASOL_BS_PLUS: cv.COMPONENT_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(DeltaSol_BS_Plus),
                cv.GenerateID(CONF_VBUS_ID): cv.use_id(VBus),
                cv.Optional(CONF_TIME): text_sensor.text_sensor_schema(text_sensor.TextSensor),
                cv.Optional(CONF_VERSION): text_sensor.text_sensor_schema(text_sensor.TextSensor),
            }
        ),
    },
    key=CONF_MODEL, lower=True, space="_",
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    if config[CONF_MODEL] == CONF_DELTASOL_C:
        cg.add(var.set_command(0x0100))
        cg.add(var.set_source(0x4212))
        cg.add(var.set_dest(0x0010))
        if CONF_TIME in config:
            sens = await text_sensor.new_text_sensor(config[CONF_TIME])
            cg.add(var.set_time_tsensor(sens))

    elif config[CONF_MODEL] == CONF_DELTASOL_CS2:
        cg.add(var.set_command(0x0100))
        cg.add(var.set_source(0x1121))
        cg.add(var.set_dest(0x0010))
        if CONF_VERSION in config:
            sens = await text_sensor.new_text_sensor(config[CONF_VERSION])
            cg.add(var.set_version_tsensor(sens))

    elif config[CONF_MODEL] == CONF_DELTASOL_BS_PLUS:
        cg.add(var.set_command(0x0100))
        cg.add(var.set_source(0x4221))
        cg.add(var.set_dest(0x0010))
        if CONF_TIME in config:
            sens = await text_sensor.new_text_sensor(config[CONF_TIME])
            cg.add(var.set_time_tsensor(sens))
        if CONF_VERSION in config:
            sens = await text_sensor.new_text_sensor(config[CONF_VERSION])
            cg.add(var.set_version_tsensor(sens))

    vbus = await cg.get_variable(config[CONF_VBUS_ID])
    cg.add(vbus.register_listener(var))
