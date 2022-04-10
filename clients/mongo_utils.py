import pymongo

from utils.logger import Logger
from utils.singelton import Singleton
from bson.json_util import loads, dumps
from CONSTANTS import SECRETS


class MongoUtils(metaclass=Singleton):
    _connection:pymongo.MongoClient = None
    db = SECRETS.MONGO_DB_NAME

    logger = Logger().get_logger()
    def __init__(self):
        if not self._connection:
            try:
                self._connection = pymongo.MongoClient(
                    SECRETS.MONGO_CLUSTER_ENDPOINT
                )
                self.logger.info(self._connection.server_info())
                self.logger.info("MongoDB Connection established for database: {}".format(self.db))
            except Exception as e:
                self.logger.error(f"Unable to connect to the server. having error : {e}")
                raise e

    def get_mongo_client(self):
        return self._connection

    def cms_db(self):
        return self._connection[self.db]

    def get_document(self, query, collection, result_type="json", db=db):
        if result_type != "json":
            return self._connection[db][collection].find(query)

        else:
            docs = []
            for doc in self._connection[db][collection].find(query):
                docs.append(doc)
            return loads(dumps(docs))

    def get_single_document(self, query, collection, db=db):
        document = self._connection[db][collection].find_one(query)
        if (document):
            return loads(dumps(document))
        else:
            return None

    def insert_document(self, document, collection, db=db):
        try:
            response = self._connection[db][collection].insert_one(document)
            self.logger.info("Inserted document {} in collection {}".format(document, collection))
            return response
        except Exception as e:
            raise e

    def update_document(self, query, document, collection, db=db):
        try:
            response = self._connection[db][collection].update_one(query, {"$set": document}, upsert=True)
            self.logger.info("Updated document {} in collection {}".format(document, collection))
            return response
        except Exception as e:
            raise e

    def delete_single_document(self, query, collection, db=db):
        response = self._connection[db][collection].delete_one(query)
        self.logger.info("Deleted from collection {} with query {}".format(collection, query))
        return response

    def delete_documents(self, query, collection, db=db):
        return self._connection[db][collection].delete_many(query)

    def remove_key_from_document(self, query, key_value_document, collection, db=db):
        if query and key_value_document:
            response = self._connection[db][collection].update_one(query, {"$unset": key_value_document})
            self.logger.info("Deleted keys {} from collection {}".format(key_value_document, collection))
            return response
        self.logger.info("Cant delete empty keys {} from collection {}".format(key_value_document, collection))
        return None

    def document_exists(self, query, collection):
        if self.get_document(query, collection):
            return True
        return False


