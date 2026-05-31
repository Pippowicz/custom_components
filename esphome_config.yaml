esphome:
  name: etamonitor
#  on_boot:
#    priority: 800
#    then:
#      - uart.write: [0x7B, 0x4D, 0x43, 34, 47, 0x0A, 0x08, 0x00, 0x0C, 0x08, 0x00, 0x0B, 0x08, 0x00, 0x0A, 0x08, 0x00, 0x46, 0x08, 0x00, 0x4B, 0x08, 0x00, 0x0F, 0x08, 0x00, 0x08, 0x08, 0x00, 0x09, 0x08, 0x00, 0x44, 0x08, 0x00, 0x42, 0x08, 0x00, 0x75, 0x7D]

#external_components:
#  - source:
#      type: git
#      url: https://github.com/ssieb/custom_components
#      ref: eta
#    components: [ eta_sh ]
#    refresh: 1min

external_components:
  - source: external_components/eta_sh

esp32:
  board: esp32dev
  framework:
    type: arduino

# Enable logging
logger:
  level: VERBOSE

# Enable Home Assistant API
api:
  encryption:
    key: !secret encryption_key

ota:
  - platform: esphome
    password: !secret ota_password
  
  
ethernet:
  type: LAN8720
  mdc_pin: GPIO23
  mdio_pin: GPIO18
  phy_addr: 0
  power_pin: GPIO12
  clk:
    mode: CLK_OUT
    pin: 17

uart:
  tx_pin: 4
  rx_pin: 36
  baud_rate: 19200
#  debug:
#    direction: BOTH
#    dummy_receiver: true
#    sequence:
#      - lambda: UARTDebug::log_string(direction, bytes);
#      - lambda: UARTDebug::log_hex(direction, bytes, ':');

#button:
#  - platform: template
#    name: "3 Werte"
#    on_press:
#      - logger.log: 3 Werte pressed
#      - uart.write: [0x7B, 0x4D, 0x43, 10, 39, 0x0A, 0x08, 0x00, 0x0C, 0x08, 0x00, 0x0B, 0x08, 0x00, 0x0A, 0x7D]

#  - platform: template
#    name: "11 Werte"
#    on_press:
#      - logger.log: 11 Werte pressed
#      - uart.write: [0x7B, 0x4D, 0x43, 34, 47, 0x0A, 0x08, 0x00, 0x0C, 0x08, 0x00, 0x0B, 0x08, 0x00, 0x0A, 0x08, 0x00, 0x46, 0x08, 0x00, 0x4B, 0x08, 0x00, 0x0F, 0x08, 0x00, 0x08, 0x08, 0x00, 0x09, 0x08, 0x00, 0x44, 0x08, 0x00, 0x42, 0x08, 0x00, 0x75, 0x7D]

#  - platform: template
#    name: "Cancel Abos"
#    on_press:
#      - logger.log: cancel pressed
#      - uart.write: [0x7B, 0x4D, 0x45, 0x00, 0x00, 0x7D]

eta_sh:  
  buffer_load:
    name: Pufferladezustand
  boiler_temperature:
    name: Kesseltemperatur
  fan_speed:
    name: Gebläsedrehzahl
    unit_of_measurement: RPM
  external_heater_temperature:
    name: Externer Brenner
  room1_temperature:
    name: Raumtemperatur
  room1_output_temperature:
    name: Vorlauf Raum 1
  outside_temperature:
    name: Außentemperatur
  return_temperature:
    name: Kesselrücklauf
  buffer_top_temperature:
     name: Puffer oben
  buffer_middle_temperature:
    name: Puffer mitte
  buffer_bottom_temperature:
    name: Puffer unten
  exhaust_temperature:
    name: Abgastemperatur
  oxygen_sensor:
    name: Restsauerstoff
  heater_status:
    name: "Status"
