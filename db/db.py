import csv
from datetime import datetime


HEADERS = ['Blockchain', 'Protocol', 'Token 0', 'Token 1', 'APR', 'Staked']


class Database:
    def __init__(self, blockchain):
        self._file_name = f"results/{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}_{blockchain}.csv"
        self._headers_added = False

    def add(self, rows):
        self._add_headers()
        with open(self._file_name, 'a') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)

    def _add_headers(self):
        if self._headers_added:
            return
        with open(self._file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
        self._headers_added = True
       
