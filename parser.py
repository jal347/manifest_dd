import csv
import os
import re

import numpy as np
import pandas
from biothings import config
from biothings.utils.dataload import dict_convert, dict_sweep

logging = config.logger

process_key = lambda k: k.replace(" ", "_").lower()


def load_annotations(data_folder):
    infile = os.path.join(data_folder, "var_drug_ann.tsv")
    assert os.path.exists(infile)
    dat = pandas.read_csv(infile, sep="\t", quoting=csv.QUOTE_NONE).to_dict(orient="records")
    results = {}
    for rec in dat:
        if not rec["Gene"] or pandas.isna(rec["Gene"]):
            # logging.warning("No gene information for annotation ID '%s'", rec["Annotation ID"])
            continue
        _id = re.match(".* \((.*?)\)", rec["Gene"]).groups()[0]
        rec = dict_convert(rec, keyfn=process_key)
        # remove NaN values, not indexable
        rec = dict_sweep(rec, vals=[np.nan])
        results.setdefault(_id, []).append(rec)
    for _id, docs in results.items():
        doc = {"_id": _id, "annotations": docs}
        yield doc
