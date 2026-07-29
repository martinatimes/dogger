import csv

from config import CSV_HEADERS


class CSVExporter:

    def export(self, records, filename):

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as csvfile:

            writer = csv.DictWriter(
                csvfile,
                fieldnames=CSV_HEADERS
            )

            writer.writeheader()

            for record in records:
                writer.writerow(record)
