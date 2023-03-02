from pyvolt import network, nv_powerflow
import cimpy

res = cimpy.cim_import(
    ["./net.xml"], "cgmes_v2_4_15")
system = network.System()

base_apparent_power = 25
system.load_cim_data(res['topology'], base_apparent_power=25
                     )

# Execute power flow analysis
results_pf, num_iter_cim = nv_powerflow.solve(system)

for node in results_pf.nodes:
    print('{}={}'.format(node.topology_node.uuid, node.voltage))
