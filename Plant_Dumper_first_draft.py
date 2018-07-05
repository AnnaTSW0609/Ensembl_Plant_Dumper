import sys
import os
import time
from ftplib import FTP
import requests

import biothings, config
biothings.config_for_app(config)

from biothings.utils.common import timesofar, safewfile, is_int
from biothings.utils.hipchat import hipchat_msg
from biothings.utils.hub_db import get_src_dump
from biothings.utils.dataload import tab2list
from config import DATA_ARCHIVE_ROOT, logger as logging
from biothings.hub.dataload.dumper import HTTPDumper

XML_QUERY_TEMPLATE_EXAMPLE = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Query>
<Query  virtualSchemaName = "plants_mart" formatter = "TSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" >
			
	<Dataset name = "athaliana_eg_gene" interface = "default" >
		<Filter name = "biotype" value = "antisense_RNA"/>
		<Attribute name = "ensembl_gene_id" />
		<Attribute name = "start_position" />
		<Attribute name = "end_position" />
		<Attribute name = "external_gene_name" />
		<Attribute name = "chromosome_name" />
		<Attribute name = "strand" />
		<Attribute name = "description" />
		<Attribute name = "gene_biotype" />
	</Dataset>
</Query>
'''

XML_QUERY_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Query>
<Query  virtualSchemaName = "%(virtual_schema)s" formatter = "TSV" header = "0" uniqueRows = "1" count = "" datasetConfigVersion = "0.6" >
    <Dataset name = "%(dataset)s" interface = "default" >
        %(filters)s
        %(attributes)s
    </Dataset>
</Query>
'''

class BioMart(HTTPDumper):

    SRC_NAME = "ensembl"
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)

    ENSEMBL_FTP_HOST = "ftp.plant.ensembl.org"
    MART_URL = "https://plants.ensembl.org/biomart/martservice"
    #MART_URL = "http://uswest.ensembl.org/biomart/martservice"
    TEMPLATE = XML_QUERY_TEMPLATE
    species_li = []
    DUMP_METHOD = {"gene_emsembl_get_plant_gene.txt": "gene_emsembl_get_plant_gene"}

    SCHEDULE = "0 6 * * *"
    
    def gene_emsembl_get_plant_gene(self, outfile, debug=False):
        header = ['taxonomy_id',
                  'ensembl_gene_id',
                  'symbol',
                  'gene_chrom_start', 'gene_chrom_end', 'chr_name', 'chrom_strand',
                  'description','type_of_gene']
        attributes = ["ensembl_gene_id",
                      "external_gene_name",   # symbols, called "external_gene_id" before release 76
                      "start_position", "end_position", "chromosome_name", "strand",
                      "description","gene_biotype"]
        filters = ["Gene type: antisense_RNA"]
        self._fetch_data(outfile, attributes, header=header, debug=debug)
