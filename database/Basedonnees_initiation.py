import sqlalchemy
from database.identifiant import ID, mdp
"""
Connection à la BDD
"""
connection = sqlalchemy.create_engine('postgresql://'+ID+':'+ mdp + '@172.16.99.2:5432/radio_libre')

metadonnees = sqlalchemy.MetaData()

table_morceaux = sqlalchemy.Table('morceaux',metadonnees,
                                  sqlalchemy.Column('titre',sqlalchemy.String),
                                  sqlalchemy.Column('album',sqlalchemy.String),
                                  sqlalchemy.Column('artiste',sqlalchemy.String),
                                  sqlalchemy.Column('genre',sqlalchemy.String),
                                  sqlalchemy.Column('sousgenre',sqlalchemy.String),
                                  sqlalchemy.Column('duree', sqlalchemy.Integer),
                                  sqlalchemy.Column('format',sqlalchemy.String),
                                  sqlalchemy.Column('polyphonie',sqlalchemy.Integer),
                                  sqlalchemy.Column('chemin',sqlalchemy.String)
                                  )

# s = sqlalchemy.select([table_morceaux])
# 
# 
# 
# conn = connection.connect()
# result = conn.execute(s)
# 
# for row in result:
#     print(row)
#     
