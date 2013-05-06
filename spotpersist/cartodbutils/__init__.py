from cartodb import CartoDBAPIKey
import json
import datetime

#unique = "ALTER TABLE the_table ADD CONSTRAINT constraint_name UNIQUE (thecolumn);"

def quote(s):
    return "'" + s + "'"


class CartoTransaction(object):

    #_SQL_INSERT = "insert into {0} ( the_geom, type, happened_at, message, spotid ) values( g, t, h, m, i ) select {1} where {1} not in (select spotid from {0} where spotid = {1}
    _SQL_INSERT = "insert into %s ( the_geom, type, happened_at, message, spotid ) values( %s, %s, %s, %s, %s);"
    _SQL_DELETE = "delete from %s where spotid = %s;"

    def __init__(self, api_key, domain, table, debug = False):
        self.cl = CartoDBAPIKey(api_key, domain)
        self.table = table
        self.queries = []
        self.debug = debug

    def commit(self):

        if len(self.queries) == 0:
            return

        stmts = "\n".join(self.queries)
        query = "BEGIN;\n"
        query += stmts
        query += "COMMIT;\n"
        if self.debug:
            print query
        resp = self.cl.sql(query)
        if self.debug:
            print resp

    def _craft_insert(self, the_geom, event_type, happened_at, message, spotid):
        if happened_at is None:
            happened_at = ''
        if message is None:
            message = ''
        return self._SQL_INSERT % (self.table, the_geom , quote(event_type), quote(happened_at), quote(message), quote(spotid))

    def insert_point(self, point):
        the_geom = "ST_SetSRID(ST_Point(%s,%s), 4326)" %(point.longitude, point.latitude)
        insert = self._craft_insert(the_geom, "checkin", point.dateTime, point.messageContent, str(point.id))
        self.queries.append(insert)

    def update_line(self, spotid, coords, remove_first=False):
        geojson = json.dumps({ "type" : "MultiLineString", "coordinates": [coords] })
        the_geom = "ST_SetSRID(ST_GeomFromGeoJSON('%s'), 4326)" % (geojson)
        insert = self._craft_insert(the_geom, "track", str(datetime.datetime.now()), None, str(spotid))
        delete = self._SQL_DELETE % (self.table, quote(spotid))
        self.queries.append(delete)
        self.queries.append(insert)




