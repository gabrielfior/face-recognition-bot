from src.DbService import DbService

def test_alive(dbService : DbService):
    print(dbService)

def assert_documents_in_table(dbService, documents, tablename):

    all_entries = dbService.db.table(tablename).all()
    assert len(all_entries) == len(documents)

    for entry, document in zip(all_entries, documents):
        print(document)
        assert entry == document

def test_addDocumentsToTable(dbService : DbService):

    documents = [
            {"id": 1, "name": "Alice", "coins" : ["BTC", "NEO"]},
            {"id": 2, "name": "Bob", "coins": ["ETH", "IOT"]}
            ]
    tablename = "crypto"

    # empty table
    dbService.purge_table(tablename)
    dbService.add_documents_to_table(tablename, documents)

    assert dbService is not None
    assert_documents_in_table(dbService, documents, tablename)
