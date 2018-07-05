# New job no.1: write a dumper for the Ensembl plant 
# The following code originated from 
# https://github.com/biothings/mygene.info/blob/master/src/hub/dataload/sources/ensembl/dump.py#L214


	 def get_gene__main(self, outfile, debug=False):
        header = ['taxonomy_id',
                  'ensembl_gene_id',
                  'symbol',
                  'gene_chrom_start', 'gene_chrom_end', 'chr_name', 'chrom_strand',
                  'description','type_of_gene']
        attributes = ["ensembl_gene_id",
                      "external_gene_name",   # symbols, called "external_gene_id" before release 76
                      "start_position", "end_position", "chromosome_name", "strand",
                      "description","gene_biotype"]
        self._fetch_data(outfile, attributes, header=header, debug=debug)
        
	def get_translation__main(self, outfile, debug=False):
        header = ['taxonomy_id',
                  'gene_stable_id',
                  'transcript_stable_id',
                  'translation_stable_id']
        attributes = ["ensembl_gene_id",
                      "ensembl_transcript_id",
                      "ensembl_peptide_id"]
        self._fetch_data(outfile, attributes, header=header, debug=debug)

    def get_xref_entrezgene(self, outfile, debug=False):
        header = ['taxonomy_id',
                  'gene_stable_id',
                  'dbprimary_id']
        attributes = ["ensembl_gene_id",
                      "entrezgene"]
        filters = ["with_entrezgene"]
        self._fetch_data(outfile, attributes, filters, header=header, debug=debug)

    def get_profile(self, outfile, debug=False):
        header = ['taxonomy_id',
                  'gene_stable_id',
                  'transcript_stable_id',
                  'translation_stable_id',
                  'profile_id']
        attributes = ["ensembl_gene_id",
                      "ensembl_transcript_id",
                      "ensembl_peptide_id",
                      "pfscan"]
        filters = ["with_pfscan"]
        self._fetch_data(outfile, attributes, filters, header=header, debug=debug)

    def get_interpro(self, outfile, debug=False):
        header = ['taxonomy_id',
                  'gene_stable_id',
                  'transcript_stable_id',
                  'translation_stable_id',
                  'interpro_id', 'short_description', 'description']
        attributes = ["ensembl_gene_id",
                      "ensembl_transcript_id",
                      "ensembl_peptide_id",
                      "interpro", "interpro_short_description", "interpro_description"]
        filters = ["with_interpro"]
        self._fetch_data(outfile, attributes, filters, header=header, debug=debug)

    def get_pfam(self, outfile, debug=False):
        header = ['taxonomy_id',
                  'gene_stable_id',
                  'transcript_stable_id',
                  'translation_stable_id',
                  'pfam']
        attributes = ["ensembl_gene_id",
                      "ensembl_transcript_id",
                      "ensembl_peptide_id",
                      "pfam"]
        filters = ["with_pfam"]
        self._fetch_data(outfile, attributes, filters, header=header, debug=debug)
