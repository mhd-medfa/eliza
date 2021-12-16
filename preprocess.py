import re
import pandas as pd

with open ("pilot-script.txt", encoding="utf8") as myfile:
    data = myfile.read().splitlines()

processed_data = pd.DataFrame(columns=["name", "line"])
for line in data:
    processed_line = re.sub("[\(\[].*?[\)\]]", "", line)
    processed_line = processed_line.replace("’", "'")
    processed_line = processed_line.replace("…", "...")
    processed_line = processed_line.replace('–', '-')
    processed_line = processed_line.strip().split(":")
    if len(processed_line)==2 and (processed_line[0] not in ["Scene", "Story"]):
        processed_data = processed_data.append({"name": processed_line[0].strip(), "line": processed_line[1]}, ignore_index=True)

processed_data.to_csv(r'pilot-script.csv', header = True, encoding="utf8")
