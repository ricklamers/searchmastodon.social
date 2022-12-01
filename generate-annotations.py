import pandas as pd
import json


with open("docs/instances.json") as f:
  instances = json.load(f)["instances"]


instances = sorted(instances, key=lambda instance: int(instance["users"]), reverse=True)

instances_en = list(filter(lambda instance: instance["info"] != None and "en" in instance["info"]["languages"], instances))


df = pd.DataFrame([instance["name"] for instance in instances_en][:2000])

df['URL'] = df[0].apply(lambda url: "*." + url + "/*")
df['Label'] = df[0].apply(lambda url: "_include_")
df['Score'] = df[0].apply(lambda url: "1.000000")

df = df.drop(labels=[0], axis=1)

df.to_csv("annotations.tsv", sep="\t", index=False)