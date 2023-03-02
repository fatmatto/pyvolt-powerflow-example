from pyvolt import network, nv_powerflow
import cimpy

res = cimpy.cim_import(["./net.xml"], "cgmes_v2_4_15")
system = network.System()

base_apparent_power = 25
system.load_cim_data(res["topology"], base_apparent_power=25)

# Execute power flow analysis
results_pf, num_iter_cim = nv_powerflow.solve(system)

for node in results_pf.nodes:
    print("Node: {} => ".format(node.topology_node.uuid))
    print("\tBase Voltage: {} kV".format(node.topology_node.baseVoltage))
    print("\tBase Current: {}".format(node.topology_node.base_current))
    print("\tBase Apparent Power: {}".format(node.topology_node.base_apparent_power))
    print("\tVoltage: {}".format(node.voltage))
    print("\tVoltage_PU: {}".format(node.voltage_pu))
    print("\tCurrent: {}".format(node.current))
    print("\tCurrent_PU: {}".format(node.current_pu))
    print("\tPower: {}".format(node.power))
    print("\tPower_PU: {}".format(node.power_pu))
