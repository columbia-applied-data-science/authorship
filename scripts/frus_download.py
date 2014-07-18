# This script downloads 150 random documents each written Kissinger, Rostow,
# and Bundy from the FRUS database.
import os
import yaml

from declass.utils.database import DBCONNECT

DATA = os.path.join(os.environ['DATA'], 'authorship',  'frus')
KISSINGER = os.path.join(DATA, 'kissinger')
ROSTOW = os.path.join(DATA, 'rostow')
BUNDY = os.path.join(DATA, 'bundy')

for directory in [KISSINGER, ROSTOW, BUNDY]:
    try:
        os.makedirs(directory)
    except OSError:
        pass

peoplemapping = [('Kissinger', KISSINGER),
                 ('Rostow', ROSTOW),
                 ('Bundy', BUNDY)]

login_file = os.path.join(os.getenv('HOME'), '.declass_ro')
login_info = yaml.load(open(login_file))
host_name = login_info['host_name']
db_name = 'declassification_frus2'
user_name = login_info['user_name']
pwd = login_info['pwd']

dbCon = DBCONNECT(host_name, db_name, user_name, pwd)

for person, folder in peoplemapping:
    query = "SELECT id, body FROM docs "
    query += " where p_from = '%s' ORDER BY RAND() limit 150;" % person
    results = dbCon.run_query(query)
    for result in results:
        docid = result['id']
        body = result['body']
        filepath = os.path.join(folder, docid + '.txt')
        with open(filepath, 'w') as f:
            f.write(body)

dbCon.close()
