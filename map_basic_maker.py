import json

position = int(input("Position value: "))
capture = int(input("Capture value: "))

arc_map_step = []
for i in range(position + 1):
    arc_map_step.append({"position": i, "capture": capture})

output_json = {"steps": arc_map_step}
print(json.dumps(output_json, indent=2))