from networkml.pandas_csv_importer import WS_FIELDS
from networkml.featurizers.features import Features


class Generic(Features):

    def all(self, rows_f):
        return [{field: row.get(field, '') for field in WS_FIELDS} for row in rows_f()]