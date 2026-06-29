# prediction mapping
class_names={y:x for x,y in train_gen.class_indices.items()}

material_map=(df.drop_duplicates("category").set_index("category")["material"].to_dict())

recyclable_map=(df.drop_duplicates("category").set_index("category")["recyclable"].to_dict())



## rule engine: to futher filter out items that are not dry,clean or rigid based on blue recyling bin rules
def rule_engine(category,is_clean,is_dry,is_rigid):
  recyclable=recyclability(category)

  material=get_material(category)

  if not is_clean:
    return{"Explanantion":"residues can contaminate entire batches of recyclables"}

  if not is_dry:
    return{"Explanation":"Wet recyclables lower material recovery quality"}

  if material=="plastic" and not is_rigid:
    return{"Explanation":"Soft plastics such as bags,films and wrappers can become entangled in sorting machines"}

  if recyclable==False:
    return{"Explanation":f"{category} cannot be recylced in the Singapore Blue Bin"}

  elif recyclable==True:
    return{"Explanation":f"{category} can be recycled in the Singapore Blue Bin"}
