from gpiozero import MCP3008
adc = MCP3008(channel=0, device=0)
print(adc.value)