from Bio import SeqIO
import json

infile = open("sequence.gb", "r")
record = list(SeqIO.parse(infile, "gb"))[0]
infile.close()

out_dict = {}

for r in record.features:
    if r.type == "CDS":
        locus_tag = " ".join(r.qualifiers["locus_tag"])
        note = " ".join(r.qualifiers.get("note", [""]))
        product = " ".join(r.qualifiers["product"])
        location_start = r.location.nofuzzy_start
        location_end = r.location.nofuzzy_end
        strand = r.location.strand
        # print(
        #     locus_tag,
        #     location_start,
        #     location_end,
        #     strand,
        #     note,
        #     product
        # )
        out_dict[product] = {
            "start": location_start,
            "stop": location_end,
            "strand": strand,
            "note": note
        }
        
with open("mpx_def.js", "w") as outjs:
    outjs.write("// Attempt at mangling https://www.ncbi.nlm.nih.gov/nuccore/ON563414.3 into JSON\n")
    outjs.write("// Quite possibly Not Correct\n\n")
    outjs.write("var mpx_def = ")
    outjs.write(json.dumps(out_dict, indent=2))